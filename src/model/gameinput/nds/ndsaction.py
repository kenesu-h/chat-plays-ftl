from __future__ import annotations

from enum import Enum

class NDSAction(Enum):
  UP = "up"
  DOWN = "down"
  LEFT = "left"
  RIGHT = "right"

  Y = "y"
  X = "x"
  A = "a"
  B = "b"

  L = "l"
  R = "r"

  START = "start"
  SELECT = "select"