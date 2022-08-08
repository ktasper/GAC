"""
This is the main file of the program, this is where all the CLI options
are defined.
"""
import logging
import click

from gac import auth, data
from . import fetchers

LOGGING_LEVELS = {
    0: logging.NOTSET,
    1: logging.ERROR,
    2: logging.WARN,
    3: logging.INFO,
    4: logging.DEBUG,
}  #: a mapping of `verbose` option counts to logging levels


# Create the config object
class Config(): # pylint: disable=too-few-public-methods
    """
    This is a config object used to store config objects, that we will
    eventually pass down via decorators
    """
    def __init__(self) -> None:
        self.verbose: int = 0
        self.access_token: str = None

# Create the decorator to pass the config object down
pass_config = click.make_pass_decorator(Config, ensure=True)


@click.group()
@click.option("--verbose", "-v", count=True, help="Enable verbose output, (up to -vvvv)")
@click.option('--access-token', "-t", envvar='GAC_ACCESS_TOKEN', required=True,
    help="GitHub Access token, can be set via GAC_ACCESS_TOKEN")
@pass_config
def cli(config, verbose, access_token):
    """Run cli"""
    # Use the verbosity count to determine the logging level...
    if verbose > 0:
        logging.basicConfig(
            level=LOGGING_LEVELS[verbose]
            if verbose in LOGGING_LEVELS
            else logging.DEBUG
        )
        click.echo(
            click.style(
                f"Verbose logging is enabled. "
                f"(LEVEL={logging.getLogger().getEffectiveLevel()})",
                fg="yellow",
            )
        )
    config.verbose = verbose
    config.access_token = access_token

@cli.command()
@click.argument("repo-name")
@click.argument('out', type=click.File('w'), default='-', required=False)
@pass_config
def fetch(config: Config, repo_name: str, out):
    """
    This fetches repo access information on given repos.
    Args:

    repo-name - This is the name of the repo you wish to get access info for

    out - This defaults to STDOUT, if given a file will write the output to
    the given file instead
    """
    if config.verbose == 3:
        click.echo(f"INFO: repo-name -> {repo_name}")
    session = auth.github_auth(config=config,auth_token=config.access_token)
    user_access_dict = fetchers.fetch_repo_users(config=config,
        github_session=session, repo_name=repo_name)

    data.user_dict_to_json(users_dict=user_access_dict)
    click.echo (" ", file=out)
