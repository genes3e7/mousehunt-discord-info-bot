import random
from constants import *
from vrift.prestigebase import *
from vrift.vriftcache import *

class Commands:
    def __init__(self):
        self.ls = sorted(COMMANDLIST)

    def command(self, string):
        string = string.lower()
        testTrigger = False

        # instant triggers
        for i in DONOTIRRITATE:
            if i in string:
                return self.donotirritate(i)
        for i in REPEAT:
            if i in string:
                return self.repeater(i)

        # Determines whether to react to string or not
        if TRIGGER in string:
            # test if trigger has keywords tagged to it.
            if (TRIGGER + '?') in string:
                testTrigger = True
            else:
                for i in COMMANDLIST:
                    if (TRIGGER + i) in string:
                        testTrigger = True
        else:
            return NOREPLY

        # help desk
        if (TRIGGER in string) and (not testTrigger):
            return self.helpDesk()

        # View command list
        if (TRIGGER + HELP) in string or (TRIGGER + "?") in string:
            return self.viewCommandList()

        if (TRIGGER + PRESTIGESTATS) in string:
            return prestigestats(string, TRIGGER, PRESTIGESTATS)

        if (TRIGGER + ABOUTPRESTIGE) in string:
            return aboutprestigebase()

        if (TRIGGER + VRIFTFRAGCORE) in string:
            return vriftFragCore(string, TRIGGER, VRIFTFRAGCORE)

        if (TRIGGER + VRIFTFLOORCACHE)in string:
            return vriftcache(string, TRIGGER, VRIFTFLOORCACHE)

        return ERROR

    def donotirritate(self, string):
        hateReply = [
            "No to {0}!".format(string),
            "Stop saying {0}!".format(string),
            "Too many {0}!".format(string)
        ]
        return random.choice(hateReply).upper()

    def repeater(self, string):
        triangle = []
        for i in range(10):
            triangle.append(
                ("{0}".format(string.upper()) + " ") * (i + 1) + "\n")

        repeatString = [
            (((("{0}".format(string.upper())) + " ") * 10 + "\n") * 10),
            (("{0}".format(string.upper()) + " ") * 10),
            (("{0}".format(string.upper()) + "\n") * 10),
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
        msg += "\n```\n{0}\n```".format(self.ls)

        return msg
