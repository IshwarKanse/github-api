import os
from github import Github
from github import GithubException

GITHUB_TOKEN = os.environ['GITHUB_TOKEN']
g = Github(GITHUB_TOKEN)

def repo_name():
    myrepos = []
    for repo in g.get_user().get_repos():
        myrepos.append(repo.name)
    print(myrepos)

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
    try:
        pr = repo.create_pull(title="fix debug message", body=body, head="dev", base="master")
    except GithubException:
        print("You already created that pull request")

repo_name()
top_content()
create_issue()
pull_request()
