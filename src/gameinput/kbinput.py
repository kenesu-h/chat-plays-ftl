from gameinput.igameinput import GameInput

from typing import List

class KBInput(GameInput):
  """A class representing a keyboard input, which can consist of multiple keys
  and a number of times the input will be repeated.
  """

  def __init__(self, keys: List[str], presses: int):
    """Constructs a KBInput from a given number of key presses.

    :param keys: the keys involved in this input as a list
    :type keys: List[str]
    :param presses: the number of times to repeat this input
    :type presses: int
    """
    self.__keys: List[str] = keys
    self.__presses: int = presses

  @property
  def keys(self):
    return self.__keys

  @property
  def presses(self):
    return self.__presses

  # Override
  def is_empty_input(self) -> bool:
    return len(self.__keys) == 0 and self.__presses == 0