from model.gameinput.igameinput import GameInput
from model.gameinput.nds.ndsaction import NDSAction

class NDSInput(GameInput):
  # TODO: Abstract NDS and FTLInput classes

  def __init__(self, action: NDSAction, presses: int) -> None:
    self.__action: NDSAction = action
    self.__presses: int = presses

  @property
  def action(self) ->  NDSAction:
    return self.__action

  @property
  def presses(self) -> int:
    return self.__presses

  # Override
  def is_empty_input(self) -> bool:
    return self.__presses == 0