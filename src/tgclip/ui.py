from rich.align import Align
from rich.table import Table
from rich.console import Console
from rich.panel import Panel
from rich import box
from time import sleep

from rich.text import Text

console = Console()


# show config
def show_config(config):
    table = Table(
        box=box.SIMPLE,
        show_header=False,
        pad_edge=False,
        expand=True,
    )

    table.add_column("Key", style="bold cyan", justify="left")
    table.add_column("Value", style="white")

    table.add_row("Name", config.get("name", "[dim]not set[/dim]"))
    table.add_row("Chat ID", str(config.get("chat_id", "[dim]not set[/dim]")))
    table.add_row("Auto Delete", config.get("auto_delete", "disabled"))
    table.add_row("Delete After", config.get("delete_after", "30s"))
    table.add_row("Version", config.get("version", "0.1.0"))

    panel = Panel(
        table,
        title="⚙ TGClip System Config",
        title_align="center",
        border_style="bright_blue",
        box=box.ROUNDED,
        padding=(1, 2),
        expand=False,
    )

    console.print(panel)


# Welcome Screen
def welcome_screen():
    with console.status(
        "[bold bright_cyan]⚡ Initializing TGClip...[/bold bright_cyan]",
        spinner="aesthetic",
    ):
        sleep(1.5)
    header = Text("TGClip", style="bold bright_magenta")

    body = (
        "[bold white]Welcome to[/bold white] [bold bright_red]TGClip[/bold bright_red] CLI Tool 🌻\n\n"
        "[bold white]Telegram Clipboard CLI[/bold white]\n"
        "[dim]Fast • Minimal • Smart Automation Tool[/dim]\n\n"
        "[cyan]➤ Version:[/cyan] [green]1.0.0[/green]\n"
        "[cyan]➤ Status:[/cyan] [green]Ready[/green]\n"
        "[cyan]➤ Mode:[/cyan] [magenta]Interactive Shell[/magenta]\n\n"
        "[dim]Commands:[/dim]\n"
        "[yellow]--help[/yellow]  Show all available commands\n\n"
        "[dim]Tip:[/dim]\n"
        "Run [green]tgclip --help[/green] to start using TGClip\n\n"
        "[dim]------------------------------------------------[/dim]\n"
        "[dim]Devloped by CyberLeafy 🕊️[/dim]\n"
        "[dim]Version 0.1.0 [/dim]"
    )

    panel = Panel(
        Align.center(body),
        title=header,
        title_align="center",
        border_style="magenta",
        box=box.ROUNDED,
        padding=(1, 4),
        expand=False,
    )

    console.print(panel)
