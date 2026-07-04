import os
import json
from typing import Any

from tgclip.utils import console_input_func
from tgclip.ui import console

CONFIG_FILE = "config.json"
COMMAND_LIST = ["-h", "-e", "-r"]


def clear_config():
    os.remove(CONFIG_FILE)
    console.print("[green]Clear config successfully.[/]")


def load_config() -> dict[str, Any] | None:
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return None


def save_config(bot_token: str, chat_id: int, name: str | None):
    with open(CONFIG_FILE, "w") as f:
        if name is None:
            json.dump({"bot_token": bot_token, "chat_id": chat_id}, f)
        else:
            json.dump({"bot_token": bot_token, "chat_id": chat_id, "name": name}, f)


def setup_name():
    console.print("[bold yellow]⚙ First time setup required[/bold yellow]\n")

    console.print("[cyan]What should I call you? (default: Friend):[/]")
    name = console_input_func()

    if name == "":
        console.print("[red]No worrries! I'll call you 'Friend'.[/red]\n")
        return None

    return name


def is_config_complete(config: dict[str, Any] | None) -> bool:
    if config is None:
        console.print("Please run 'tgclip init' first.")
        return False

    return bool(config.get("bot_token")) and bool(config.get("chat_id"))
