import random
import discord
from constants import *
from vrift.vriftcache import *
from vrift.prestigebase import *
from vrift.vriftaugment import *
from frift.batterytable import *


class Commands:
    def __init__(self, message):
        self.ls = sorted(COMMANDLIST)
        self.message = message
        self.string = self.message.content.lower()

    def error(self):
        reply = ">>> Something went wrong.\n"
        reply += "No generated reply returned"

        return reply

    def check_non_trigger_keys(self):
        # instant triggers
        for i in DONOTIRRITATE:
            if i in self.string:
                return self.message.channel.send(self.donotirritate(i))
        for i in REPEAT:
            if i in self.string:
                return self.message.channel.send(self.repeater(i))

    def command(self):
        testTrigger = False

        # Check instant triggers
        response = self.check_non_trigger_keys()
        if not(response is None):
            return response

        # Determines whether to react to self.string or not
        if TRIGGER in self.string:
            # test if trigger has keywords tagged to it.
            if (TRIGGER + '?') in self.string:
                testTrigger = True
            else:
                for i in COMMANDLIST:
                    if (TRIGGER + i) in self.string:
                        testTrigger = True
        else:
            return

        # help desk
        if (TRIGGER in self.string) and (not testTrigger):
            return self.message.channel.send(self.helpDesk())

        # View command list
        if (TRIGGER + HELP) in self.string or (TRIGGER + "?") in self.string:
            return self.message.channel.send(self.viewCommandList())

        # Check against vrift functions
        response = self.vrift_fn()
        if not(response is None):
            return response

        # Check against frift functions
        response = self.frift_fn()
        if not(response is None):
            return response

        return self.message.channel.send(self.error())

    def vrift_fn(self):
        # prestige base stats
        if (TRIGGER + PRESTIGESTATS) in self.string:
            return prestigestats(self.message, TRIGGER, PRESTIGESTATS)

        # prestige base in relation to
        if (TRIGGER + ABOUTPRESTIGE) in self.string:
            return aboutprestigebase(self.message)

        # frag/core count
        if (TRIGGER + VRIFTFRAGCORE) in self.string:
            return vriftFragCore(self.message, TRIGGER, VRIFTFRAGCORE)

        # floor cache
        if (TRIGGER + VRIFTFLOORCACHE) in self.string:
            return vriftcache(self.message, TRIGGER, VRIFTFLOORCACHE)

        # augment list
        if (TRIGGER + VRIFTAUGMENTATION) in self.string:
            return vriftaugment(self.message)

    def frift_fn(self):
        if (TRIGGER + FRIFTBATTERYTABLE) in self.string:
            return batterytable(self.message)

    def donotirritate(self):
        hateReply = [
            "No to {0}!".format(self.string),
            "Stop saying {0}!".format(self.string),
            "Too many {0}!".format(self.string)
        ]
        return random.choice(hateReply).upper()

    def repeater(self):
        triangle = []
        for i in range(10):
            triangle.append(
                ("{0}".format(self.string.upper()) + " ") * (i + 1) + "\n")

        repeatString = [
            (((("{0}".format(self.string.upper())) + " ") * 10 + "\n") * 10),
            (("{0}".format(self.string.upper()) + " ") * 10),
            (("{0}".format(self.string.upper()) + "\n") * 10),
            "".join(triangle),
            "".join(triangle[::-1])
        ]

        msg = "Repeater Triggered!!!\n"
        msg += "```\n"
        msg += random.choice(repeatString)
        msg += "\n```"
        return msg

    def helpDesk(self):
        msg = "To see list of commands type\n"
        msg += "`{0}{1}` or `{0}{2}`".format(TRIGGER, HELP, HELPSYMBOL)

        return msg

    def viewCommandList(self):
        msg = "List of commands:\n"
        msg += "> Place \'{0}\' before any of the keywords underneath".format(
            TRIGGER)
        msg += "\n```\n{0}\n```".format(' '.join(self.ls))

        return msg
