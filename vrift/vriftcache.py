import csv

KIV = "Feature under construction\nTry again later"
CACHEDATA = "vrift/vriftcache.csv"


class FragCoreCount:
    def __init__(self, floor):
        self.floor = int(floor)
        if self.floor < 1:
            raise ValueError

        self.eclipse = self.floor // 8
        self.eclipse_floor = self.floor % 8 == 0
        self.current_total = 0
        for i in range(self.eclipse):
            self.current_total += self.eclipse_frag(i + 1)

    def eclipse_frag(self, eclipse):
        if eclipse == 0:
            return 0
        return 1 + 2 * (eclipse - 1)

    def stats(self, floor, is_next_floor):
        floor_fragcore = self.eclipse_frag(self.eclipse)
        total_fragcore = self.current_total
        total_fragcore_fire = self.current_total + self.eclipse
        if is_next_floor:
            floor_fragcore = self.eclipse_frag(self.eclipse + 1)
            total_fragcore += floor_fragcore
            total_fragcore_fire += floor_fragcore + 1

        msg = ""
        msg += "Frag/Core drop for {0} floor:{1:>22}\n".format(
            floor, "{0} frag/core".format(floor_fragcore)
        )
        msg += "Frag/Core drop total till {0} floor:{1:>15}\n".format(
            floor, "{0} frag/core".format(total_fragcore)
        )

        msg += "\nWith fire\n"
        msg += "Frag/Core drop for {0} floor:{1:>22}\n".format(
            floor, "{0} frag/core".format(
                floor_fragcore if floor_fragcore == 0 else floor_fragcore + 1
            )
        )
        msg += "Frag/Core drop total till {0} floor:{1:>15}\n".format(
            floor, "{0} frag/core".format(total_fragcore_fire)
        )
        return msg

    def toString(self):
        divider = "-" * 51 + "\n"
        floor = self.eclipse * 8

        msg = "Current floor: {0}\n".format(self.floor)
        if not self.eclipse_floor:
            msg += "Floor not divisible by 8\n"
            msg += divider
            msg += "Prev floor with frag/core: {0}\n".format(floor)

        msg += self.stats(floor, False)

        if not self.eclipse_floor:
            msg += divider
            msg += "Next floor with frag/core: {0}\n".format(floor + 8)
            msg += self.stats(floor + 8, True)

        return msg


def vriftcache(string, trigger, key):
    try:
        idx = string.find("{0}{1}".format(trigger, key)) + \
            len(trigger) + len(key) + 1

        floor = int(string[idx:])
        if floor < 1:
            raise ValueError

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

        floor = string[idx:]

        msg = "```\n{0}\n```".format(FragCoreCount(floor).toString())

        return msg

    except ValueError:
        msg = "Invalid value.\n"
        msg += "Enter a positive integer >= 1 after {0}\n".format(key)
        msg += "Eg. `{0}{1} <value>`".format(trigger, key)
        return msg
