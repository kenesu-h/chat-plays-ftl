from model.botclient.message.imessage import Message
from model.gameinput.igameinputhandler import GameInputHandler

from abc import ABC, abstractmethod

class MessageHandler(ABC):

  @property
  @abstractmethod
  def input_handler(self) -> GameInputHandler:
    return None

  @abstractmethod
  def handle_msg(self, prefix: str, id: str, msg: Message) -> None:
    return