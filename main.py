import click
from assist import tryit


@click.group()
def cli():
    pass


@click.command()
def plan():
    """Plan the next workout"""
    tryit()


@click.command()
def report():
    """Read results of last workout from stdin and update the tracker"""
    pass


@click.command()
@click.option('--name', default='friend', help='The person to greet.')
def greet(name):
    """Simple program that greets NAME."""
    click.echo(f"Hello {name}!")


@click.command()
@click.option('--name', default='friend', help='The person to say goodbye to.')
def goodbye(name):
    """Simple program that says goodbye to NAME."""
    click.echo(f"Goodbye {name}!")


cli.add_command(plan)
cli.add_command(report)

if __name__ == '__main__':
    cli()
