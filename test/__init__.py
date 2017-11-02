import decimal
import json
import os
import unittest

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


class TestFilesExist(unittest.TestCase):
    def setUp(self):
        self.files_required = [
            ['./Dockerfile', 'docker/Dockerfile'],
            ['./docker-compose.yml', './docker/docker-compose.yml'],
            './.env_sample',
            './.gitignore',
            './.travis.yml',
            './.codeclimate.yml',
            './CHANGELOG.md',
            './CODE_OF_CONDUCT.md',
            './CONTRIBUTING.md',
            './.github/ISSUE_TEMPLATE',
            ['./LICENSE.md', '.LICENSE.txt'],
            './.github/PULL_REQUEST_TEMPLATE',
            './README.md',
            './TROUBLESHOOTING.md',
            './USAGE.md',
            './USE_CASES.md'
        ]
        self.file_missing_msg = '"{}" missing in repo'

    def test_file_exists(self):

        for file in self.files_required:
            if isinstance(file, list):
                self.assertTrue(any(os.path.exists(f) for f in file),
                                msg=self.file_missing_msg.format('" or "'.join(file)))
            else:
                self.assertTrue(os.path.exists(file), msg=self.file_missing_msg.format(file))


if __name__ == '__main__':
    unittest.main()
