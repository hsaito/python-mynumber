# Python module for My Number (マイナンバー) Validation
This module validates Japanese My Number[^1], also known as Social Security and Tax Number System. Calculation is as specified on Act on the Use of Numbers to Identify a Specific Individual
in the Administrative Procedure[^2]. 

## Functions
* verify_number -- takes one argument, a list of 12 digits. Returns True if My Number is valid, False if not.
* verify_string -- a wrapper function for verify_number. Takes one argument, a string. This will allow you to pass string of a number to verify instead of a list. Returns True if My Number is valid, False if not.
* calc_check_digit -- takes one argument, a list of 11 digits. Returns check digit in integer.
* gen_random_number -- for testing. Generate random My Number that is valid in a list.
* check_list -- check to see if the list contains valid numbers. This check is not performed automatically for a performance reason in batch processing. (NOTE: this function does not check length of the list)

Functions returns TypeError if a list of wrong number of items.

## License
Please see COPYING.

[^1]: http://www.cas.go.jp/jp/seisaku/bangoseido/english.html
[^2]: http://www.cas.go.jp/jp/seisaku/bangoseido/pdf/en3.pdf
