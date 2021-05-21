from model.gameinput.igameinput import GameInput

from abc import ABC, abstractmethod

class GameInputHandler(ABC):
  """
  An abstract class representing a game input handler. In order to avoid inputs
  being mixed up, handlers are expected to operate on a queue (or stack) and
  iterate on it.
  """

  @abstractmethod
  def append(self, game_input: GameInput) -> None:
    """Appends a game input to this handler's internal stack.

    :param game_input: the game input
    :type game_input: GameInput
    """
    return

  @abstractmethod
  def pop_input(self) -> None:
    """Pops the game input at the top of this handler's internal stack.
    """
    return

  @abstractmethod
  def handle_input(self, game_input: GameInput) -> None:
    """Parses a game input and performs a corresponding action.

    :param game_input: the game input
    :type game_input: GameInput
    """
    return