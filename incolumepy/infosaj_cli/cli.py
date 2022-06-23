import argparse
import click
from pathlib import Path

import toml

from incolumepy.infosaj.infosaj import gen_infosaj, gen_model_conf


#infosaj
@click.group()
@click.option('-c',
              "--configfile",
              prompt="Your file config name",
              default='infosaj/model.yml',
              help="Provide your file YAML config name")
@click.option('-o',
              "--outputfile",
              default='infosaj/index.html',
              prompt="Your file output name",
              help="Provide your file HTML output name")
@click.pass_context
def infosaj(ctx, **kwargs):
    """Generate informativo SAJ."""
    ctx.obj = {}
    ctx.obj.update(**kwargs)


@infosaj.command()
@click.argument('subcommand')
@click.pass_context
def help(ctx, subcommand):
    """Show the help for specific command."""
    subcommand_obj = infosaj.get_command(ctx, subcommand)
    if subcommand_obj is None:
        click.echo("I don't know that command.")
    else:
        click.echo(subcommand_obj.get_help(ctx))


@infosaj.command()
@click.pass_context
def model(ctx):
    """Generate model config file."""
    click.secho(f'{ctx.obj} {ctx.obj.get("configfile")}', fg='green')
    return gen_model_conf(ctx.obj.get("configfile"))


@infosaj.command(name='gen')
@click.pass_context
def generator(ctx):
    """Generate infosaj HTML file."""
    click.secho(f'{ctx.obj} {ctx.obj.get("configfile")}', fg='green')
    return gen_infosaj(ctx.obj.get("outputfile"))
