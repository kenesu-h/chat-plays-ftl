from model.chatplatform import ChatPlatform
from model.botclient.botstate import BotState

from abc import ABC, abstractmethod

class ApplicationViewModel(ABC):

  @property
  @abstractmethod
  def bot_state(self) -> BotState:
    return

  @bot_state.setter
  @abstractmethod
  def bot_state(self, bot_state: BotState) -> None:
    return

  @property
  @abstractmethod
  def prefix(self) -> str:
    return ""

  @prefix.setter
  @abstractmethod
  def prefix(self, prefix: str) -> None:
    return

  @property
  @abstractmethod
  def platform(self) -> ChatPlatform:
    return

  @platform.setter
  @abstractmethod
  def platform(self, platform: ChatPlatform) -> None:
    return

  @property
  @abstractmethod
  def token(self) -> str:
    return

  @token.setter
  @abstractmethod
  def token(self, token: str) -> None:
    return

  @property
  @abstractmethod
  def username(self) -> str:
    return

  @username.setter
  @abstractmethod
  def username(self, username: str) -> None:
    return

  @abstractmethod
  def initialize(self) -> None:
    return

  @abstractmethod
  def stop(self) -> None:
    return

  @abstractmethod


  @abstractmethod
  def write_config(self, prefix: str, platform: ChatPlatform, token: str,
    username: str) -> None:
    return

  @abstractmethod
  def parse_config(self) -> None:
    return