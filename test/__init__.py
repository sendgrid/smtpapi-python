import unittest
import json
from smtpapi import SMTPAPIHeader

class TestSMTPAPI(unittest.TestCase):

  def setup(self):
    self.validHeader = json.loads('''{"to":["test@email.com"],
      "sub":{"subKey":["subValue"]},
      "section":{"testSection":"sectionValue"},
      "category":["testCategory"],
      "unique_args":{"testUnique":"uniqueValue"},
      "filters":{"testFilter":{"settings":{"filter":"filterValue"}}}}''')

  def test_add(self):
    header = SMTPAPIHeader()
    header.add_to('test@email.com')
    header.add_substitution('subKey', 'subValue')
    header.add_section('testSection', 'sectionValue')
    header.add_category('testCategory')
    header.add_unique_arg('testUnique', 'uniqueValue')
    header.add_filter('testFilter', 'filter', 'filterValue')
    self.assertEqual(self.validHeader, header.json_string())

if __name__ == '__main__':
  unittest.main()