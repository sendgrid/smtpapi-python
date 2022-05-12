import os
import unittest


class ProjectTests(unittest.TestCase):

    # ./Docker or docker/Docker
    def test_docker_dir(self):
        self.assertTrue(
            os.path.isfile("./Dockerfile")
            or os.path.isdir("./docker/Dockerfile")
        )

    # ./docker-compose.yml or ./docker/docker-compose.yml
    def test_docker_compose(self):
        self.assertTrue(
            os.path.isfile('./docker-compose.yml')
            or os.path.isfile('./docker/docker-compose.yml')
        )

    # ./.env_sample
    def test_env(self):
        self.assertTrue(os.path.isfile('./.env_sample'))

    # ./.gitignore
    def test_gitignore(self):
        self.assertTrue(os.path.isfile('./.gitignore'))

    # ./CHANGELOG.md
    def test_changelog(self):
        self.assertTrue(os.path.isfile('./CHANGELOG.md'))

    # ./CODE_OF_CONDUCT.md
    def test_code_of_conduct(self):
        self.assertTrue(os.path.isfile('./CODE_OF_CONDUCT.md'))

    # ./CONTRIBUTING.md
    def test_contributing(self):
        self.assertTrue(os.path.isfile('./CONTRIBUTING.md'))

    # ./LICENSE
    def test_license(self):
        self.assertTrue(os.path.isfile('./LICENSE'))

    # ./PULL_REQUEST_TEMPLATE.md
    def test_pr_template(self):
        self.assertTrue(
            os.path.isfile('./PULL_REQUEST_TEMPLATE.md')
        )

    # ./README.rst
    def test_readme(self):
        self.assertTrue(os.path.isfile('./README.rst'))

    # ./TROUBLESHOOTING.md
    def test_troubleshooting(self):
        self.assertTrue(os.path.isfile('./TROUBLESHOOTING.md'))

    # ./USAGE.md
    def test_usage(self):
        self.assertTrue(os.path.isfile('./USAGE.md'))

    # ./VERSION.txt
    def test_use_cases(self):
        self.assertTrue(os.path.isfile('./VERSION.txt'))


if __name__ == '__main__':
    unittest.main()
