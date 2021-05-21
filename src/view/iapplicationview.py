from abc import ABC, abstractmethod

class ApplicationView(ABC):

  @abstractmethod
  def initialize(self) -> None:
    return