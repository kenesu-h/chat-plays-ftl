from model.gameinput.igameinput import GameInput
from model.gameinput.igameinputhandler import GameInputHandler
from model.gameinput.kbinput import KBInput
from model.gameinput.nds.ndsinput import NDSInput
from model.gameinput.nds.ndstokbmapper import NDSToKBMapper

from typing import List
from win32gui import GetWindowText, GetForegroundWindow
import pydirectinput

class NDSInputHandler(GameInputHandler):
  # TODO: You might want to abstract this, FTL handler, and GameInputHandler as
  # a whole, it might be easy to involve generics in this.

  def __init__(self) -> None:
    self.__mapper: NDSToKBMapper = NDSToKBMapper()
    self.__stack: List[NDSInput] = []

  # Override
  def append(self, game_input: GameInput) -> None:
    nds_input: NDSInput = game_input
    self.__stack.append(nds_input)

  # Override
  def pop_input(self) -> None:
    if len(self.__stack) > 0:
      self.handle_input(self.__mapper.get_kb_input(self.__stack.pop(0)))

  # Override
  def handle_input(self, game_input: GameInput) -> None:
    kb_input: KBInput = game_input
    for _ in range(kb_input.presses):
      if self.game_focused():
        self.press_keys(kb_input)

  # Helper
  def game_focused(self) -> bool:
    return str(GetWindowText(GetForegroundWindow())).startswith("DeSmuME")

  # Helper
  def press_keys(self, kb_input: KBInput) -> None:
    key: str
    for key in kb_input.modifiers:
      pydirectinput.keyDown(key)
    for key in kb_input.keys:
      pydirectinput.press(key)
    for key in kb_input.modifiers:
      pydirectinput.keyUp(key)