# log_file_to_json

### How to run
* Clone repo onto local system
* Run log_to_json.py with necessary command line arguments
  * *I ran with python 3. python 2 should work, but test cases use python 3.* (on a \*nix system, run like `python3 /path/to/log_to_json.py -l TRACE -d -f /other/path/to/test_ok_complicated.txt`)
* To run tests, run `./tester.sh` from *testing* subdirectory on a system with bash. Tests rely on existing directory structure.
  * If permissions aren't set, run `chmod 755 tester.sh`
* The python files can be placed anywhere on the system (however, they must be kept in the same directory). Log files can be anywhere on the system, as long as the correct relative or absolute file path is given when running the program.
  
### List of libraries
* `sys`
  * Necessary for getting command line arguments
* `getopt`
  * Greatly simplifies handling of command line arguments. Built in error handling. Additionally, because it functions the same as C's `getopt`, the handling of command line arguments will be familiar to most.
* `OrderedDict`
  * I chose to use python dictionaries over some other data structure because they are naturally very similar to JSON in structure (and method of printing) and dictionaries are very "pythonic". Built-in python dictionaries do not maintain key ordering and instead use their ordering post-hashing. `OrderedDict` was necessary to ensure key-value pairs remain in the proper order (e.g. "level" comes before "timestamp").
* `json`
  * I used the `json` library for the `json.dumps()` function, which makes it easy to convert & print json. Furthermore, `json.dumps()` prints python dictionaries as JSON. I could have simply printed the dictionaries mostly as-is, but the json library provides nice "pretty-print" options that are useful for debugging.
  
### Testing overview
Instead of using the normal python `unittest` framework, I chose to use a lightweight shell script for testing. I chose this testing route because a shell script makes testing the full program (including command line arguments) much more simple in structure and amount of code. This shell script compares command output with the contents of a `*.ans` file using `diff`. If the outputs are the same, nothing is printed; if the outputs are different, `diff` shows exactly what is different (just like `unittest` does). 

I am reasonably confident my solution works as intended. I'm certain my program meets the requirements specified and will function correctly in reasonably expected scenarios. Undoubtedly corner cases exist in which the program would fail, because the tests are by no means comprehensive. Given additional time, additional tests could be created to increase the confidence level.

### Assumptions
* I assume that the different log sections will be separated by one or more spaces, where all numbers of spaces >=1 are treated equally.
  * Furthermore, I do not maintain spacing in the log message. E.g. "Spacing &nbsp; &nbsp; &nbsp; test" and "Spacing test" will be considered equal and output as "Spacing test".
* I assume the filenames in the log messages are valid. Technically, each OS has a couple invalid filename characters as well as a character limit, but I chose to assume validity.
* I assume JSON is to be output with a space between colon and value.

### Example program output
`alexray$ python3 log_to_json.py -l TRACE -d -f ./testing/test_ok_complicated.txt`

`{"level": "INFO", "timestamp": "2017-09-01 13:57:29", "file": "index.go", "line": 125, "message": "Starting search"}`

`{"level": "ERROR", "timestamp": "2017-09-01 13:57:29", "file": "index.go", "line": 125, "message": "Starting search"}`

`{"level": "INFO", "timestamp": "2017-09-01 13:57:29", "file": "index.go", "line": 125, "message": "Starting sch"}`

`{"level": "TRACE", "timestamp": "2017-09-01 14:57:29", "file": "index.go", "line": 125998473, "message": "Starting sch"}`
