import click
from hello_claude.api import call_claude, stream_claude

MODELS = {
    "haiku": "claude-haiku-4-5-20251001",
    "sonnet": "claude-sonnet-4-6",
    "opus": "claude-opus-4-8"
}

@click.command()
@click.option("--prompt", required=True, help="The prompt to send to claude")
@click.option("--model", type=click.Choice(["haiku", "sonnet", "opus"]), default ="sonnet", help="...")
@click.option("--stream/--no-stream", default=True, help="Stream the response as it arrives.")
@click.option("--system", default="", help="A custom system prompt to shape Claude's behavior")
@click.option("--show-cost", is_flag=True, default=False, help="Display the cost of running an inference")
def main(prompt, model, stream, system, show_cost): 
    """Send a prompt to Claude and print the response."""
    if stream: 
        for text in stream_claude(prompt, model=MODELS[model], system=system):
            click.echo(text, nl=False)
        click.echo()
    else: 
        response, cost=call_claude(prompt, model=MODELS[model], system=system)
        click.echo(response)
        if show_cost:
            click.echo(f"\n[cost: ${cost:.6f}]")


if __name__ == "__main__":
    main()