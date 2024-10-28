import re
#example@gmail.com
"""regex: regular expression 
# \d - digit
# \w - word character [a-zA-Z0-9_]
# \s - whitespace
# . - any character except newline
# ^ - start of string
# $ - end of string
# * - 0 or more occurrences
# + - 1 or more occurrences
# ? - 0 or 1 occurrence
# {n} - exactly n occurrences
# {n,} - n or more occurrences
# {n,m} - between n and m occurrences"""

email_condition = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,3}$"
user_email = input("Enter email address: ")
if re.search(email_condition, user_email):
    print("sahi hai email")
else:
    print("invalid format")
