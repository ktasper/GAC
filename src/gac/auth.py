"""
This module deals with auth
"""
from github import Github
import click


def github_auth(config, auth_token) -> Github:
    """
    Creates a Github object that we can use in other functions
    """
    if config.verbose == 3:
        click.echo(f"INFO: auth_token -> {auth_token}")
    github_session = Github(auth_token)
    return github_session
