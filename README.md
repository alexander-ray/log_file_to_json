# log_file_to_json

### How to run
* Clone repo onto local system
* Run log_to_json.py with necessary command line arguments
  * *python3* (on a \*nix system, run like `python3 log_to_json.py -l TRACE -d -f test_ok_complicated.txt`)
* To run tests, run `./tester.sh` from *testing* subdirectory
  * If permissions aren't set, run `chmod 755 tester.sh`
  
### List of libraries
* `sys`
  * Necessary for getting command line arguments
* `getopt`
  * Greatly simplifies handling of command line arguments. Built in error handling. Additionally, because it functions the same as C's `getopt`, the handling of command line arguments will be familiar to most.
* `OrderedDict`
  * I chose to use python dictionaries over some other data structure because they are naturally very similar to JSON in structure and printing and dictionaries are very "pythonic". Built-in python dictionaries do no maintain key ordering and instead use their ordering post-hashing. `OrderedDict` was necessary to ensure key-value pairs remain in the proper order (e.g. "level" comes before "timestamp").
* `json`
  * I used the `json` library for the `json.dumps()` function, which makes it easy to convert & print json. Furthermore, `json.dumps()` prints python dictionaries as JSON. I could have simply printed the dictionaries mostly as-is, but the json library provides nice "pretty-print" options that are useful for debugging".
  
### Testing overview
Instead of using the normal python `unittest` framework, I chose to use a lightweight shell script for testing. This shell script compares command output with the contents of a `*.ans` file using `diff`. If the outputs are the same, nothing is printed; if the outputs are different, `diff` shows exactly what is different (just like `unittest` does). I chose this testing route because a shell script makes testing the full program (including command line arguments) much more simple in structure and amount of code.

### Assumptions
* I assume that the different log sections will be separated by one or more spaces, where all numbers of spaces >1 are treated equally.
  * Furthermore, I do not maintain spacing in the log message. E.g. "Spacing &nbsp; &nbsp; &nbsp; test" and "Spacing test" will be considered equal and outputted as "Spacing test".
