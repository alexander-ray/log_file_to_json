#!/bin/bash

echo "test_no_filename"
expect=`cat test_no_filename.ans`
got=`python3 ../log_to_json.py`
diff <( echo "$expect" ) <( echo "$got" )

echo "test_invalid_filename"
expect="[Errno 2] No such file or directory: 'test_invalid_dae.txt'"
got=`python3 ../log_to_json.py -f test_invalid_dae.txt`
diff <( echo "$expect" ) <( echo "$got" )

echo "test_level_filter"
expect=`cat test_level_filter.ans`
got=`python3 ../log_to_json.py -f test_level_filter.txt -l ERROR`
diff <( echo "$expect" ) <( echo "$got" )

echo "test_remove_all_dups"
expect=`cat test_remove_all_dups.ans`
got=`python3 ../log_to_json.py -f test_remove_all_dups.txt -d`
diff <( echo "$expect" ) <( echo "$got" )

echo "test_invalid_date"
expect=`cat test_invalid_date.ans`
got=`python3 ../log_to_json.py -f test_invalid_date.txt`
diff <( echo "$expect" ) <( echo "$got" )

echo "test_0_line_number"
expect=`cat test_0_line_number.ans`
got=`python3 ../log_to_json.py -f test_0_line_number.txt`
diff <( echo "$expect" ) <( echo "$got" )

echo "test_empty_line"
expect=`cat test_empty_line.ans`
got=`python3 ../log_to_json.py -f test_empty_line.txt`
diff <( echo "$expect" ) <( echo "$got" )

echo "test_garbled_line"
expect=`cat test_garbled_line.ans`
got=`python3 ../log_to_json.py -f test_garbled_line.txt`
diff <( echo "$expect" ) <( echo "$got" )

echo "test_ok_single_line"
expect=`cat test_ok_single_line.ans`
got=`python3 ../log_to_json.py -f test_ok_single_line.txt`
diff <( echo "$expect" ) <( echo "$got" )

echo "test_ok_complicated"
expect=`cat test_ok_complicated.ans`
got=`python3 ../log_to_json.py -l TRACE -d -f test_ok_complicated.txt`
diff <( echo "$expect" ) <( echo "$got" )

echo "test_normal"
expect=`cat test_normal.ans`
got=`python3 ../log_to_json.py -f test_normal.txt`
diff <( echo "$expect" ) <( echo "$got" )
