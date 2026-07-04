import json
from typing import Any
from pathlib import Path
from platformdirs import user_config_dir

from tgclip.utils import console_input_func
from tgclip.ui import console

CONFIG_DIR = Path(user_config_dir("tgclip", ""))
CONFIG_DIR.mkdir(parents=True, exist_ok=True)
CONFIG_FILE = CONFIG_DIR / "config.json"


def clear_config():
    if CONFIG_FILE.exists():
        CONFIG_FILE.unlink()
    console.print("[green]Clear config successfully.[/]")


def load_config() -> dict[str, Any] | None:
    if CONFIG_FILE.exists():
        with CONFIG_FILE.open("r", encoding="utf-8") as f:
            return json.load(f)
    return None


def save_config(bot_token: str, chat_id: int, name: str | None):
    with CONFIG_FILE.open("w", encoding="utf-8") as f:
        config = {"bot_token": bot_token, "chat_id": chat_id}

        if name is not None:
            config["name"] = name

        json.dump(config, f, indent=4)


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
