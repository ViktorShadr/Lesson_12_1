import json
from unittest.mock import patch

from src.get_users import get_user_info, get_user_repos, get_github_users

@patch('requests.get')
def test_get_user_info(mocked_get):
    mocked_get.return_value.status_code = 200
    mocked_get.return_value.json.return_value = {'login': 'test_user', 'public_repos': 10}
    result = get_user_info('test_user')
    assert result == (True, {'login': 'test_user', 'public_repos': 10})

@patch('requests.get')
def test_get_user_info_invalid(mocked_get):
    mocked_get.return_value.json.return_value = {'message': 'Not Found'}
    result = get_user_info('non_existent_user')
    assert result == (False, {})

@patch('requests.get')
def test_get_user_repos(mocked_get):
    mocked_get.return_value.status_code = 200
    mocked_get.return_value.json.return_value = [{'name': 'repo1'}, {'name': 'repo2'}]
    result = get_user_repos('test_user')
    assert result == (True, ['repo1', 'repo2'])

@patch('requests.get')
def test_get_user_repos_invalid(mocked_get):
    mocked_get.return_value.status_code = 404
    mocked_get.return_value.json.return_value = {'message': 'Not Found'}
    result = get_user_repos('non_existent_user')
    assert result == (False, [])

@patch('get_user_info')
@patch('get_user_repos')
def test_get_github_users(mock_get_user_repos, mock_get_user_info):
    mock_get_user_info.return_value = (True, {'login': 'user1', 'public_repos': 2})
    mock_get_user_repos.return_value = (True, ['repo1', 'repo2'])
    expected_result = [{'login': 'user1', 'public_repos': 2, 'repositories': ['repo1', 'repo2']}]
    result = get_github_users(['user1'])
    assert result == json.dumps(expected_result)

@patch('get_user_info')
@patch('get_user_repos')
def test_get_github_users_negative(mock_get_user_repos, mock_get_user_info):
    mock_get_user_info.return_value = (False, {})
    mock_get_user_repos.return_value = (False, [])
    result = get_github_users(['non_existent_user'])
    assert result == None