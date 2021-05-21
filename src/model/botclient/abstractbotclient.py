from model.botclient.botstate import BotState
from model.botclient.ibotclient import BotClient
from model.botclient.message.imessage import Message
from model.botclient.message.imessagehandler import MessageHandler

from abc import abstractmethod
from typing import Callable
import asyncio

class AbstractBotClient(BotClient):

  def __init__(self, prefix: str, id: str, token: str,
    msg_handler: MessageHandler) -> None:
    self.__prefix: str = prefix
    self.__id: str = id
    self.__token: str = token
    self.__msg_handler: MessageHandler = msg_handler

    self.__state: BotState = BotState.STANDBY
    self.__state_callback: Callable[[BotState], None] = (lambda s: s)

  @property
  def prefix(self) -> str:
    return self.__prefix

  @property
  def id(self) -> str:
    return self.__id

  @id.setter
  def id(self, id: str) -> None:
    self.__id = id

  @property
  def token(self) -> str:
    return self.__token

  @property
  def msg_handler(self) -> MessageHandler:
    return self.__msg_handler

  @property
  def state(self) -> BotState:
    return self.__state

  @state.setter
  def state(self, state: BotState) -> None:
    self.__state = state
    self.__state_callback(state)

  @property
  def state_callback(self) -> Callable[[BotState], None]:
    return self.__state_callback

  @state_callback.setter
  def state_callback(self, callback: Callable[[BotState], None]) -> None:
    self.__state_callback = callback

  # Override
  def handle_msg(self, msg: Message) -> None:
    self.__msg_handler.handle_msg(self.__prefix, self.__id, msg)

  # Helper
  async def handle_inputs(self) -> None:
    """An asynchronous method intended for constantly parsing inputs within the
    message handler's input handler.
    """
    while True:
      self.msg_handler.input_handler.pop_input()
      # Sleeping an arbitrary, but short amount of time to keep things
      # asynchronous and parsing time short.
      await asyncio.sleep(0.01)

  @abstractmethod
  def initialize(self) -> None:
    pass