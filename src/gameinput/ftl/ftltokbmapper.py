from gameinput.kbinput import KBInput
from gameinput.ftl.ftlaction import FTLAction
from gameinput.ftl.ftlinput import FTLInput

from typing import Dict

class FTLToKBMapper():

  def __init__(self) -> None:
    self.__mappings: Dict[FTLAction, str] = {
      FTLAction.POWER_SHIELDS: "a",
      FTLAction.POWER_ENGINES: "s",
      FTLAction.POWER_OXYGEN: "f",
      FTLAction.POWER_MEDBAY: "d",
      FTLAction.POWER_CLONE_BAY: "d",
      FTLAction.POWER_TELEPORTER: "g",
      FTLAction.POWER_CLOAKING: "h",
      FTLAction.POWER_MIND_CONTROL: "k",
      FTLAction.POWER_HACKING: "l",
      FTLAction.POWER_ARTILLERY_BEAM: "y",

      FTLAction.POWER_WEAPON_1: "1",
      FTLAction.POWER_WEAPON_2: "2",
      FTLAction.POWER_WEAPON_3: "3",
      FTLAction.POWER_WEAPON_4: "4",
      FTLAction.POWER_DRONE_1: "5",
      FTLAction.POWER_DRONE_2: "6",
      FTLAction.POWER_DRONE_3: "7",

      FTLAction.EVENT_CHOICE_1: "1",
      FTLAction.EVENT_CHOICE_2: "2",
      FTLAction.EVENT_CHOICE_3: "3",
      FTLAction.EVENT_CHOICE_4: "4",

      FTLAction.OPEN_DOORS: "z",
      FTLAction.CLOSE_DOORS: "x",
      FTLAction.ACTIVATE_CLOAKING: "c",
      FTLAction.START_HACKING: "n",
      FTLAction.START_MIND_CONTROL: "m",
      FTLAction.ACTIVATE_BATTERY: "b"
    }

  def get_kb_input(self, ftl_input: FTLInput) -> KBInput:
    if ftl_input.action in self.__mappings:
      if ftl_input.presses > 0:
        return KBInput([self.__mappings[ftl_input.action]], ftl_input.presses)
      elif ftl_input.presses < 0:
        return KBInput(["shift", self.__mappings[ftl_input.action]],
          0 - ftl_input.presses)
      else:
        return KBInput([], 0)
    else:
      return KBInput([], 0)