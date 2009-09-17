import unittest
import coverage
from alexa import alexa_etl, top_list

coverage.exclude('if __name__ == .__main__.:')


class alexaTest(unittest.TestCase):

    def test_etl(self):
        a = alexa_etl()
        first = a.next()

        # first should have a rank of 1 and the second part should be a domain
        self.assertEqual(first[0], 1, \
        "First item in alexa_etl did not have a rank of 1, "
        + "it had a rank of %d" 
        % first[0])

        # simple check to see that the first result is a domain
        # i.e. has a dot in it
        self.assertTrue(first[1].count('.') > 0, 
        "alexa_etl did not return a url")

    def test_top_list(self):
        a = top_list(10)
        self.assertEqual(len(a), 10, "top_list did not return 10 items")
        self.assertEqual(a[0][0], 1, "first item was not ranked #1")
        self.assertEqual(a[9][0], 10, 
        "tenth item was not ranked #10, rank of %d provided" % a[9][0])
