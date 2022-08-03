"""
This module contains all the fetch functions we need to get the information
from the GitHub API
"""
import click

def fetch_repo_access(config, repo_name: str): # pylint: disable=inconsistent-return-statements
    """
    Gets access information from a given repo
    """
    if config.verbose == 4:
        click.echo("DEBUG: In fetch_repo_access func")
        return f"Hello World, Reponame = {repo_name}"
