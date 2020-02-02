import csv

KIV = "Feature under construction\nTry again later"
CACHEDATA = "vrift/vriftcache.csv"


class FragCoreCount:
    def __init__(self, floor):
        self.divider = "-" * 51 + "\n"
        self.floor = int(floor)
        if floor < 1:
            raise ValueError

    def floordiv(self, floor):
        return floor//8

    def floorMod(self, floor):
        return floor % 8

    def currFrag(self, floor):
        if (self.floordiv(floor) == 0):
            return 0
        if (self.floordiv(floor) == 1):
            return 1
        return 1 + 2 * (self.floordiv(floor) - 1)

    def cummFrag(self, floor):
        total = 0
        if (self.floordiv != 0):
            for i in range(1, self.floordiv(floor) + 1):
                total = total + self.currFrag(i * 8) + 1
        return total

    def cummFragFire(self, floor):
        total = 0
        if (self.floordiv(floor) != 0):
            for i in range(1, self.floordiv(floor) + 1):
                total = total + self.currFrag(i * 8) + 1
        return total

    def stats(self, floor):
        msg = ""
        msg += "Frag/Core drop for {0} floor:{1:>22}\n".format(
            self.floordiv(floor) * 8,
            "{0} frag/core".format(self.currFrag(floor))
        )
        msg += "Frag/Core drop total till {0} floor:{1:>15}\n".format(
            self.floor,
            "{0} frag/core".format(self.cummFrag(floor))
        )

        currFragFire = self.currFrag(floor)

        if currFragFire != 0:
            currFragFire += 1

        msg += "\nWith fire\n"
        msg += "Frag/Core drop for {0} floor:{1:>22}\n".format(
            self.floordiv(floor) * 8,
            "{0} frag/core".format(currFragFire)
        )
        msg += "Frag/Core drop total till {0} floor:{1:>15}\n".format(
            self.floor,
            "{0} frag/core".format(self.cummFragFire(floor))
        )
        return msg

    def toString(self):
        msg = "Current floor: {0}\n".format(self.floor)
        floor = self.floor
        if not(self.floorMod(floor) == 0):
            msg += "Floor not divisible by 8\n"
            msg += self.divider
            msg += "Prev floor with frag/core: {0}\n".format(
                self.floordiv(floor) * 8)

        msg += self.stats(floor)

        if not(self.floorMod(floor) == 0):
            msg += self.divider
            self.floor = (self.floordiv(floor) + 1) * 8
            msg += "Next floor with frag/core: {0}\n".format(
                self.floordiv(floor) * 8)
            msg += self.stats(floor)

        return msg


def vriftcache(string, trigger, key):
    try:
        idx = string.find("{0}{1}".format(trigger, key)) + \
            len(trigger) + len(key) + 1

        floor = int(string[idx:])
        if floor < 1:
            raise ValueError

        print("Val: {0} {1}\n".format(floor, type(floor)))

        floorData = {}

        with open(CACHEDATA, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0

            for row in csv_reader:
                line_count += 1
                #print("line_count: {0} {1}".format(line_count,row))

                if line_count == floor or line_count == 200:
                    floorData = row
                    break

        print("\nTEST!!!")
        print("{0}\n".format(floorData.keys()))

        fieldName = []
        values = []
        for i in floorData.keys():
            fieldName.append(i)
            values.append(floorData[i])

        top_left = "╔"
        top_right = "╗"
        top_center = "╦"

        left_center = "╠"
        center = "╬"
        right_center = "╣"

        bottom_left = "╚"
        botton_center = "╩"
        botton_right = "╝"

        horizontal = "═"
        vertical = "║"

        msg = ""

        if floor > 200:
            msg += "Maximum floor cache: 200\n"

        msg += "```\n"
        msg += "{0}{3:^7}{1}{4:^7}{1}{5:^14}{1}{6:^15}{1}{7:^12}{2}\n".format(
            top_left, top_center, top_right,
            horizontal * 7, horizontal * 7, horizontal * 14,
            horizontal * 15, horizontal * 12
        )
        msg += "{0}{1[0]:^7}{0}{1[1]:^7}{0}{1[2]:^14}{0}{1[3]:^15}{0}{1[4]:^12}{0}\n".format(
            vertical, fieldName
        )
        msg += "{0}{3:^7}{1}{4:^7}{1}{5:^14}{1}{6:^15}{1}{7:^12}{2}\n".format(
            left_center, center, right_center,
            horizontal * 7, horizontal * 7, horizontal * 14,
            horizontal * 15, horizontal * 12
        )
        msg += "{0}{1[0]:^7}{0}{1[1]:^7}{0}{1[2]:^14}{0}{1[3]:^15}{0}{1[4]:^12}{0}\n".format(
            vertical, values
        )
        msg += "{0}{3:^7}{1}{4:^7}{1}{5:^14}{1}{6:^15}{1}{7:^12}{2}\n".format(
            bottom_left, botton_center, botton_right,
            horizontal * 7, horizontal * 7, horizontal * 14,
            horizontal * 15, horizontal * 12
        )
        msg += "```"

        return msg

    except ValueError:
        msg = "Invalid value.\n"
        msg += "Enter a positive integer >= 1 after {0}\n".format(key)
        msg += "Eg. `{0}{1} <value>`".format(trigger, key)
        return msg


def vriftFragCore(string, trigger, key):
    try:
        idx = string.find("{0}{1}".format(trigger, key)) + \
            len(trigger) + len(key) + 1

        floor = int(string[idx:])
        if floor < 1:
            raise ValueError

        print("Val: {0} {1}\n".format(floor, type(floor)))

        msg = "```\n{0}\n```".format(FragCoreCount(floor).toString())

        return msg

    except ValueError:
        msg = "Invalid value.\n"
        msg += "Enter a positive integer >= 1 after {0}\n".format(key)
        msg += "Eg. `{0}{1} <value>`".format(trigger, key)
        return msg
