from abc import ABC, abstractmethod

class GameInput(ABC):
  """
  An abstract class representing a generic game input. This can involve a
  combination of keystrokes or mouse clicks --- perhaps even multiple times.
  """

  @abstractmethod
  def is_empty_input(self) -> bool:
    """Returns whether this game input is an empty input.

    :returns: whether this game input is an empty input
    :rtype: bool
    """
    return False