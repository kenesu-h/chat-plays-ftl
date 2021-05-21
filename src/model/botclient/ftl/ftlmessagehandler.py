from model.botclient.message.imessage import Message
from model.botclient.message.imessagehandler import MessageHandler

from model.gameinput.igameinputhandler import GameInputHandler
from model.gameinput.ftl.ftlaction import FTLAction
from model.gameinput.ftl.ftlinput import FTLInput
from model.gameinput.ftl.ftlinputhandler import FTLInputHandler
from model.gameinput.ftl.ftlsystem import FTLSystem

from typing import List

class FTLMessageHandler(MessageHandler):

  def __init__(self) -> None:
    self.__input_handler: FTLInputHandler = FTLInputHandler()

  # Override
  @property
  def input_handler(self) -> GameInputHandler:
    return self.__input_handler

  # Override
  def handle_msg(self, prefix: str, id: str, msg: Message) -> None:
    '''
    lmao this looks fucking ugly
    
    I realize that this could be made lots cleaner, but the reality is that I
    wanted to make commands more intuitive by having them be named after the
    system to target.
    '''

    # Ensure that the message starts with our prefix first.
    if msg.author != id and msg.content.startswith(prefix):
      content: List[str] = msg.content[1:].split(" ")

      if len(content) > 0:
        try:
          # The system should ALWAYS be the first argument.
          system: FTLSystem = FTLSystem.get_system(content[0])
          action: FTLAction

          # If just the system name is given, parse it as a single input with no
          # argument.
          if len(content) == 1:
            action = FTLAction.get_action(system, "")
            self.__input_handler.append(FTLInput(action, 1))

          # Otherwise, it gets plenty more complex.
          else:
            # Get the corresponding action; this matters since this will
            # differentiate allocating power to something like cloaking, rather
            # than activating cloak.
            action = FTLAction.get_action(system, content[1])

            # If the action is a repeatable action (power allocation), make sure
            # the amount of times to repeat isn't greater than 8.
            if FTLAction.is_repeatable(action):
              if abs(int(content[1])) <= 8:
                self.__input_handler.append(FTLInput(action, int(content[1])))
              else:
                raise ValueError("Absolute value of power must be less than or equal to 8.")
              
            # Otherwise, we have to check for if we're targeting weapons,
            # drones, or something else (like event choice).
            else:
              # If we're targeting weapons or drones, give either 1 or -1
              # presses depending on whether the number (for the target
              # weapon/drone slot) was positive or negative. This especially
              # matters since targeting a specific slot only requires one input.
              if FTLAction.is_weapon_action(action) or FTLAction.is_drone_action(action):
                self.__input_handler.append(FTLInput(action, 1 if int(content[1]) > 0 else -1))
                
              # Otherwise, just give a single input.
              else:
                self.__input_handler.append(FTLInput(action, 1))
        except ValueError as err:
          print(err)