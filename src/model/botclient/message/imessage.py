from abc import ABC, abstractmethod

class Message(ABC):

  @property
  @abstractmethod
  def author(self) -> str:
    return ""

  @property
  @abstractmethod
  def content(self) -> str:
    return ""