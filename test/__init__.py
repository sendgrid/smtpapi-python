import decimal
import json
import os
import unittest
import datetime

from smtpapi import SMTPAPIHeader


class TestSMTPAPI(unittest.TestCase):

    def setUp(self):
        self.validHeader = json.loads('''{"to":["test@email.com",
        "test2@email.com", "test3@email.com"],
        "sub":{"subKey":["subValue"],"decimalKey":[1.23456789]},
        "section":{"testSection":"sectionValue"},
        "category":["testCategory"],
        "unique_args":{"testUnique":"uniqueValue"},
        "asm_group_id":42,
        "send_each_at":[1409348513, 1409348514],
        "send_at": 1409348515,
        "ip_pool": "testPool",
        "filters":{"testFilter":{"settings":{"filter":"filterValue"}}}}''')

        self.dropsHeader = json.loads('''{
        "sub":{"subKey":["subValue"],"decimalKey":[1.23456789]},
        "unique_args":{"testUnique":"uniqueValue"},
        "filters":{"testFilter":{"settings":{"filter":"filterValue"}}}}''')

    def test_add(self):
        header = SMTPAPIHeader()
        header.add_to('test@email.com')
        header.add_to(['test2@email.com', 'test3@email.com'])
        header.add_substitution('subKey', 'subValue')
        header.add_substitution('decimalKey', decimal.Decimal("1.23456789"))
        header.add_section('testSection', 'sectionValue')
        header.add_category('testCategory')
        header.add_unique_arg('testUnique', 'uniqueValue')
        header.set_asm_group_id(42)
        header.add_send_each_at(1409348513)
        header.add_send_each_at(1409348514)
        header.set_send_at(1409348515)
        header.set_ip_pool('testPool')
        header.add_filter('testFilter', 'filter', 'filterValue')
        self.assertEqual(self.validHeader, json.loads(header.json_string()))

    def test_set(self):
        header = SMTPAPIHeader()
        header.set_tos(["test@email.com", "test2@email.com", "test3@email.com"])
        header.set_substitutions({
            "subKey": ["subValue"],
            "decimalKey": [decimal.Decimal("1.23456789")]
        })
        header.set_sections(json.loads('{"testSection":"sectionValue"}'))
        header.set_categories(["testCategory"])
        header.set_unique_args(json.loads('{"testUnique":"uniqueValue"}'))
        header.set_asm_group_id(42)
        header.set_send_each_at([1409348513, 1409348514])
        header.set_send_at(1409348515)
        header.set_ip_pool('testPool')
        header.add_filter('testFilter', 'filter', 'filterValue')
        self.assertEqual(self.validHeader, json.loads(header.json_string()))

    def test_drop_empty(self):
        header = SMTPAPIHeader()
        header.set_tos([])
        header.set_substitutions({
            "subKey": ["subValue"],
            "decimalKey": [decimal.Decimal("1.23456789")]
        })
        header.set_sections(json.loads('{}'))
        header.set_categories([])
        header.set_unique_args(json.loads('{"testUnique":"uniqueValue"}'))
        header.set_asm_group_id(None)
        header.set_send_each_at([])
        header.set_ip_pool(None)
        header.add_filter('testFilter', 'filter', 'filterValue')
        self.assertEqual(self.dropsHeader, json.loads(header.json_string()))

    def test_license_year(self):
        LICENSE_FILE = 'LICENSE.md'
        copyright_line = ''
        with open(LICENSE_FILE, 'r') as f:
            for line in f:
                if line.startswith('Copyright'):
                    copyright_line = line.strip()
                    break
        self.assertEqual('Copyright (C) %s, Twilio SendGrid, Inc. <help@twilio.com>' % datetime.datetime.now().year, copyright_line)


class TestRepository(unittest.TestCase):

    def setUp(self):

        self.required_files = [
            ['./Dockerfile', './docker/Dockerfile'],
            ['./docker-compose.yml', './docker/docker-compose.yml'],
            './.codeclimate.yml',
            './.env_sample',
            './ISSUE_TEMPLATE.md',
            './PULL_REQUEST_TEMPLATE.md',
            './.gitignore',
            './.travis.yml',
            './CHANGELOG.md',
            './CODE_OF_CONDUCT.md',
            './CONTRIBUTING.md',
            ['./LICENSE.md', './LICENSE.txt'],
            './README.rst',
            './TROUBLESHOOTING.md',
            './USAGE.md',
            './VERSION.txt',
        ]

        self.file_not_found_message = 'File "{0}" does not exist in repo!'

    def test_repository_files_exists(self):

        for file_path in self.required_files:
            if isinstance(file_path, list):
                # multiple file paths: assert that any one of the files exists
                self.assertTrue(any(os.path.exists(f) for f in file_path),
                                msg=self.file_not_found_message.format('" or "'.join(file_path)))
            else:
                self.assertTrue(os.path.exists(file_path), msg=self.file_not_found_message.format(file_path))


if __name__ == '__main__':
    unittest.main()
