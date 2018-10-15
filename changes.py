"""
Small python script that, when run, will update the CHANGELOG with information
about all merged pull requests since the previous release.

This script must be run after tagging the latest version
It checks the log of commits since the previous tag and parses it
"""
import re
import subprocess
import sys

RELEASE_MD_PATTERN = re.compile(r'## \[(\d+\.\d+\.\d+)\]')
MERGED_PR_PATTERN = re.compile(
    r'[0-9a-f]{7} Merge pull request #(\d+) from (.+)/.+'
)

# Get latest tag
command = 'git tag'.split(' ')
res = subprocess.run(command, capture_output=True, text=True)
if res.returncode != 0:
    print('Error occurred when running git tag command:', str(res.stderr))
    sys.exit(1)
# Get the last line and get the tag number
latest_release = list(filter(None, res.stdout.split('\n')))[-1].split('v')[-1]
print('Generating CHANGELOG for', latest_release)

# Read in the CHANGELOG file first
with open('CHANGELOG.md') as f:
    # Read the text in as a list of lines
    old_text = f.readlines()
    # Get the latest release (top of the CHANGELOG)
    for line in old_text:
        match = RELEASE_MD_PATTERN.match(line)
        if match:
            prev_release = match[1]
            break

if latest_release == prev_release:
    print(
        'The latest git tag matches the last release in the CHANGELOG. '
        'Please tag the repository before running this script.'
    )
    sys.exit(1)

# Use git log to list all commits between that tag and HEAD
command = 'git log --oneline v{}..@'.format(prev_release).split(' ')
res = subprocess.run(command, capture_output=True, text=True)
if res.returncode != 0:
    print('Error occurred when running git log command:', str(res.stderr))
    sys.exit(1)

# Parse the output from the above command to find all commits for merged PRs
for line in res.stdout.split('\n'):
    match = MERGED_PR_PATTERN.match(line)
    if match:
        print(match[1], match[2])
