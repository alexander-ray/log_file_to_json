import sys, getopt
import json
import json_parser

def main():
    filename = ''
    levels = ["TRACE", "DEBUG", "INFO", "WARN", "ERROR"]
    keys = ["level", "timestamp", "file", "line", "message"]

    try:
        opts, args = getopt.getopt(sys.argv[1:], 'f:ld', [])
    except getopt.GetoptError as e:
        print(e)
        sys.exit(2)

    default_level = True
    for o, a in opts:
        if o == "-f":
            filename = a
        if o == "-l":
            default_level = False
            try:
                levels = levels[levels.index(a.upper()):]
            except ValueError("Invalid level specifier")

    if (default_level) levels = levels[levels.index("INFO"):]

    jp = json_parser.Json_Parser(keys)
    dicts = jp.parse_file(filename, levels)

    for d in dicts:
        json.dumps(d)

if __name__ == '__main__':
    main()
