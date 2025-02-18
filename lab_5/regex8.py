import re

def split_at_uppercase(s):
    return re.findall(r'[A-Z][^A-Z]*', s)

string = "HelloWorldThisIsPython"
result = split_at_uppercase(string)
print(result)
