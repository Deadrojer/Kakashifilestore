<div align="center">

# 🤖 Telegram File Sequence Bot

<img src="https://img.shields.io/badge/Telegram-Bot-blue?style=for-the-badge&logo=telegram" alt="Telegram Bot">
<img src="https://img.shields.io/badge/Python-3.9+-yellow?style=for-the-badge&logo=python" alt="Python">
<img src="https://img.shields.io/badge/MongoDB-Database-green?style=for-the-badge&logo=mongodb" alt="MongoDB">
<img src="https://img.shields.io/badge/License-MIT-red?style=for-the-badge" alt="License">

### *A powerful Telegram bot for managing file sequencing with force subscription capabilities*

[Features](#-features) • [Installation](#-installation) • [Commands](#-commands) • [Deployment](#-deployment) • [Support](#-support)

</div>

---

## ✨ Features

<table>
<tr>
<td width="50%">

### 📁 File Management
- **Smart Sequencing**: Sort files by Quality, Episode, or Season
- **Batch Rename**: Rename multiple files at once
- **Auto Organization**: Automatic file categorization

</td>
<td width="50%">

### 🔐 Access Control
- **Force Subscription**: Require channel membership
- **Admin System**: Multi-level admin management
- **User Ban System**: Block unwanted users

</td>
</tr>
<tr>
<td width="50%">

### 📊 Database
- **MongoDB Integration**: Persistent data storage
- **User Tracking**: Monitor all bot users
- **Statistics**: Detailed usage analytics

</td>
<td width="50%">

### 📢 Broadcasting
- **Mass Messaging**: Send to all users
- **Admin Notifications**: Real-time alerts
- **Custom Messages**: Personalized content

</td>
</tr>
</table>

---

## 🚀 Installation

### Prerequisites

```bash
Python 3.9+
MongoDB Database
Telegram API Credentials
```

### Quick Start

```bash
# Clone the repository
git clone https://github.com/abhinai2244/SEQUENCE-BOT.git

# Navigate to project directory
cd SEQUENCE-BOT

# Install dependencies
pip install -r requirements.txt

# Run the bot
python bot.py
```

---

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the root directory:

```env
# Telegram Configuration
API_ID=your_api_id
API_HASH=your_api_hash
BOT_TOKEN=your_bot_token
OWNER_ID=your_telegram_user_id

# Database Configuration
DB_URI=mongodb://your_mongodb_uri
DB_NAME=Rex_sequencebott
DATABASE_CHANNEL=your_channel_id

# Customization
FSUB_PIC=https://your_force_sub_image_url
START_PIC=https://your_start_image_url
START_MSG=Welcome to the bot!
ABOUT_MESSAGE=About this bot...
HELP_MESSAGE=Here's how to use the bot...
```

---

## 📝 Commands

### 👤 User Commands

| Command | Description |
|---------|-------------|
| `/start` | Initialize the bot |
| `/help` | Display help information |
| `/about` | Learn about the bot |

### 👑 Admin Commands

| Command | Description |
|---------|-------------|
| `/add_admin <user_id>` | Grant admin privileges |
| `/deladmin <user_id>` | Revoke admin privileges |
| `/admins` | View all administrators |
| `/ban <user_id> [reason]` | Ban a user from the bot |
| `/unban <user_id>` | Remove user ban |
| `/banned` | List all banned users |
| `/broadcast` | Send message to all users |
| `/stats` | View bot statistics |

### 🔒 Force Subscription Commands

| Command | Description |
|---------|-------------|
| `/addchnl <channel_id>` | Add force sub channel |
| `/delchnl <channel_id>` | Remove force sub channel |
| `/listchnl` | List all force sub channels |
| `/fsub_mode` | Toggle force subscription |

---

## 🌐 Deployment

### Deploy on Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

1. Click the deploy button above
2. Fill in the required environment variables
3. Deploy and enjoy!

### Deploy on Railway

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new)

1. Click the deploy button
2. Connect your GitHub repository
3. Set environment variables
4. Deploy automatically

### Deploy on VPS

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Python and pip
sudo apt install python3 python3-pip -y

# Clone and setup
git clone https://github.com/yourusername/telegram-file-sequence-bot.git
cd telegram-file-sequence-bot
pip3 install -r requirements.txt

# Run with screen or tmux
screen -S bot
python3 bot.py
```

---

## 📦 Dependencies

```
pyrogram
pyrofork
pymongo
python-dotenv
tgcrypto
```

---

## 🤝 Contributing

Contributions are always welcome! Here's how you can help:

1. 🍴 Fork the repository
2. 🌿 Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. 💾 Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. 📤 Push to the branch (`git push origin feature/AmazingFeature`)
5. 🔃 Open a Pull Request

---

## 💖 Support

<div align="center">

### Join Our Community

[![Telegram Channel](https://img.shields.io/badge/Telegram-Channel-blue?style=for-the-badge&logo=telegram)](https://t.me/cantarellabots)
[![Telegram Group](https://img.shields.io/badge/Telegram-Group-blue?style=for-the-badge&logo=telegram)](https://t.me/CantarellaBotschat)

### ⭐ Star This Repository

If you found this project helpful, please consider giving it a ⭐!

</div>

---

## 👨‍💻 Developers

<table>
<tr>
<td align="center">
<a href="https://t.me/V_Sbotmaker">
<img src="https://via.placeholder.com/100" width="100px;" alt=""/><br>
<sub><b>@V_Sbotmaker</b></sub>
</a><br>
<sub>Lead Developer</sub>
</td>
<td align="center">
<a href="https://t.me/adityaabhinav">
<img src="https://via.placeholder.com/100" width="100px;" alt=""/><br>
<sub><b>@adityaabhinav</b></sub>
</a><br>
<sub>Core Developer</sub>
</td>
<td align="center">
<a href="https://t.me/akaza7902">
<img src="https://via.placeholder.com/100" width="100px;" alt=""/><br>
<sub><b>@akaza7902</b></sub>
</a><br>
<sub>Developer</sub>
</td>
</tr>
</table>

---

## 📜 Credits

- **Creator**: [CantarellaBots](https://t.me/cantarellabots)
- **Original Developer**: [ZANI](https://t.me/about_zani/117)
- **Library**: [Pyrofork](https://github.com/Mayuri-Chan/pyrofork)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">

### Made with ❤️ by the CantarellaBots Team

**© 2024 Telegram File Sequence Bot. All Rights Reserved.**

[⬆ Back to Top](#-telegram-file-sequence-bot)

</div>
