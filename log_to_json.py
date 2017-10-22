import sys, getopt
import json
import json_parser
#from functools import reduce

def check_dict_equality(d1, d2, ignore_key):
    ret = {k: v for k,v in d1.items() if k not in ignore_key} == {k: v for k,v in d2.items() if k not in ignore_key}
    return ret

def remove_concecutive_dups(d, ignore_key):
    l = len(d)
    if (l > 1):
        for i in reversed(range(1, l)):
            print(check_dict_equality(d[i], d[i - 1], ignore_key))
            if check_dict_equality(d[i], d[i - 1], ignore_key):
                del d[i]
    return d

def remove_all_dups(d, ignore_key):
    seen = []
    ret = []
    for e in d:
        dup = False
        for s in seen:
            if ({k: v for k,v in e.items() if k not in ignore_key} ==
                {k: v for k,v in s.items() if k not in ignore_key}):
                dup = True
                break;
        if (dup):
            continue
        seen.append(e)
        ret.append(e)
    return ret

def main():
    filename = ''
    levels = ["TRACE", "DEBUG", "INFO", "WARN", "ERROR"]
    keys = ["level", "timestamp", "file", "line", "message"]

    default_level = True
    file_included = False
    d_flag = False
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'df:l:')
        for o, a in opts:
            if o == "-f":
                file_included = True
                filename = a
            if o == "-d":
                d_flag = True
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
        filtered = []
        if (d_flag):
            filtered = remove_all_dups(jp.parsed_lines, ["timestamp"])
        else:
            filtered = remove_concecutive_dups(jp.parsed_lines, ["timestamp"])

        for d in filtered:
            print(json.dumps(d))
    except Exception as e:
        for d in jp.parsed_lines:
            print(json.dumps(d))
        print(e)
        sys.exit(2)

if __name__ == '__main__':
    main()
