#!/usr/bin/python
"""
Small python script that, when run, will update the CHANGELOG with information
about all merged pull requests since the previous release.

This script must be run after tagging the latest version
It checks the log of commits since the previous tag and parses it
"""
import re
import subprocess
import sys
from datetime import datetime

# Regex patterns
RELEASE_MD_PATTERN = re.compile(r'## \[(\d+\.\d+\.\d+)\]')
MERGED_PR_PATTERN = re.compile(
    r'([0-9a-f]{7}) Merge pull request #(\d+) from (.+)/.+'
)
TAG_PATTERN = re.compile(
    r'refs/tags/v(\d+\.\d+\.\d+) (\w{3} \w{3} \d{1,2} \d{2}:\d{2}:\d{2} \d{4})'
)

# PR Type terms
FIX_TERMS = ['fix', 'change', 'update']


# Helper functions
def generate_pr_link(pr_num):
    """
    Returns a markdown link to a PR in this repo given its number
    """
    return (
        '[PR #{0}](https://github.com/sendgrid/smtpapi-python/pulls/{0})'
    ).format(pr_num)


def generate_user_link(user):
    """
    Returns a markdown link to a user
    """
    return '[@{0}](https://github.com/{0})'.format(user)


# Get latest tag
command = ['git', 'tag', '--format=%(refname) %(creatordate)']
res = subprocess.run(command, capture_output=True, text=True)
if res.returncode != 0:
    print('Error occurred when running git tag command:', str(res.stderr))
    sys.exit(1)
# Get the last line and get the tag number
latest_release_match = TAG_PATTERN.match(
    list(filter(None, res.stdout.split('\n')))[-1],
)
latest_release = latest_release_match[1]
latest_release_date = datetime.strptime(
    latest_release_match[2], '%a %b %d %H:%M:%S %Y',
)
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
merge_commits = []
for line in res.stdout.split('\n'):
    match = MERGED_PR_PATTERN.match(line)
    if match:
        merge_commits.append(match)

# Determine the type of PR from the commit message
added, fixes = [], []
for commit in merge_commits:
    # Get the hash of the commit and get the message of it
    commit_sha = commit[1]
    command = 'git show {} --format=format:%B'.format(commit_sha).split(' ')
    res = subprocess.run(command, capture_output=True, text=True)
    out = res.stdout.lower()
    is_added = True

    # When storing we need the PR title, number and user
    data = {
        # 3rd line of the commit message is the PR title
        'title': out.split('\n')[2],
        'number': commit[2],
        'user': commit[3],
    }

    for term in FIX_TERMS:
        if term in out:
            fixes.append(data)
            is_added = False
            break
    if is_added:
        added.append(data)

# Now we need to write out the CHANGELOG again
with open('CHANGELOG.md', 'w') as f:
    # Write out the header lines first
    for i in range(0, 3):
        f.write(old_text[i])

    # Create and write out the new version information
    latest_release_date_string = latest_release_date.strftime('%Y-%m-%d')
    f.write('## [{}] - {} ##\n'.format(
        latest_release,
        latest_release_date_string,
    ))
    # Add the stuff that was added
    f.write('### Added\n')
    for commit in added:
        f.write('- {}: {}{} (via {})\n'.format(
            generate_pr_link(commit['number']),
            commit['title'],
            '.' if commit['title'][-1] != '.' else '',
            generate_user_link(commit['user'])
        ))
    f.write('\n')
    # Add the fixes
    f.write('### Fixes\n')
    for commit in fixes:
        f.write('- {}: {}{} (via {})\n'.format(
            generate_pr_link(commit['number']),
            commit['title'],
            '.' if commit['title'][-1] != '.' else '',
            generate_user_link(commit['user'])
        ))
    f.write('\n')

    # Add the old stuff
    for i in range(3, len(old_text)):
        f.write(old_text[i])
