from model.botclient.message.imessage import Message
from model.botclient.message.imessagehandler import MessageHandler

from model.gameinput.igameinputhandler import GameInputHandler
from model.gameinput.nds.ndsaction import NDSAction
from model.gameinput.nds.ndsinput import NDSInput
from model.gameinput.nds.ndsinputhandler import NDSInputHandler

from typing import List

class NDSMessageHandler(MessageHandler):

  def __init__(self) -> None:
    self.__input_handler: NDSInputHandler = NDSInputHandler()

  @property
  def input_handler(self) -> GameInputHandler:
    return self.__input_handler

  # Override
  def handle_msg(self, prefix: str, id: str, msg: Message) -> None:
    if msg.author != id and msg.content.startswith(prefix):
      content: List[str] = msg.content[1:].split(" ")
      if len(content) > 0:
        try:
          action: NDSAction = NDSAction(content[0].lower())
          # If there's an argument, then it's probably the number of times to
          # press. This isn't as complex as the FTL inputs.
          if len(content) >= 2:
            self.__input_handler.append(NDSInput(action, int(content[1])))
          # If there's no arguments, we can safely assume that the user wants to
          # just press the button once.
          else:
            self.__input_handler.append(NDSInput(action, 1))
        except ValueError as err:
          print(err)