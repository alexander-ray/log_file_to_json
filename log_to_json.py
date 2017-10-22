import sys, getopt
import json
import json_parser

def main():
    filename = ''
    levels = ["TRACE", "DEBUG", "INFO", "WARN", "ERROR"]
    keys = ["level", "timestamp", "file", "line", "message"]

    default_level = True
    file_included = False

    try:
        opts, args = getopt.getopt(sys.argv[1:], 'f:l:d:')
        for o, a in opts:
            if o == "-f":
                file_included = True
                filename = a
            if o == "-l":
                default_level = False
                try:
                    levels = levels[levels.index(a.upper()):]
                except ValueError:
                    raise ValueError("Error: Invalid level specifier")
        if (not file_included):
            raise RuntimeError("Error: filename argument required")
    except Exception as e:
        print(e)
        sys.exit(2)

    if (default_level):
        levels = levels[levels.index("INFO"):]

    jp = json_parser.Json_Parser(keys)
    try:
        jp.parse_file(filename, levels)
        for d in jp.parsed_lines:
            print(json.dumps(d))
    except Exception as e:
        for d in jp.parsed_lines:
            print(json.dumps(d))
        print(e)
        sys.exit(2)

if __name__ == '__main__':
    main()
