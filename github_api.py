import os
from github import Github

GITHUB_TOKEN = os.environ['GITHUB_TOKEN']
g = Github(GITHUB_TOKEN)

for repo in g.get_user().get_repos():
    print(repo.name)

def top_content():
    repo = g.get_repo("IshwarKanse/testrole")
    contents = repo.get_top_paths()
    print(contents)

def create_issue():
    repo = g.get_repo("IshwarKanse/testrole")
    repo.create_issue(title="This issue was created using PyGithub", body="This is the issue body")

def pull_request():
    repo = g.get_repo("IshwarKanse/testrole")
    body = '''
    SUMMARY
    Change debug in the role's tasks/main.yml
    '''
    pr = repo.create_pull(title="fix debug message", body=body, head="dev", base="master")


top_content()
create_issue()
pull_request()
