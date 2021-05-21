from model.botclient.abstractbotclient import AbstractBotClient
from model.botclient.message.basicmessage import BasicMessage
from model.botclient.message.imessagehandler import MessageHandler

from pydle.features import RFC1459Support
import asyncio

class IRCBotClient(AbstractBotClient, RFC1459Support):

  def __init__(self, prefix: str, username: str, token: str,
    msg_handler: MessageHandler, hostname: str, port: int) -> None:
    AbstractBotClient.__init__(self, prefix, username, token, msg_handler)
    RFC1459Support.__init__(self, self.id, [], username=self.id)
    self.__hostname: str = hostname
    self.__port: int = port

  # Override (from AbstractBotClient)
  async def initialize(self) -> None:
    await self.connect(self.__hostname, self.__port,
      password="oauth:" + self.token)
    asyncio.get_event_loop().create_task(self.handle_inputs())

  # Override (from RFC1459Support)
  async def on_connect(self) -> None:
    print("Logged in as", str(self.username))
  
  # Override (from RFC1459Support)
  async def on_message(self, target, by, message) -> None:
    '''
    The types of all arguments are unfortunately unknown (thanks Pydle docs).
    This probably won't have type annotations until I do some trial-and-error.
    '''
    self.handle_msg(BasicMessage(by, message))