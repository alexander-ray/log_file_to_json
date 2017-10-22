import sys, getopt
import json

import json_parser
import helper
def main():
    # Initial declarations
    h = helper.Helper()
    filename = ''
    levels = ["TRACE", "DEBUG", "INFO", "WARN", "ERROR"]
    keys = ["level", "timestamp", "file", "line", "message"]

    default_level = True
    file_included = False
    d_flag = False

    # Get arguments
    try:
        # d doesn't have arg, f & l do
        opts, args = getopt.getopt(sys.argv[1:], 'df:l:')
        for o, a in opts:
            # Filename checker
            if o == "-f":
                file_included = True
                filename = a
            # Global repeats checker
            if o == "-d":
                d_flag = True
            # Level specifier checker
            if o == "-l":
                default_level = False
                # Cut levels list to relevant levels
                try:
                    levels = levels[levels.index(a.upper()):]
                except ValueError:
                    raise ValueError("Error: Invalid level specifier")
        if (not file_included):
            raise RuntimeError("Error: filename argument required. \nSpecify file path with -f. \nSpecify minimum level with -l. \nSpecify no repeated messages with -d.")
    except Exception as e:
        print(e)
        sys.exit(2)

    # Cut TRACE and DEBUG if unspecified
    if (default_level):
        levels = levels[levels.index("INFO"):]

    # Initialize parser with key list
    jp = json_parser.Json_Parser(keys)
    try:
        jp.parse_file(filename, levels)
        filtered = []
        if (d_flag):
            filtered = h.remove_all_dups(jp.parsed_lines, ["timestamp"])
        else:
            filtered = h.remove_concecutive_dups(jp.parsed_lines, ["timestamp"])

        # Print all elements in filtered list
        for d in filtered:
            print(json.dumps(d))
    # If exception is raised, print all lines already parsed
    except Exception as e:
        filtered = []
        if (d_flag):
            filtered = h.remove_all_dups(jp.parsed_lines, ["timestamp"])
        else:
            filtered = h.remove_concecutive_dups(jp.parsed_lines, ["timestamp"])
        for d in filtered:
            print(json.dumps(d))
        print(e)
        sys.exit(2)

if __name__ == '__main__':
    main()
