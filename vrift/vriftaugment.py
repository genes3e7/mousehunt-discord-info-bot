import discord

def vriftaugment(message):
    msg = "```\n"
    msg += "╔═════════════════╦════════════╦══════════════╦═══════════════════════════════════╗\n"
    msg += "║   Augmentation  ║ unlocks at ║     cost     ║               Effect              ║\n"
    msg += "║                 ║   (Floor)  ║    per run   ║                                   ║\n"
    msg += "╠═════════════════╬════════════╬══════════════╬═══════════════════════════════════╣\n"
    msg += "║   Sigil Hunter  ║      5     ║   250k Gold  ║   Adds 50% more Sigils to cache   ║\n"
    msg += "╠═════════════════╬════════════╬══════════════╬═══════════════════════════════════╣\n"
    msg += "║ Secret Research ║     15     ║  500 Sigils  ║   Adds 50% more Secrets to cache  ║\n"
    msg += "╠═════════════════╬════════════╬══════════════╬═══════════════════════════════════╣\n"
    msg += "║   Super Siphon  ║     20     ║   1k Sigils  ║       Doubles siphon effect       ║\n"
    msg += "╠═════════════════╬════════════╬══════════════╬═══════════════════════════════════╣\n"
    msg += "║  Ultimate Umbra ║     25     ║ 75 Fragments ║         Ultimate Umbra run        ║\n"
    msg += "╠═════════════════╬════════════╬══════════════╬═══════════════════════════════════╣\n"
    msg += "║   Elixir Rain   ║     40     ║  500 Secrets ║        50% Elixir drop rate       ║\n"
    msg += "╠═════════════════╬════════════╬══════════════╬═══════════════════════════════════╣\n"
    msg += "║ String Stepping ║     65     ║ 1.5k Secrets ║ Double terrified adventurer steps ║\n"
    msg += "╚═════════════════╩════════════╩══════════════╩═══════════════════════════════════╝\n"
    msg += "```"

    return message.channel.send(msg)
