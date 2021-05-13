from __future__ import annotations

from gameinput.ftl.ftlsystem import FTLSystem

from enum import Enum
from typing import List

class FTLAction(Enum):
  # Repeatable Actions
  POWER_SHIELDS = "power_shields"
  POWER_ENGINES = "power_engines"
  POWER_OXYGEN = "power_oxygen"
  POWER_MEDBAY = "power_medbay"
  POWER_CLONE_BAY = "power_clone_bay"
  POWER_TELEPORTER = "power_teleporter"
  POWER_CLOAKING = "power_cloaking"
  POWER_MIND_CONTROL = "power_mind_control"
  POWER_HACKING = "power_hacking"
  POWER_ARTILLERY_BEAM = "power_artillery_beam"

  # ...not repeatable (or at least, they shouldn't)
  POWER_WEAPON_1 = "power_weapon_1"
  POWER_WEAPON_2 = "power_weapon_2"
  POWER_WEAPON_3 = "power_weapon_3"
  POWER_WEAPON_4 = "power_weapon_4"
  POWER_DRONE_1 = "power_drone_1"
  POWER_DRONE_2 = "power_drone_2"
  POWER_DRONE_3 = "power_drone_3"

  EVENT_CHOICE_1 = "event_choice_1"
  EVENT_CHOICE_2 = "event_choice_2"
  EVENT_CHOICE_3 = "event_choice_3"
  EVENT_CHOICE_4 = "event_choice_4"

  OPEN_DOORS = "open_doors"
  CLOSE_DOORS = "close_doors"
  ACTIVATE_CLOAKING = "activate_cloaking"
  START_HACKING = "start_hacking"
  START_MIND_CONTROL = "mind_control"
  ACTIVATE_BATTERY = "activate_battery"

  # Helper
  @classmethod
  def is_numeric(self, string: str) -> bool:
    try:
      int(string)
      return True
    except ValueError:
      return False

  @classmethod
  def get_action(self, system: FTLSystem, arg: str) -> FTLAction:
    has_arg: bool = arg != ""
    if system == FTLSystem.NONE:
      if self.is_numeric(arg) and (int(arg) >= 1 and int(arg) <= 4):
        return FTLAction("event_choice_" + arg)
      else:
        raise ValueError("A numeric in the range [1, 4] must be passed to event"
          + " choice.")
    if system == FTLSystem.SHIELDS:
      return self.POWER_SHIELDS
    elif system == FTLSystem.ENGINES:
      return self.POWER_ENGINES
    elif system == FTLSystem.OXYGEN:
      return self.POWER_OXYGEN
    elif system == FTLSystem.MEDBAY:
      return self.POWER_MEDBAY
    elif system == FTLSystem.CLONE_BAY:
      return self.POWER_CLONE_BAY
    elif system == FTLSystem.TELEPORTER:
      # We don't have control of the mouse yet, so we're only allowing
      # teleporters to be powered rather than actually controlled.
      return self.POWER_TELEPORTER
    elif system == FTLSystem.CLOAKING:
      if has_arg:
        return self.POWER_CLOAKING
      else:
        return self.ACTIVATE_CLOAKING
    elif system == FTLSystem.MIND_CONTROL:
      if has_arg:
        return self.POWER_MIND_CONTROL
      else:
        return self.START_MIND_CONTROL
    elif system == FTLSystem.HACKING:
      if has_arg:
        return self.POWER_HACKING
      else:
        return self.START_HACKING
    elif system == FTLSystem.ARTILLERY_BEAM:
      return self.POWER_ARTILLERY_BEAM
    elif system == FTLSystem.WEAPON_CONTROL:
      if self.is_numeric(arg) and (abs(int(arg)) >= 1 and abs(int(arg)) <= 4):
        return FTLAction("power_weapon_" + str(abs(int(arg))))
      else:
        raise ValueError("A numeric with an absolute value in the range [1, 4]"
          + " must be passed to weapon control.")
    elif system == FTLSystem.DRONE_CONTROL:
      if self.is_numeric(arg) and (abs(int(arg)) >= 1 and abs(int(arg)) <= 3):
        return FTLAction("power_drone_" + str(abs(int(arg))))
      else:
        raise ValueError("A numeric with an absolute value in the range [1, 3]"
          + " must be passed to drone control.")
    elif system == FTLSystem.DOORS:
      if arg == "open":
        return self.OPEN_DOORS
      elif arg == "close":
        return self.CLOSE_DOORS
      else:
        raise ValueError("Door control must be given either \"open\" or"
          + " \"close\".")
    elif system == FTLSystem.BACKUP_BATTERY:
      return self.ACTIVATE_BATTERY
    else:
      raise ValueError("")

  @classmethod
  def is_repeatable(self, action: FTLAction) -> bool:
    return (action == self.POWER_SHIELDS
        or action == self.POWER_ENGINES
        or action == self.POWER_OXYGEN
        or action == self.POWER_MEDBAY
        or action == self.POWER_CLONE_BAY
        or action == self.POWER_TELEPORTER
        or action == self.POWER_CLOAKING
        or action == self.POWER_MIND_CONTROL
        or action == self.POWER_HACKING
        or action == self.POWER_ARTILLERY_BEAM)

  @classmethod
  def is_weapon_action(self, action: FTLAction) -> bool:
    return (action == self.POWER_WEAPON_1
        or action == self.POWER_WEAPON_2
        or action == self.POWER_WEAPON_3
        or action == self.POWER_WEAPON_4)

  @classmethod
  def is_drone_action(self, action: FTLAction) -> bool:
    return (action == self.POWER_DRONE_1
        or action == self.POWER_DRONE_2
        or action == self.POWER_DRONE_3)