import sys
import re # Regex
from collections import OrderedDict

class Json_Parser:
    def __init__(self, keys):
        self.keys = keys
        self.parsed_lines = []

    def __timestamp_to_string(self, date, time):
        if (not date.isdigit() or len(date) != 8)
            raise RuntimeError("Invalid date")
        elif (not time.isdigit() or len(time) != 6)
            raise RuntimeError("Invalid time")

        return "%s-%s-%s %s:%s:%s" %
            (date[0:4], date[4:6], date[6,8], time[0:2], time[2:4], time[4:6])

    def parse_file(self, filename, levels):
        f = open(filename, 'r')
        lines = f.readlines()

        for line in lines:
            values = []

            # Removing punctuation
            line = re.sub('[]', '', line)
            line = re.sub(':', ' ', line)

            fields = line.split(' ') # String to list

            if (fields[0] not in levels) continue else values.append(fields[0])

            try:
                values.append(self.__timestamp_to_string(fields[1], fields[2]))

                tmp = int(fields[3])
                if (tmp <= 0):
                    raise RuntimeError("Invalid line number")
                values.append(fields[3])
            except Exception as e:
                raise

            values.append(' '.join(fields[4:]))

            self.parsed_lines.append(OrderedDict(zip(self.keys, values)))
