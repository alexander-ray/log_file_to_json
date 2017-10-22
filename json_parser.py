import sys
from collections import OrderedDict

class Json_Parser:
    def __init__(self, keys):
        self.keys = keys
        self.parsed_lines = []

    # "valid" timestamp if everything is a digit, lengths are correct
    def __timestamp_to_string(self, date, time):
        if (not date.isdigit() or len(date) != 8):
            raise RuntimeError("Error: Invalid date")
        elif (not time.isdigit() or len(time) != 6):
            raise RuntimeError("Error: Invalid time")

        # Format return string
        ret = "%s-%s-%s %s:%s:%s" % (date[0:4], date[4:6], date[6:8], time[0:2], time[2:4], time[4:6])
        return ret

    def parse_file(self, filename, levels):
        f = open(filename, 'r')
        lines = f.readlines()

        for line in lines:
            values = []
            # Setting up list of words
            line = line.replace('[', '')
            line = line.replace(']', '')
            line = line.replace(':', ' ')
            fields = line.split() # String to list

            # Skip entry if not in specified level set
            if (fields[0] not in levels):
                continue
            else:
                values.append(fields[0])

            try:
                # Add formatted timestamp
                values.append(self.__timestamp_to_string(fields[1], fields[2]))
                # Add filename
                # Assume valid
                values.append(fields[3])

                # Add line number, if valid
                tmp = int(fields[4])
                if (tmp <= 0):
                    raise RuntimeError("Error: Invalid line number")
                values.append(fields[4])
            except Exception as e:
                raise

            # Append log message
            values.append(' '.join(fields[5:]))
            # Add OrderedDict of full log entry
            self.parsed_lines.append(OrderedDict(zip(self.keys, values)))
