from model.gameinput.igameinput import GameInput
from model.gameinput.igameinputhandler import GameInputHandler
from model.gameinput.kbinput import KBInput
from model.gameinput.ftl.ftlinput import FTLInput
from model.gameinput.ftl.ftltokbmapper import FTLToKBMapper

from typing import List
from win32gui import GetWindowText, GetForegroundWindow
import pyautogui

class FTLInputHandler(GameInputHandler):
  """A GameInputHandler implementation intended specifically for FTL. This
  primarily relies on a stack-based queue for keyboard inputs, which are
  retrieved from a FTLToKBMapper.
  """

  def __init__(self) -> None:
    """Constructs an instance of a FTLInputHandler.
    """
    self.__mapper: FTLToKBMapper = FTLToKBMapper()
    self.__stack: List[FTLInput] = []

  # Override
  def append(self, game_input: GameInput) -> None:
    ftl_input: FTLInput = game_input
    self.__stack.append(ftl_input)

  # Override
  def pop_input(self) -> None:
    if len(self.__stack) > 0:
      self.handle_input(self.__mapper.get_kb_input(self.__stack.pop(0)))
          
  # Override
  def handle_input(self, game_input: GameInput) -> None:
    kb_input: KBInput = game_input
    for _ in range(kb_input.presses):
      '''
      The input should only be executed while the game is focused.

      If it turns out that the game isn't focused while an input is being
      executed, ideally we should have a way to "preserve" that input until the
      window is focused again.

      The easy but more-calls-per-loop way:
      Keep attempting to complete the next step of the input. Only execute if
      the window is focused.

      The harder but less-calls-per-loop way:
      If we're in the middle of an input and can't continue it, save the
      remaining input as a KBInput and push it to the top of the stack to
      continue it later.

      But then again, the difference is probably minimal.
      '''
      if self.game_focused():
        self.fast_press_keys(kb_input)
  
  # Helper
  def game_focused(self) -> bool:
    """Returns whether the currently focused window is our game (FTL).

    :return: whether the currently focused window is our game
    :rtype: bool
    """
    return GetWindowText(GetForegroundWindow()) == "FTL: Faster Than Light"

  # Helper
  def press_keys(self, kb_input: KBInput) -> None:
    """Presses the keys in the given keyboard input. Modifier keys are held down
    first, all non-modifier keys are pressed, then the modifiers are released.

    :param kb_input: the keyboard input
    :type kb_input: KBInput
    """
    key: str
    ''' 
    This is unfortunately a REALLY slow way of handling modifiers, but it's the
    only sensible way that can support multiple modifier keys. As a result,
    you'll notice that removing power is noticeably slower than adding power.
    '''
    for key in kb_input.modifiers:
      pyautogui.keyDown(key)
    for key in kb_input.keys:
      pyautogui.press(key)
    for key in kb_input.modifiers:
      pyautogui.keyUp(key)

  # Helper
  def fast_press_keys(self, kb_input: KBInput) -> None:
    """An alternative implementation of press_keys that aims for speed rather
    than extensibility. This assumes that only one key and one accompanying
    modifier, if applicable, are given.

    :param kb_input: the keyboard input
    :type kb_input: KBInput
    """
    if len(kb_input.modifiers) == 0:
      pyautogui.press(kb_input.keys[0])
    else:
      '''
      pyautogui.hotkey will not work properly (will input just one key) if you
      don't specify the time interval between each press. This is a hacky way of
      doing it, but as far as I can see, it consistently works fine on my end.
      Hopefully this is the case for others.
      '''
      pyautogui.hotkey(kb_input.modifiers[0], kb_input.keys[0], interval=0.1)