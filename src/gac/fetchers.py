"""
This module contains all the fetch functions we need to get the information
from the GitHub API
"""
import sys
import click
import github



def fetch_repo_users(config, github_session, repo_name: str):
    """
    Gets a list of all the users for a repo, each user should be of type:
    'github.NamedUser.NamedUser'
    """
    try:
        if config.verbose == 3:
            click.echo (f"Attempting to fetch: {repo_name}")
        repo = github_session.get_repo(repo_name)
    except github.UnknownObjectException:
        click.echo(f"Repo: {repo_name}, not found. Exiting..")
        sys.exit(1)
    # Get all the users with access to the repo
    user_dict = {}
    users = repo.get_collaborators()
    for i in users:
        name = i.name
        if not name:
            name = i.login
        user_dict[name] = i
    return user_dict

def fetch_repo_access(config, repo_name: str): # pylint: disable=inconsistent-return-statements
    """
    Gets access information from a given repo
    """
    if config.verbose == 3:
        click.echo("DEBUG: In fetch_repo_access func")
        return f"Hello World, Reponame = {repo_name}"
