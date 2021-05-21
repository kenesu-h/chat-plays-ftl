from model.botclient.botstate import BotState
from model.botclient.message.imessage import Message
from model.botclient.message.imessagehandler import MessageHandler

from abc import ABC, abstractmethod
from typing import Callable

class BotClient(ABC):

  @property
  @abstractmethod
  def prefix(self) -> str:
    return ""

  @property
  @abstractmethod
  def id(self) -> str:
    return ""

  @id.setter
  @abstractmethod
  def id(self, id: str) -> None:
    return

  @property
  @abstractmethod
  def token(self) -> str:
    return ""

  @property
  @abstractmethod
  def msg_handler(self) -> MessageHandler:
    return None

  @property
  @abstractmethod
  def state(self) -> BotState:
    return None

  @state.setter
  @abstractmethod
  def state(self, state: BotState) -> None:
    return

  @property
  @abstractmethod
  def state_callback(self) -> Callable[[BotState], None]:
    return None

  @state_callback.setter
  @abstractmethod
  def state_callback(self, callback: Callable[[BotState], None]) -> None:
    return

  @abstractmethod
  def handle_msg(self, msg: Message) -> None:
    """Handles a given message and performs a corresponding action.

    :param msg: the message
    :type msg: Message
    """
    return

  @abstractmethod
  def initialize(self) -> None:
    """Initializes the bot by logging in and connecting to a chat platform.
    """
    return