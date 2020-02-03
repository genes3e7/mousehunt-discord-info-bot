import os
import sys
import discord
from constants import *
from Commands import *
from settings import DISCORD_TOKEN


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
        print(DIVIDER)

    async def on_message(self, message):
        print('Message from {0.author}:\n{0.content}'.format(message))

        # Prevents talking to self from taking place
        if message.author == client.user:
            print("<MESSAGE IGNORED>\n")
            return
        print()

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
        print(DIVIDER)
        print("Start Up Sequence Initiated")
        print("Retrieving setup information")

        client = MyClient()

        try:
            client.run(DISCORD_TOKEN)
        except discord.errors.LoginFailure as e:
            print("Login unsuccessful: {0}".format(e))

    except KeyboardInterrupt:
        print("Kill Program")

    # windows terminal will return nt
    # mac and linux terminals will return posix
    # pause so user can see printouts
    if os.name == "nt":
        os.system("pause")
