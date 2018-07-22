#!/usr/local/bin/python3

import locale
import json
import sys

query = float(sys.argv[1])
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
currency = locale.currency(query, symbol=True,
                           grouping=True, international=False)


alfredDict = {
    "items": [
        {
            "title": currency,
            "arg": currency
        }, {
            "title": "{:,.2f}".format(query),
            "arg": "{:,.2f}".format(query)
        }, {
            "title": query,
            "arg": query
        }
    ]
}

print(json.dumps(alfredDict, ensure_ascii=False))
