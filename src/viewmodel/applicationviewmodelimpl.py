from model.iapplicationmodel import ApplicationModel
from model.chatplatform import ChatPlatform
from model.botclient.botstate import BotState
from viewmodel.iapplicationviewmodel import ApplicationViewModel

class ApplicationViewModelImpl(ApplicationViewModel):

  def __init__(self, model: ApplicationModel) -> None:
    self.__model: ApplicationModel = model

  @property
  def bot_state(self) -> BotState:
    return self.__model.bot_state

  @bot_state.setter
  def bot_state(self, bot_state: BotState) -> None:
    self.__model.bot_state = bot_state

  @property
  def prefix(self) -> str:
    return self.__model.prefix

  @prefix.setter
  def prefix(self, prefix: str) -> None:
    self.__model.prefix = prefix

  @property
  def platform(self) -> ChatPlatform:
    return self.__model.platform

  @platform.setter
  def platform(self, platform: ChatPlatform) -> None:
    self.__model.platform = platform

  @property
  def token(self) -> str:
    return self.__model.token

  @token.setter
  def token(self, token: str) -> None:
    self.__model.token = token

  @property
  def username(self) -> str:
    return self.__model.username

  @username.setter
  def username(self, username: str) -> None:
    self.__model.username = username

  # Override
  def initialize(self) -> None:
    self.__model.initialize()

  # Override
  def stop(self) -> None:
    self.__model.stop()

  # Override
  def write_config(self, prefix: str, platform: ChatPlatform, token: str, username: str) -> None:
    self.__model.write_config(prefix, platform, token, username)

  # Override
  def parse_config(self) -> None:
    self.__model.parse_config()

  