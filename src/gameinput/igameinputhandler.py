from gameinput.igameinput import GameInput

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
  async def handle_inputs(self) -> None:
    """Initializes an asynchronous, constant loop to handle and run game inputs.
    """
    pass