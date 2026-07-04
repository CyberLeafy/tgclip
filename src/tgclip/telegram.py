import requests
import time

from tgclip.ui import console
from typing import Any


def telegram_request(
    method: str, url: str, payload: dict | None = None
) -> requests.Response | None:
    try:
        if method == "get":
            response = requests.get(url)
            return response
        if method == "post":
            response = requests.post(url=url, data=payload)
            return response

    except requests.exceptions.ConnectionError:
        console.print("[bold red]✘ No internet connection.[/bold red]")
        return None
    except requests.exceptions.Timeout:
        console.print("[bold red]✘ Request time out. Please try again.[/bold red]")
        return None
    except requests.RequestException as e:
        console.print(f"[bold red]✘ Network error: {e} [/bold red]")
        return None


def send_message(config: dict[str, Any], text) -> requests.Response | None:
    bot_token = config.get("bot_token")
    chat_id = config.get("chat_id")

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

    with console.status("[cyan]Sending...[/cyan]", spinner="dots"):
        response = telegram_request(
            method="post", payload={"chat_id": chat_id, "text": text}, url=url
        )
    time.sleep(0.3)

    if response and response.ok:
        console.print(" " * 30, end="\r")  # clear line
        console.print("[green]✓ Sent[/green]")
    else:
        console.print("[red]✕ Fail[/red]")

    return response


def delete_message_later(config: dict[str, Any], message_id: int, delay=60):
    bot_token = config.get("bot_token")
    chat_id = config.get("chat_id")

    time.sleep(delay)

    url = f"https://api.telegram.org/bot{bot_token}/deleteMessage"

    telegram_request(
        method="post",
        payload={
            "chat_id": chat_id,
            "message_id": message_id,
        },
        url=url,
    )


def get_user_chat_id(bot_token: str):
    url = f"https://api.telegram.org/bot{bot_token}/getUpdates"
    response = telegram_request(method="get", url=url)

    if response and response.ok:
        updates = response.json().get("result", [])
        return updates[-1]["message"]["chat"]["id"] if updates else None

    return None


def validate_token(bot_token: str):
    url = f"https://api.telegram.org/bot{bot_token}/getMe"

    response = telegram_request(method="get", url=url)

    if response and response.ok:
        data = response.json()
        return data.get("ok", False)

    return False
