try:
    import unittest2 as unittest
except ImportError:
    import unittest

import datetime


class LicenseTests(unittest.TestCase):
    def test_license_year(self):
        with open("license.txt", "r") as f:
            copyright_line = f.readline().rstrip()

        self.assertEqual(
            "Copyright (c) 2012-%s SendGrid, Inc." % datetime.datetime.now().year,
            copyright_line,
        )
