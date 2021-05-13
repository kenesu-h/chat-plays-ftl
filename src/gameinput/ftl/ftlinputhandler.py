from gameinput.igameinput import GameInput
from gameinput.igameinputhandler import GameInputHandler
from gameinput.kbinput import KBInput
from gameinput.ftl.ftlinput import FTLInput
from gameinput.ftl.ftltokbmapper import FTLToKBMapper

from typing import List
from win32gui import GetWindowText, GetForegroundWindow
import asyncio, pyautogui

class FTLInputHandler(GameInputHandler):

  def __init__(self) -> None:
    self.__mapper: FTLToKBMapper = FTLToKBMapper()
    self.__stack: List[FTLInput] = []

  # Override
  def append(self, game_input: GameInput) -> None:
    ftl_input: FTLInput = game_input
    self.__stack.append(ftl_input)

  # Override
  async def handle_inputs(self) -> None:
    while True:
      # Only read inputs if FTL is the currently focused window.
      if GetWindowText(GetForegroundWindow()) == "FTL: Faster Than Light":
        if len(self.__stack) > 0:
          kb_input: KBInput = self.__mapper.get_kb_input(self.__stack.pop(0))
          for _ in range(kb_input.presses):
            if len(kb_input.keys) == 1:
              pyautogui.press(kb_input.keys[0])
            else:
              pyautogui.keyDown(kb_input.keys[0])
              pyautogui.press(kb_input.keys[1])
              pyautogui.keyUp(kb_input.keys[0])
      # Sleep a little bit. This is just an arbitrarily low value so there's
      # little downtime between every input read. Also this whole thing doesn't
      # work without sleeping for whatever reason.
      await asyncio.sleep(0.1)