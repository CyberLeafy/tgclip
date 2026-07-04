from time import sleep
import time
import os
import sys
import pyperclip
import typer

from tgclip.clipboard import get_text
from tgclip.ui import console, show_config, welcome_screen
from tgclip.config import (
    clear_config,
    is_config_complete,
    load_config,
    save_config,
    setup_name,
)
from tgclip.telegram import get_user_chat_id, send_message, validate_token
from tgclip.utils import console_input_func, multiline_input

app = typer.Typer(
    add_completion=False, help="Send clipboard content to Telegram instantly."
)


@app.command(help="Configur tgclip with your Telegram bot and chat ID.")
def init():
    with console.status(
        "[bold cyan]Initializing TGClip Engine...[/]", spinner="dots12"
    ):
        time.sleep(3)

    token_attempt = 1
    config = load_config()

    if not config:
        user_name = setup_name()

        while True:
            console.print("[cyan]Enter BOT TOKEN:[/]")
            bot_token = console_input_func()

            sys.stdout.write("\033[F")  # Cursor one line upar
            sys.stdout.write("\033[2K")  # clear those line
            sys.stdout.flush()
            with console.status("[cyan]Verifying Token....[/cyan]", spinner="dots"):
                is_valid = validate_token(bot_token)

            if is_valid:
                console.print("[bold green]✓ Token verify successfully[/bold green]\n")
                break

            if token_attempt == 4:
                console.print(
                    "[bold red]Error: Reach max attempt. Try again[/bold red]"
                )
                return

            console.print("[red]Error: Invalid Bot Token[/red]")
            token_attempt += 1

        while True:
            chat_id = get_user_chat_id(bot_token)

            if chat_id:
                save_config(bot_token, chat_id, user_name)
                break

            console.print("[bold red]Note:[/bold red]")
            sleep(0.2)
            console.print("[red]Open your Telegram bot.[/red]")
            sleep(0.2)
            console.print("[cyan]Send [blue]/start[/blue].[/cyan]")
            sleep(0.2)
            console.input("[green]Press Enter after sending /start...[/green]\n")

        console.print("[bold green]✓ Configuration saved successfully[/bold green]\n")
        return

    is_config = is_config_complete(config)

    if is_config:
        console.print("[bold yellow]All ready setup.[/bold yellow]\n")


@app.command(help="Send clipboard text content to Telegram.")
def send():
    config = load_config()

    is_config = is_config_complete(config)
    if config is None or is_config is False:
        return

    text = get_text()

    if not text.strip():
        console.print("Clipboard is empty.")
        return

    response = send_message(config, text)

    if response is None:
        return

    if not response.ok:
        return

    message_id = response.json()["result"]["message_id"]


@app.command(help="Monitor the clipboard and automatically send new content.")
def watch():
    config = load_config()

    is_config = is_config_complete(config)
    if config is None or is_config is False:
        return

    last_text = None

    try:
        while True:
            text = get_text()

            if not text.strip():
                time.sleep(0.5)
                continue

            if text == last_text:
                time.sleep(0.5)
                continue

            response = send_message(config, text)

            last_text = text
            time.sleep(0.5)

            if response is None:
                return

            message_id = response.json()["result"]["message_id"]

    except KeyboardInterrupt:
        console.print("\n[yellow]Stopped watching.[/yellow]")


@app.command(help="Start an intractive shell to send multiple messages.")
def shell():
    config = load_config()

    is_config = is_config_complete(config)
    if config is None or is_config is False:
        return

    os.system("cls" if os.name == "nt" else "clear")  # clear terminal

    console.print("[bold green]TGCLIP Shell[/bold green]")
    console.print("Type '/exit' to quit.")
    console.print("Type '/clear' to clear screen.\n")

    while True:
        try:
            console.print("➤ (Enter empty line to send)")

            texts = multiline_input(config.get("name", "Friend"))
            if texts == "exit":
                return

            if not texts:
                continue

            response = send_message(config, texts)

            if response is None:
                return

            message_id = response.json()["result"]["message_id"]

        except KeyboardInterrupt:
            break


@app.command(help="Display the current tgclip configuration.")
def config():
    config = load_config()

    is_config = is_config_complete(config)
    if config is None or is_config is False:
        return

    show_config(config)


@app.command(help="Remove the current configuration.")
def reset():
    config = load_config()

    is_config = is_config_complete(config)
    if config is None or is_config is False:
        return

    clear_config()


@app.command(help="Check your setup and diagnose configuration or connection issues.")
def doctor():
    config = load_config()

    with console.status("[cyan]Cheking config...[/cyan]", spinner="arc"):
        sleep(0.3)
        is_config = is_config_complete(config)
    if config is None or is_config is False:
        return

    bot_token = config.get("bot_token")
    config_chat_id = config.get("chat_id")
    assert bot_token is not None

    console.print("[green]✔ Config found[/green]")
    sleep(0.3)

    with console.status("[cyan]Cheking token...[/cyan]", spinner="arc"):
        isvalid = validate_token(bot_token)

    if isvalid:
        console.print("[green]✔ Token valid[/red]")
        sleep(0.3)

    with console.status("[cyan]Cheking chat ID...[/cyan]", spinner="arc"):
        new_chat_id = get_user_chat_id(bot_token)

    if new_chat_id is not None:
        if config_chat_id == new_chat_id:
            console.print("[green]✔ Chat ID valid[/green]")
        else:
            console.print("[red]✘Chat ID not valid[/red]")
    sleep(0.2)

    try:
        with console.status("[cyan]Cheking clipboard...[/cyan]", spinner="arc"):
            sleep(0.3)
            pyperclip.paste()

        console.print("[green]✔ Clipboard working[/green]")
    except Exception:
        console.print("[red]✘ Clipboard not accessible[/red]")


@app.callback(invoke_without_command=True)
def callback(ctx: typer.Context):
    if ctx.invoked_subcommand is None:
        welcome_screen()
        raise typer.Exit()


def main():
    app()


if __name__ == "__main__":
    main()
