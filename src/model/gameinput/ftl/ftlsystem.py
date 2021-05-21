from __future__ import annotations

from enum import Enum

class FTLSystem(Enum):
  """An enumeration representing the different systems available in FTL.
  """
  NONE = "none"
  SHIELDS = "shields"
  ENGINES = "engines"
  OXYGEN = "oxygen"
  MEDBAY = "medbay"
  CLONE_BAY = "clone_bay"
  TELEPORTER = "teleporter"
  CLOAKING = "cloaking"
  MIND_CONTROL = "mind_control"
  HACKING = "hacking"
  ARTILLERY_BEAM = "artillery_beam"
  WEAPON_CONTROL = "weapon_control"
  DRONE_CONTROL = "drone_control"
  DOORS = "doors"
  BACKUP_BATTERY = "backup_battery"

  @classmethod
  def get_system(self, string: str) -> FTLSystem:
    """Returns an FTL system corresponding with the given string, if any. This
    serves as a way for users to specify a system using an abbreviation, as
    opposed to the full system name.

    :param string: the string
    :type string: str
    :raises ValueError: if the string does not correspond with any system
    :return: the corresponding FTL system
    :rtype: FTLSystem
    """
    # It's a bit of a dirty way to do it, but at least it ensures some semblance
    # of manual control over accepted terms.
    if string in ["event", "choice", "choose"]:
      return self.NONE
    elif string in ["shields", "shield", "s"]:
      return self.SHIELDS
    elif string in ["engines", "engine", "e"]:
      return self.ENGINES
    elif string in ["oxygen", "o2", "oz", "o"]:
      return self.OXYGEN
    elif string in ["medbay", "med", "mb"]:
      return self.MEDBAY
    elif string in ["clone_bay", "clone", "cb"]:
      return self.CLONE_BAY
    elif string in ["teleporter", "tele", "tp"]:
      return self.TELEPORTER
    elif string in ["cloaking", "cloak"]:
      return self.CLOAKING
    elif string in ["mind_control", "mind", "mc"]:
      return self.MIND_CONTROL
    elif string in ["hacking", "hack", "h"]:
      return self.HACKING
    elif string in ["artillery_beam", "artillery", "a"]:
      return self.ARTILLERY_BEAM
    elif string in ["weapon_control", "weapons", "weapon", "wep", "w"]:
      return self.WEAPON_CONTROL
    elif string in ["drone_control", "drones", "drone"]:
      return self.DRONE_CONTROL
    elif string in ["doors", "door"]:
      return self.DOORS
    elif string in ["backup_battery", "battery", "b"]:
      return self.BACKUP_BATTERY
    else:
      raise ValueError("String " + string
        + " could not be mapped to any FTL system.")