import os

try:
    import unittest2 as unittest
except ImportError:
    import unittest


class ProjectTests(unittest.TestCase):

    # ./Docker or docker/Docker
    def test_dockerfile(self):
        self.assertEqual(True, os.path.isfile("./Dockerfile") or os.path.isfile("./docker/Dockerfile"))

    # ./docker-compose.yml or ./docker/docker-compose.yml
    def test_docker_compose(self):
        self.assertEqual(True, os.path.isfile('./docker-compose.yml') or os.path.isfile('./docker/docker-compose.yml'))

    # ./.env_sample
    def test_env(self):
        self.assertEqual(True, os.path.isfile('./.env_sample'))

    # ./.gitignore
    def test_gitignore(self):
        self.assertEqual(True, os.path.isfile('./.gitignore'))

    # ./.travis.yml
    def test_travis(self):
        self.assertEqual(True, os.path.isfile('./.travis.yml'))

    # ./.codeclimate.yml
    def test_codeclimate(self):
        self.assertEqual(True, os.path.isfile('./.codeclimate.yml'))

    # ./CHANGELOG.md
    def test_changelog(self):
        self.assertEqual(True, os.path.isfile('./CHANGELOG.md'))

    # ./CODE_OF_CONDUCT.md
    def test_code_of_conduct(self):
        self.assertEqual(True, os.path.isfile('./CODE_OF_CONDUCT.md'))

    # ./CONTRIBUTING.md
    def test_contributing(self):
        self.assertEqual(True, os.path.isfile('./CONTRIBUTING.md'))

    # ./ISSUE_TEMPLATE.md
    def test_issue_template(self):
        self.assertEqual(True, os.path.isfile('./ISSUE_TEMPLATE.md'))

    # ./LICENSE.md
    def test_license(self):
        self.assertEqual(True, os.path.isfile('./LICENSE.md') or os.path.isfile('./LICENSE.txt'))

    # ./PULL_REQUEST_TEMPLATE.md
    def test_pr_template(self):
        self.assertEqual(True, os.path.isfile('./PULL_REQUEST_TEMPLATE.md'))

    # ./README.rst
    def test_readme(self):
        self.assertEqual(True, os.path.isfile('./README.rst'))

    # ./TROUBLESHOOTING.md
    def test_troubleshooting(self):
        self.assertEqual(True, os.path.isfile('./TROUBLESHOOTING.md'))

    # ./USAGE.md
    def test_usage(self):
        self.assertEqual(True, os.path.isfile('./USAGE.md'))

    # ./VERSION.txt
    def test_use_cases(self):
        self.assertEqual(True, os.path.isfile('./VERSION.txt'))


if __name__ == '__main__':
    unittest.main()
