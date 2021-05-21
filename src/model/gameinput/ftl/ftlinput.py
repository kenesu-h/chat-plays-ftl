from model.gameinput.igameinput import GameInput
from model.gameinput.ftl.ftlaction import FTLAction

class FTLInput(GameInput):
  """An class representing an input for FTL. Each input is expected to specify a
  specific action.
  """

  def __init__(self, action: FTLAction, presses: int) -> None:
    """Constructs an FTL input from a target action and a number of presses.

    :param system: the target system
    :type system: FTLSystem
    :param presses: the number of times to repeat this input
    :type presses: int
    """
    self.__action: FTLAction = action
    self.__presses: int = presses

  @property
  def action(self) -> FTLAction:
    return self.__action

  @property
  def presses(self) -> int:
    return self.__presses

  # Override
  def is_empty_input(self) -> bool:
    return self.__presses == 0