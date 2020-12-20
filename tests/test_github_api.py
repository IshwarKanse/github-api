import github_api

def test_repo_name():
    result = github_api.repo_name()
    assert type(result) is list
    assert "ansible" in result

def test_top_content():
    result = github_api.top_content()
    assert type(result) is list

def test_create_issue():
    result = github_api.create_issue()
    assert result == None

def test_pull_request():
    result = github_api.pull_request()
