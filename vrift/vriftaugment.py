import discord

def vriftaugment(message):
    msg = "```\n"
    msg += "╔═════════════════╦════════════╦═════════════════════════════╗\n"
    msg += "║   Augmentation  ║ unlocks at ║         cost per run        ║\n"
    msg += "╠═════════════════╬════════════╬═════════════════════════════╣\n"
    msg += "║   Sigil Hunter  ║   Floor 5  ║         250,000 Gold        ║\n"
    msg += "╠═════════════════╬════════════╬═════════════════════════════╣\n"
    msg += "║ Secret Research ║  Floor 15  ║       500 Tower Sigils      ║\n"
    msg += "╠═════════════════╬════════════╬═════════════════════════════╣\n"
    msg += "║   Super Siphon  ║  Floor 20  ║      1000 Tower Sigils      ║\n"
    msg += "╠═════════════════╬════════════╬═════════════════════════════╣\n"
    msg += "║  Ultimate Umbra ║  Floor 25  ║ 75 Fragments of the Eclipse ║\n"
    msg += "╠═════════════════╬════════════╬═════════════════════════════╣\n"
    msg += "║   Elixir Rain   ║  Floor 40  ║      500 Tower Secrets      ║\n"
    msg += "╠═════════════════╬════════════╬═════════════════════════════╣\n"
    msg += "║ String Stepping ║  Floor 65  ║     1,500 Tower Secrets     ║\n"
    msg += "╚═════════════════╩════════════╩═════════════════════════════╝"
    msg += "\n```"

    return message.channel.send(msg)
