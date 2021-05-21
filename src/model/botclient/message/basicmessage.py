from model.botclient.message.imessage import Message

class BasicMessage(Message):

  def __init__(self, author: str, content: str) -> None:
    self.__author: str = author
    self.__content: str = content

  # Override
  @property
  def author(self) -> str:
    return self.__author

  # Override
  @property
  def content(self) -> str:
    return self.__content