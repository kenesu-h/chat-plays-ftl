from botclient import BotClient

if __name__ == "__main__":
  TOKEN = ""
  client: BotClient = BotClient()
  client.loop.create_task(client.handler.handle_inputs())
  client.run(TOKEN)