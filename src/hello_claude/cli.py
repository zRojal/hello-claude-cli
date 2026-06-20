import click
from hello_claude.api import call_claude

@click.command()
@click.option("--prompt", required=True, help="The prompt to send to claude")
def main(prompt): 
    """Send a prompt to Claude and print the response."""
    response = call_claude(prompt)
    click.echo(response)

if __name__ == "__main__":
    main()