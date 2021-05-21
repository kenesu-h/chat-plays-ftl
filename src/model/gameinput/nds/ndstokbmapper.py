from model.gameinput.kbinput import KBInput
from model.gameinput.nds.ndsaction import NDSAction
from model.gameinput.nds.ndsinput import NDSInput

from typing import Dict

class NDSToKBMapper():

  def __init__(self) -> None:
    # Assumes default DESMUME bindings
    self.__mappings: Dict[NDSAction, str] = {
      NDSAction.UP: "up",
      NDSAction.DOWN: "down",
      NDSAction.LEFT: "left",
      NDSAction.RIGHT: "right",

      NDSAction.Y: "a",
      NDSAction.X: "s",
      NDSAction.A: "x",
      NDSAction.B: "z",

      NDSAction.L: "q",
      NDSAction.R: "w",

      NDSAction.START: "enter",
      NDSAction.SELECT: "shiftright"
    }

  def get_kb_input(self, nds_input: NDSInput) -> KBInput:
    if nds_input.action in self.__mappings:
      if nds_input.presses > 0:
        return KBInput([], [self.__mappings[nds_input.action]], nds_input.presses)
      else:
        return KBInput([], [], 0)
    else:
      return KBInput([], [], 0)