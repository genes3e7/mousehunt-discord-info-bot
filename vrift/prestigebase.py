class PrestigeBase:
    def __init__(self, floor):
        self.floor = floor
        self.powerboost = self.getPowerBoost(floor)
        self.power = 490 + self.powerboost
        self.luckboost = self.getLuckBoost(floor)
        self.luck = 5 + self.luckboost

    def getPowerBoost(self, floor):
        return 10 * floor

    def getLuckBoost(self, floor):
        n = floor // 8

        if floor % 8 == 0:
            return n - 1

        return n

    def toString(self):
        prestige = [
            "Prestige Base (Floor {0})".format(self.floor),
            "{0:<10} ║ {1}({2} + {3})".format("power",
                                              self.power, 490, self.powerboost),
            "{0:<10} ║ {1}".format("powerbonus", "20%"),
            "{0:<10} ║ {1}({2} + {3})".format("luck",
                                              self.luck, 5, self.luckboost),
            "{0:<10} ║ {1}".format("attraction", "0%"),
            "{0:<10} ║ {1}".format("freshness", "Nil")
        ]
        mino = [
            "Minotaur Base",
            "{0:<10} ║ {1}".format("power", 1000),
            "{0:<10} ║ {1}".format("powerbonus", "20%"),
            "{0:<10} ║ {1}".format("luck", 15),
            "{0:<10} ║ {1}".format("attraction", "10%"),
            "{0:<10} ║ {1}".format("freshness", "Fresh")
        ]
        clock = [
            "Clockwork Base",
            "{0:<10} ║ {1}".format("power", 800),
            "{0:<10} ║ {1}".format("powerbonus", "20%"),
            "{0:<10} ║ {1}".format("luck", 13),
            "{0:<10} ║ {1}".format("attraction", "10%"),
            "{0:<10} ║ {1}".format("freshness", "Nil")
        ]
        denture = [
            "Denture Base(Charged)",
            "{0:<10} ║ {1}".format("power", 1500),
            "{0:<10} ║ {1}".format("powerbonus", "25%"),
            "{0:<10} ║ {1}".format("luck", 20),
            "{0:<10} ║ {1}".format("attraction", "25%"),
            "{0:<10} ║ {1}".format("freshness", "Nil")
        ]

        att = 12
        prestigeSLen = 31
        clockSLen = 18
        minSLen = 20
        dentureSLen = 23

        string = "╔{0}╦{1}╦{2}╦{3}╗\n".format(
            "═" * prestigeSLen, "═" * clockSLen, "═" * minSLen, "═" * dentureSLen)
        string += "║{0:^31}║{1:^18}║{2:^20}║{3:^23}║\n".format(
            prestige[0], clock[0], mino[0], denture[0])

        string += "╠{0}╦{1}╬{2}╦{3}╬{4}╦{5}╬{6}╦{7}╣\n".format(
            "═" * att, "═" * (prestigeSLen - att - 1),
            "═" * att, "═" * (clockSLen - att - 1),
            "═" * att, "═" * (minSLen - att - 1),
            "═" * att, "═" * (dentureSLen - att - 1)
        )

        for i in range(1, len(prestige)):
            string += "║ {0:<29} ║ {1:<16} ║ {2:<18} ║ {3:<21} ║\n".format(
                prestige[i], clock[i], mino[i], denture[i])

        string += "╚{0}╩{1}╩{2}╩{3}╩{4}╩{5}╩{6}╩{7}╝".format(
            "═" * att, "═" * (prestigeSLen - att - 1),
            "═" * att, "═" * (clockSLen - att - 1),
            "═" * att, "═" * (minSLen - att - 1),
            "═" * att, "═" * (dentureSLen - att - 1)
        )

        return string


def aboutprestigebase():
    msg = "```\n"
    msg += "╔═════════════════════════════╦═══════════════════════════════════════╗\n"
    msg += "║                             ║          Prestige Base >= at          ║\n"
    msg += "║             Base            ╠═══════════════════════════╦═══════════╣\n"
    msg += "║                             ║           Power           ║    Luck   ║\n"
    msg += "╠═════════════════════════════╬═══════════════════════════╬═══════════╣\n"
    msg += "║          Rift Base          ║         <Default>         ║  Floor 49 ║\n"
    msg += "╠═════════════════════════════╬═══════════════════════════╬═══════════╣\n"
    msg += "║         Fissure Base        ║         <Default>         ║  Floor 57 ║\n"
    msg += "╠═════════════════════════════╬═══════════════════════════╬═══════════╣\n"
    msg += "║        Clockwork Base       ║          Floor 31         ║  Floor 65 ║\n"
    msg += "╠═════════════════════════════╬═══════════════════════════╬═══════════╣\n"
    msg += "║   Mino Base (outside Rift)  ║          Floor 51         ║  Floor 81 ║\n"
    msg += "╠═════════════════════════════╬═══════════════════════════╬═══════════╣\n"
    msg += "║ Denture Base (outside Rift) ║         Floor 101         ║ Floor 121 ║\n"
    msg += "║                             ║ (Power Bonus lose though) ║           ║\n"
    msg += "╚═════════════════════════════╩═══════════════════════════╩═══════════╝\n"
    msg += "```"

    return msg


def prestigestats(string, trigger, key):
    try:
        idx = string.find("{0}{1}".format(trigger, key)) + \
            len(trigger) + len(key) + 1

        floor = int(string[idx:])
        if floor < 1:
            raise ValueError

        print("Val: {0} {1}\n".format(floor, type(floor)))

        msg=""
        if floor > 200:
            msg = "Realistically you should not exceed floor 200\n"
            floor = 200

        msg += "```\n"
        msg += "{0}\n".format(PrestigeBase(floor).toString())
        msg += "```"

        return msg

    except ValueError:
        msg = "Invalid value.\n"
        msg += "Enter a positive integer >= 1 after {0}\n".format(key)
        msg += "Eg. `{0}{1} <value>`".format(trigger, key)
        return msg
