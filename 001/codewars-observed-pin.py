#!/usr/bin/env python3
#
# https://www.codewars.com/kata/the-observed-pin/train/python

import unittest
import itertools

def get_pins(observed):

    grid = ["123",
            "456",
            "789",
            " 0 "]

    rows, cols = len(grid), len(grid[0])

    map = {}

    for x in range(rows):
        for y in range(cols):
            n = grid[x][y]
            if n != " ":
                map[n] = [n] + [grid[x1][y1]
                                for (x1,y1) in [(x+1,y), (x, y+1), (x-1, y), (x, y-1)]
                                if x1 >= 0 and x1 < rows and y1 >= 0 and y1 < cols and grid[x1][y1] != " "]

    return [''.join(c) for c in itertools.product(*[map[d] for d in observed])]


class Test(unittest.TestCase):
    def test(self):
        expectations = [
                ('8', ['5', '7', '8', '9', '0']),
                ('11', ['11', '22', '44', '12', '21', '14', '41', '24', '42']),
                ('369', ['339','366','399','658','636','258','268','669','668','266','369','398','256',
                         '296','259','368','638','396','238','356','659','639','666','359','336','299',
                         '338','696','269','358','656','698','699','298','236','239'])]

        for e in expectations:
            self.assertEqual(sorted(get_pins(e[0])), sorted(e[1]), "PIN: " + e[0])


if __name__ == "__main__":
    unittest.main(verbosity=2)
