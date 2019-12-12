#!/usr/bin/env python3

import sys
z = sys.version

alternates = {
        '0': '08',
        '1': '124',
        '2': '2135',
        '3': '326',
        '4': '4157',
        '5': '52468',
        '6': '6359',
        '7': '748',
        '8': '85790',
        '9': '968',
}

def get_pins(observed):
    return list(yield_pins(observed))

def yield_pins(observed, prefix=""):
    if not observed:
        yield prefix
        return
    key, remaining = observed[:1], observed[1:]
    for digit in alternates.get(key, key):
        # yield from yield_pins(remaining, prefix + digit)
        for pin in yield_pins(remaining, prefix + digit):
            yield pin


z = get_pins('8')
