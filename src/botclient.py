from gameinput.ftl.ftlaction import FTLAction
from gameinput.ftl.ftlsystem import FTLSystem
from gameinput.ftl.ftlinput import FTLInput
from gameinput.ftl.ftlinputhandler import FTLInputHandler

from typing import List

import discord

class BotClient(discord.Client):

  def __init__(self) -> None:
    super().__init__()
    self.__handler: FTLInputHandler = FTLInputHandler()

  @property
  def handler(self) -> FTLInputHandler:
    return self.__handler

  # Helper
  def is_numeric(self, string: str) -> bool:
    try:
      int(string)
      return True
    except ValueError:
      return False

  async def on_ready(self):
    print("Logged in as", str(self.user))

  async def on_message(self, msg: discord.Message):
    # Ensure that the message starts with our prefix first.
    if msg.author != self.user and msg.content.startswith(";"):
      content: List[str] = msg.content[1:].split(" ")

      if len(content) > 0:
        try:
          system: FTLSystem = FTLSystem.get_system(content[0])
          action: FTLAction
          if len(content) == 1:
            action = FTLAction.get_action(system, "")
            self.__handler.append(FTLInput(action, 1))
          else:
            # Only care about the first argument.
            action = FTLAction.get_action(system, content[1])
            if FTLAction.is_repeatable(action):
              if abs(int(content[1])) <= 8:
                self.__handler.append(FTLInput(action, int(content[1])))
              else:
                raise ValueError("Absolute value of power must be less than or equal to 8.")
            else:
              if FTLAction.is_weapon_action(action) or FTLAction.is_drone_action(action):
                self.__handler.append(FTLInput(action, 1 if int(content[1]) > 0 else -1))
              else:
                self.__handler.append(FTLInput(action, 1))
        except ValueError as err:
          print(err)