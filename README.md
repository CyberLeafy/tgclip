<div align="center">

# 📋 TGCLIP

### Instantly send clipboard content or text from your computer to Telegram.

[![PyPI](https://img.shields.io/badge/pip-tgclip-3776AB?logo=pypi&logoColor=white)](https://pypi.org/project/tgclip/)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](#-license)
[![Telegram](https://img.shields.io/badge/Telegram-Bot%20API-26A5E4?logo=telegram&logoColor=white)](https://core.telegram.org/bots)

A lightweight CLI that moves text, code, links, and commands from your desktop straight to Telegram — built for developers, students, and anyone who lives between a laptop and a phone.

</div>

<br>

## Table of Contents

- [Features](#-features)
- [Installation](#-installation)
- [Prerequisites](#-prerequisites)
- [Quick Start](#-quick-start)
- [Commands](#-commands)
- [Workflow](#-workflow)
- [Use Cases](#-use-cases)
- [Privacy](#-privacy)
- [Troubleshooting](#-troubleshooting)
- [Requirements](#-requirements)
- [Contributing](#-contributing)
- [License](#-license)

<br>

## ⚡ Features

<table>
<tr><td width="40">🚀</td><td>Simple one-time setup</td></tr>
<tr><td>📋</td><td>Send clipboard content instantly</td></tr>
<tr><td>✍️</td><td>Send custom text directly from the terminal</td></tr>
<tr><td>👀</td><td>Clipboard watch mode</td></tr>
<tr><td>💻</td><td>Interactive shell mode</td></tr>
<tr><td>⚙️</td><td>Easy configuration management</td></tr>
<tr><td>🩺</td><td>Built-in diagnostics with <code>doctor</code></td></tr>
<tr><td>🔄</td><td>Reset configuration anytime</td></tr>
<tr><td>🎨</td><td>Clean, colorful terminal UI powered by Rich</td></tr>
</table>

<br>

## 📦 Installation

```bash
pip install tgclip
```

Verify it worked:

```bash
tgclip
```

<br>

## ✅ Prerequisites

| Requirement | Details |
|---|---|
| Telegram account | Any personal account |
| Telegram Bot | Created via [@BotFather](https://t.me/BotFather) |


<br>

## 🚀 Quick Start

```bash
tgclip init
```

You'll be prompted for:

```bash
① Your name
② Telegram Bot Token
```

> 💾 Configuration is stored **locally** on your machine — nothing is uploaded anywhere else.

<br>

## 🛠 Commands

<details open>
<summary><b><code>tgclip init</code></b> — Initialize</summary>
<br>

Configure TGCLIP for first-time use.
</details>

<details open>
<summary><b><code>tgclip send</code></b> — Send</summary>
<br>

Send the current clipboard content to Telegram.
</details>

<details open>
<summary><b><code>tgclip watch</code></b> — Watch</summary>
<br>

Continuously monitor the clipboard and auto-send anything newly copied.
Stop with `Ctrl + C`.
</details>

<details open>
<summary><b><code>tgclip shell</code></b> — Shell</summary>
<br>

Launch an interactive shell for sending multiple messages without restarting the command.
Exit with `/exit` or `Ctrl + C`.
</details>

<details open>
<summary><b><code>tgclip config</code></b> — Configuration</summary>
<br>

Display your current configuration.
</details>

<details open>
<summary><b><code>tgclip doctor</code></b> — Doctor</summary>
<br>

Runs a full health check:

- ☑ Configuration
- ☑ Clipboard access
- ☑ Internet connectivity
- ☑ Telegram API access
- ☑ Bot token
- ☑ Chat ID
</details>

<details open>
<summary><b><code>tgclip reset</code></b> — Reset</summary>
<br>

Wipes the current configuration so you can start fresh.
</details>

<br>

## 🔁 Workflow

```mermaid
flowchart LR
    A[📄 Copy text] --> B[tgclip send]
    B --> C[✈️ Telegram]
    C --> D[📱 Open on phone]
```

<br>

## 💡 Use Cases

- 🧩 Send code snippets to your phone
- 🔗 Transfer commands between devices
- 📝 Save temporary notes
- 🌐 Share links instantly
- 📤 Move terminal output
- 🔄 Continue work from mobile

<br>

## 🔒 Privacy

TGCLIP talks **directly** to the Telegram Bot API — nothing else is in the loop.

- ✔ Configuration stays on your local machine
- ✔ No external servers, no telemetry, no middleman

<br>

## 🧰 Troubleshooting

| Problem | Fix |
|---|---|
| Something's not working | `tgclip doctor` |
| Need to start over | `tgclip reset` → `tgclip init` |
| Forgot a command | `tgclip --help` |

<br>

## 📋 Requirements

- Python **3.10+**
- A Telegram Bot
- An internet connection

<br>

## 🤝 Contributing

Bug reports, feature requests, and pull requests are always welcome — open an issue to get started.

<br>

## 📄 License

Released under the **MIT License**.

<br>

---

## 🆘 Support

If you encounter a bug or have a feature suggestion, please open an issue on the GitHub repository.

---

<div align="center">

**Developed by CyberLeafy**

*TGCLIP — Fast. Simple. Clipboard to Telegram.* 📋➡️📱

</div>
