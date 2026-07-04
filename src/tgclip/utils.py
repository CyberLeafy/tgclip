from tgclip.ui import console
import os


def console_input_func():
    return console.input("[bold green]➤ [/bold green]").strip()


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def multiline_input(name: str):
    lines = []
    while True:
        line = input()

        if line.lower() == "/exit":
            console.print(f"\nGoodbye 👋 {name}!")
            return "exit"

        if line.lower() == "/clear":
            clear_screen()
            console.print("[bold green]TGCLIP Shell[/bold green]")
            console.print("Type '/exit' to quit.")
            console.print("Type '/clear' to clear screen.\n")
            console.print("➤ (Enter empty line to send)")
            continue

        if line.startswith("/"):
            console.print("[red]Invalid command[/red]")
            continue

        if line == "":
            break
        lines.append(line)

    return "\n".join(lines)
