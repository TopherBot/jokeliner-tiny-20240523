import sys
from pathlib import Path

import click
import httpx
from rich import print as rprint

API_URL = "https://v2.jokeapi.dev/joke/Any?type=single"

@click.command()
@click.option(
    "--no-color",
    is_flag=True,
    help="Print the joke without Rich colour styling.",
)
def main(no_color: bool) -> None:
    """Fetch a random joke and display it.

    The command contacts the public JokeAPI, extracts the `joke`
    field from the JSON payload and prints it.  When `--no-color`
    is omitted the output is wrapped in a green ``[bold]`` block
    using **rich** – otherwise it falls back to plain ``print``.
    """
    try:
        resp = httpx.get(API_URL, timeout=5.0)
        resp.raise_for_status()
        data = resp.json()
        joke = data.get("joke") or "(no joke received)"
    except Exception as exc:  # pragma: no cover – network failures are rare in CI
        click.echo(f"Error fetching joke: {exc}", err=True)
        sys.exit(1)

    if no_color:
        click.echo(joke)
    else:
        rprint(f"[bold green]{joke}[/bold green]")

if __name__ == "__main__":
    # Allows ``python -m jokeliner.cli`` for quick testing.
    main()
