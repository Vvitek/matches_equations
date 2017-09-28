import unittest

import matches

resources = [line.split('\t') for line in open('equations.tsv','r').read().rstrip().split('\n')]

class TestMatches(unittest.TestCase):

    def test_solving(self):
        for i in resources:
            with self.subTest(i=1):
                self.assertEqual(matches.solve(i[0]), i[1])

if __name__ == '__main__':
    unittest.main()
