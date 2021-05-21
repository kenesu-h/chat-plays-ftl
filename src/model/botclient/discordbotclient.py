from model.botclient.botstate import BotState
from model.botclient.abstractbotclient import AbstractBotClient
from model.botclient.message.basicmessage import BasicMessage
from model.botclient.message.imessagehandler import MessageHandler

from threading import Thread
import discord

class DiscordBotClient(AbstractBotClient, discord.Client):
  """A class representing discord.py's bot implementation, but adapted to fit
  the BotClient interface.
  """

  def __init__(self, prefix: str, token: str, msg_handler: MessageHandler) -> None:
    """Constants an instance of a DiscordBotClient using a given message
    handler. The message handler dictates how the bot processes messages.

    :param msg_handler: the message handler
    :type msg_handler: MessageHandler
    """
    AbstractBotClient.__init__(self, prefix, "", token, msg_handler)
    discord.Client.__init__(self)

  # Override (from AbstractBotClient)
  def initialize(self) -> None:
    self.loop.create_task(self.handle_inputs())
    try:
      self.run(self.token)
    except ValueError as err:
      # Kind of a dirty way to "cleanly" stop the loop, but oh well.
      return

  def stop(self) -> None:
    self.loop.stop()

  # Override (from discord.Client)
  async def on_ready(self):
    print("Logged in as", str(self.user))
    self.state = BotState.OK
    self.id = str(self.user.id)

  # Override (from discord.Client)
  async def on_message(self, message: discord.Message):
    self.handle_msg(BasicMessage(message.author.id, message.content))

  # Override (from discord.Client)
  async def on_disconnect(self):
    self.state = BotState.STANDBY