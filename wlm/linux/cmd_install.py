from wlm.wlm_cli import cli
import click


class Context:
    def __init__(self, location):
        self.location = location


@click.group()
@click.option('-a', '--all', type=str, help='all helper')
@click.pass_context
def cli(ctx, all):
    '''install any linux package from wlm.'''
    print(ctx.obj.location)


@cli.command()
@click.pass_context
def now(ctx):
    pass
