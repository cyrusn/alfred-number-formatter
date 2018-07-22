#!/usr/local/bin/python3

import locale
import re
import sys

query = sys.argv[1]


dollars = re.split(r"\n|\,\s|\;|\s|\+", query)

result = 0.0
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

for dollar in dollars:
    reg = r"(?P<number>[0-9|\,|\.]+)"
    var = re.search(reg, dollar)
    if var != None:
        result += locale.atof(var['number'])


print(result, end='')
