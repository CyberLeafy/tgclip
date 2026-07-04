# TGCLIP

> **Instantly send clipboard content or text from your computer to Telegram.**

TGCLIP is a lightweight command-line tool that helps you quickly transfer text, code snippets, links, commands, or clipboard content from your desktop to Telegram. It's designed for developers, students, and anyone who frequently switches between their computer and phone.

---

## ✨ Features

| | |
|---|---|
| 🚀 | Simple one-time setup |
| 📋 | Send clipboard content instantly |
| ✍️ | Send custom text directly from the terminal |
| 👀 | Clipboard watch mode |
| 💻 | Interactive shell mode |
| ⚙️ | Easy configuration management |
| 🩺 | Built-in diagnostics with `doctor` |
| 🔄 | Reset configuration anytime |
| 🎨 | Clean and colorful terminal interface powered by Rich |

---

## 📦 Installation

Install using pip:

```bash
pip install tgclip
```

Verify the installation:

```bash
tgclip --help
```

---

## ✅ Prerequisites

Before using TGCLIP, you need:

- A Telegram account
- A Telegram Bot created using [@BotFather](https://t.me/BotFather)
- Your bot token

---

## 🚀 Quick Start

Initialize TGCLIP:

```bash
tgclip init
```

Follow the on-screen instructions to configure:

1. Your name
2. Telegram Bot Token

> Configuration is stored locally on your machine.

---

## 🛠️ Commands

### `init` — Initialize
```bash
tgclip init
```
Configure TGCLIP for first-time use.

### `send` — Send
```bash
tgclip send
```
Send the current clipboard content.

### `watch` — Watch
```bash
tgclip watch
```
Continuously monitor the clipboard and automatically send newly copied content.

Stop watching anytime with `Ctrl + C`.

### `shell` — Shell
```bash
tgclip shell
```
Launch an interactive shell for sending multiple messages without restarting the command.

Exit with `/exit` or `Ctrl + C`.

### `config` — Configuration
```bash
tgclip config
```
Display the current configuration.

### `doctor` — Doctor
```bash
tgclip doctor
```
Run a health check for your setup. It verifies:

- Configuration
- Clipboard access
- Internet connectivity
- Telegram API access
- Bot token
- Chat ID

### `reset` — Reset
```bash
tgclip reset
```
Remove the current configuration and start fresh.

---

## 🔁 Typical Workflow

```
Copy text
   │
   ▼
tgclip send
   │
   ▼
Telegram
   │
   ▼
Open on phone
```

---

## 💡 Example Use Cases

- Send code snippets to your phone
- Transfer commands between devices
- Save temporary notes
- Share links instantly
- Move terminal output
- Continue work from mobile

---

## 🔒 Privacy

TGCLIP communicates directly with the **Telegram Bot API**.

- Your configuration remains on your local machine.
- No external servers are used by TGCLIP.

---

## 🧰 Troubleshooting

**Configuration problems**
```bash
tgclip doctor
```

**Reconfigure**
```bash
tgclip reset
tgclip init
```

**Command help**
```bash
tgclip --help
```

---

## 📋 Requirements

- Python 3.10+
- A Telegram Bot
- Internet connection

---

## 📄 License

MIT License

---

## 👤 Author

Developed by **CyberLeafy**

---

## 🤝 Contributing

Bug reports, feature requests, and pull requests are welcome!

---

## 🆘 Support

If you encounter a bug or have a feature suggestion, please open an issue on the GitHub repository.

---

<p align="center"><b>TGCLIP</b> — Fast. Simple. Clipboard to Telegram. 📋➡️📱</p>
