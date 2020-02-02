import os
import sys
import discord
from constants import *
from Commands import *


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        await self.change_presence(
            status=STATUS,
            activity=discord.Game(name=GAMENAME)
        )
        print("Setting bot status to \"{0}\".".format(STATUS))
        print("Setting bot to playing \"{0}\" game.".format(GAMENAME))
        self.cmd = Commands()
        print("Loading bot commands...")
        print()
        print("The bot is ready!")

    async def on_message(self, message):
        print('Message from {0.author}:\n{0.content}\n'.format(message))

        # Prevents talking to self from taking place
        if message.author == client.user:
            print("Message ignored")
            return

        reply = self.cmd.command(message.content)

        if reply == NOREPLY:
            return
        else:
            if reply == ERROR or reply is None:
                reply = ">>> Something went wrong.\n"
                reply += "No generated reply returned"

            await message.channel.send(reply)


# Check if main script
if __name__ == '__main__':
    try:
        print("Starting discord bot practice program")
        print("-------------------------------------")
        print("Start Up Sequence Initiated")
        print("Retrieving setup information")

        client = MyClient()

        token = ""
        # Check if any arguments provided
        if len(sys.argv) > 1:
            token = sys.argv[1]
        else:
            token = input("Enter discord token:\n")

        try:
            client.run(token)
        except discord.errors.LoginFailure as e:
            print("Login unsuccessful: {0}".format(e))

    except KeyboardInterrupt:
        print("Kill Program")

    # windows terminal will return nt
    # mac and linux terminals will return posix
    # pause so user can see printouts
    if os.name == "nt":
        os.system("pause")
