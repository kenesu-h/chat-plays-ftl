from model.iapplicationmodel import ApplicationModel
from model.chatplatform import ChatPlatform
from model.botclient.botstate import BotState
from model.botclient.ibotclient import BotClient
from model.botclient.discordbotclient import DiscordBotClient
from model.botclient.ircbotclient import IRCBotClient
from model.botclient.ftl.ftlmessagehandler import FTLMessageHandler
from model.botclient.nds.ndsmessagehandler import NDSMessageHandler

from asyncio import AbstractEventLoop
from io import TextIOWrapper
from json.decoder import JSONDecodeError
from logging import Logger
from multiprocessing import Process
from os import path
from threading import Thread
from typing import Dict
import asyncio, json, logging, sys

class ApplicationModelImpl(ApplicationModel):

  def __init__(self) -> None:
    # Constants
    self.__CONFIG_FILENAME: str = "config.json"
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    self.__LOGGER: Logger = logging.getLogger()
    self.__LOOP: AbstractEventLoop = asyncio.get_event_loop()
    self.__PROCESS: Process
    self.__THREAD: Thread

    # General
    self.__client: BotClient
    self.__bot_state: BotState = BotState.STANDBY

    self.__prefix: str = ""
    self.__platform: ChatPlatform = ChatPlatform.NONE
    self.__token: str = ""

    # Twitch
    self.__username: str = ""

    # Ensure the config file is there, but make a new one if it isn't.
    self.validate_config()

  @property
  def bot_state(self) -> BotState:
    return self.__bot_state

  @bot_state.setter
  def bot_state(self, bot_state: BotState) -> None:
    self.__bot_state = bot_state

  @property
  def prefix(self) -> str:
    return self.__prefix

  @prefix.setter
  def prefix(self, prefix: str) -> None:
    self.__prefix = prefix

  @property
  def platform(self) -> ChatPlatform:
    return self.__platform

  @platform.setter
  def platform(self, platform: ChatPlatform) -> None:
    self.__platform = platform

  @property
  def token(self) -> str:
    return self.__token

  @token.setter
  def token(self, token: str) -> None:
    self.__token = token

  @property
  def username(self) -> str:
    return self.__username

  @username.setter
  def username(self, username: str) -> None:
    self.__username = username

  # Override
  def initialize(self) -> None:
    try:
      # Call config validation again in the case that the config is changed from
      # model-construction to initialization.
      self.validate_config()
      self.__client = self.create_client()
      self.__client.state_callback(self.bot_state)

      # Asynchronously start the bot.
      '''
      If it weren't for this GitHub thread, there's no way I would've figured
      out how to have client initialization be non-blocking.
      https://github.com/Rapptz/discord.py/issues/82
      '''
      self.__THREAD: Thread = Thread(target=self.__client.initialize)
      self.__THREAD.start()
    except (NotImplementedError, ValueError) as err:
      self.__LOGGER.error(err)
  
  # Override
  def stop(self) -> None:
    #self.__PROCESS.terminate()
    #self.__THREAD.join()
    self.__client.stop()
    self.__THREAD.join()
    # self.__LOOP.stop()

  # Helper
  def create_client(self) -> BotClient:
    """Creates a bot client instance corresponding to the chat platform chosen.

    :raises NotImplementedError: if bot clients for a chat platform have not been
                                implemented yet
    :raises ValueError: if an invalid platform is provided
    :return: the corresponding bot client
    :rtype: BotClient
    """
    if self.__platform == ChatPlatform.DISCORD:
      return DiscordBotClient(self.__prefix, self.__token, NDSMessageHandler()) 
      # return DiscordBotClient(self.__prefix, self.__token, FTLMessageHandler())
    elif self.__platform == ChatPlatform.TWITCH:
      return IRCBotClient(self.__prefix, self.__username, self.__token,
        FTLMessageHandler(), "irc.chat.twitch.tv", 6667)
    else:
      raise ValueError("It looks like you didn't specify a platform in config.json. "
        + "Please open it in a text editor and specify your platform (either "
        + "\"discord\" or \"twitch\").")

  # Override
  def validate_config(self) -> None:
    """Validates a configuration file at CONFIG_FILENAME. If one does not exist,
    one will be generated. Otherwise, this attempts to read from the file.
    """
    if not path.exists(self.__CONFIG_FILENAME):
      self.__LOGGER.info("No configuration file found, writing a default file.")
      self.write_config(";", ChatPlatform.NONE, "", "")
      self.__LOGGER.info("Wrote default configuration file. Please specify your "
      + "platform (either \"discord\" or \"twitch\") and your corresponding "
      + "OAuth token. Specify a username as well if you are using \"twitch\" "
      + "as your platform.")

      # Exit for now, but we probably don't want to do this once we make a GUI.
      exit(0)
    else:
      self.__LOGGER.info("Found configuration file, setting values of constants.")
      self.parse_config()

  # Override
  def write_config(self, prefix: str, platform: ChatPlatform, token: str,
    username: str) -> None:
    """Writes a new configuration file to the path set in CONFIG_FILENAME.

    :param prefix: the prefix
    :type prefix: str
    :param platform: the chat platform
    :type platform: ChatPlatform
    :param token: the OAuth token
    :type token: str
    :param username: the username
    :type username: str
    """
    config_file: TextIOWrapper = open(self.__CONFIG_FILENAME, "w")
    config_file.write(json.dumps(
      {
        "general": {
          "prefix": prefix,
          "platform": platform.value,
          "token": token
        },
        "twitch": {
          "username": username,
        }
      }
    ))
    config_file.close()
    self.__LOGGER.info("Wrote values to configuration file.")

  # Override
  def parse_config(self) -> None:
    """Attempts to parse a configuration file at CONFIG_FILENAME and will read
    from it, setting the values of global variables. If the configuration file
    cannot be read as JSON or lacks specific fields, exceptions will be thrown.
    """
    try:
      config_file: TextIOWrapper = open(self.__CONFIG_FILENAME, "r")
      config_contents: Dict[str, Dict[str, str]] = json.loads(config_file.read())
      config_file.close()

      general: Dict[str, str] = config_contents["general"]
      twitch: Dict[str, str] = config_contents["twitch"]

      self.__prefix = general["prefix"]
      self.__platform = ChatPlatform(general["platform"])
      self.__token = general["token"]

      self.__username = twitch["username"]
    except (JSONDecodeError, ValueError) as err:
      self.__LOGGER.error(err)
      exit(0)