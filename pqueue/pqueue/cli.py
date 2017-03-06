import click
import sqlite3
conn = sqlite3.connect('queue.db')
c = conn.cursor()

@click.command()
@click.argument('command', default='world', required=False)
@click.option('-m', required=False, prompt='Your name', help='The message to push.')

@click.command()
@click.argument('w', default='world', required=False)
@click.option('-c', required=False, prompt='wit', help='www message to push.')

def main(command, m):
    """A command line priority queue for organizing your life!"""
    click.echo('{0}, {1}.'.format(command, m))

if __name__ == '__main__':
    main()
