<div align="center">

# 🛡️ ModerationPlus Bot

**A modern, feature-rich Discord moderation bot showcasing advanced UI components and slash commands**

[![Discord.py](https://img.shields.io/badge/discord.py-2.0+-blue.svg)](https://github.com/Rapptz/discord.py)
[![Python](https://img.shields.io/badge/python-3.9+-brightgreen.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-orange.svg)](LICENSE)
[![Open Source](https://img.shields.io/badge/open--source-yes-success.svg)](#)

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Documentation](#-documentation) • [Contributing](#-contributing)

</div>

---

## 📋 Overview

**ModerationPlus** is a production-ready Discord moderation bot that demonstrates modern best practices in bot development. Built with discord.py's ComponentsV2, it showcases how to create rich, interactive moderation interfaces with slash commands, persistent case management, and advanced UI components.

Perfect for communities seeking powerful moderation tools and developers wanting to learn cutting-edge Discord API implementation patterns.

---

## ✨ Key Highlights

### 🎯 Purpose
- **Production Ready** - Deploy-ready moderation solution for Discord servers
- **Educational** - Learn how to leverage ComponentsV2 for rich UI experiences
- **Open Source** - Study and contribute to real-world Discord bot development
- **Community Focused** - Built with transparency and collaboration in mind

### 🚀 Why Choose ModerationPlus?

| Feature | Benefit |
|---------|---------|
| **Modern UI Components** | Rich, interactive case displays with images and actions |
| **Slash Commands** | Intuitive, slash-based moderation interface |
| **Persistent Storage** | JSON-based case management for full audit trails |
| **Image Support** | Attach proof (screenshots, evidence) directly to cases |
| **Error Handling** | Robust permission checks and error recovery |
| **Developer Friendly** | Well-documented, modular codebase for learning |

---

## 🎮 Features

### 📊 Moderation Commands
| Command | Description | Usage |
|---------|-------------|-------|
| `/timeout` | Timeout a user (duration support) | `/timeout @user 5m "spam"` |
| `/kick` | Remove user from server | `/kick @user "violated rules"` |
| `/ban` | Permanently ban user | `/ban @user "repeated violations"` |
| `/mute` | Mute user with role | `/mute @user "off-topic"` |
| `/unmute` | Remove mute role | `/unmute @user` |
| `/warn` | Issue warning with DM | `/warn @user "warning reason"` |
| `/unban` | Unban by user ID | `/unban 123456789` |
| `/report` | Submit moderation report | `/report @user "reason"` |
| `/case` | View specific case details | `/case 1` |

### 🎨 Advanced UI System
- **CaseContainer** - Beautiful, interactive case display with:
  - Unique case IDs
  - Moderator & target information
  - Detailed reason and timestamps
  - Image evidence gallery (up to 4 images)
  - Action buttons (Update, Revoke, History, Export, Share, Appeal)

- **MediaGallery** - Professional image display for evidence attachments
- **Interactive Components** - Buttons, dropdowns, and text displays
- **Real-time Updates** - Dynamic case information and status changes

### 💾 Data Persistence
- **JSON Database** - Cases automatically stored and retrievable
- **Case History** - Complete audit trail for transparency
- **Image Storage** - Links to uploaded evidence preserved
- **Backup Ready** - Easy export and recovery

### 🔒 Security Features
- **Permission Validation** - Only authorized users can execute commands
- **Role Hierarchy** - Respects Discord's role structure
- **API Error Handling** - Graceful failure recovery
- **Input Validation** - Robust checks on all user inputs

---

## 📁 Project Structure

```
ModerationPlus-Bot/
│
├── 📂 cogs/                    # Moderation command handlers
│   ├── timeout.py             # Timeout command with duration
│   ├── kick.py                # Kick command
│   ├── ban.py                 # Ban command
│   ├── warn.py                # Warn command with DM notification
│   ├── report.py              # Report system
│   ├── mute.py                # Mute command with role
│   ├── unban.py               # Unban by user ID
│   ├── unmute.py              # Unmute command
│   └── case.py                # Case retrieval
│
├── 📂 utils/                   # Utility modules
│   ├── __init__.py            # Package initialization
│   ├── db.py                  # JSON database handler
│   └── case.py                # CaseContainer UI component
│
├── index.py                    # Main bot entry point
├── cases.json                  # Case storage (auto-generated)
├── .env                        # Environment configuration
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

---

## 🚀 Installation

### Prerequisites
- **Python** 3.9 or higher
- **discord.py** 2.0+ with ComponentsV2
- **Git** for cloning

### Step-by-Step Setup

#### 1️⃣ Clone Repository
```bash
git clone https://github.com/kuwshyDEV/ModerationPlus-Bot.git
cd ModerationPlus-Bot
```

#### 2️⃣ Create Virtual Environment (Recommended)
```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

#### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

#### 4️⃣ Configure Environment
Create a `.env` file in the root directory:
```env
DISCORD_TOKEN=your_bot_token_here
MOD_LOG_CHANNEL_ID=your_channel_id_here
MUTED_ROLE_ID=your_muted_role_id_here
```

**How to find these IDs:**
- **Bot Token**: [Discord Developer Portal](https://discord.com/developers/applications)
- **Channel ID**: Right-click channel → Copy Channel ID (enable Developer Mode)
- **Role ID**: Right-click role → Copy Role ID (enable Developer Mode)

#### 5️⃣ Server Setup
1. Create a **"Muted"** role in your server
2. Remove "Send Messages" and "Speak" permissions from the role
3. Add the bot to your server with these permissions:
   - Send Messages
   - Read Message History
   - Manage Messages
   - Manage Members
   - Ban Members

#### 6️⃣ Run the Bot
```bash
python index.py
```

✅ **Bot is now online!** You should see confirmation in your console.

---

## 💻 Usage Guide

### Basic Command Syntax
All commands use Discord's modern slash command format for an intuitive user experience.

### Moderation Examples

**Timeout a user (mute temporarily)**
```
/timeout @SpamUser 5m reason: "Spam in general chat"
```
→ Bot displays a professional case card with images and metadata

**Permanently ban a user with evidence**
```
/ban @ToxicUser reason: "Harassment" image1: [screenshot.png]
```
→ Case stored in database with attached evidence

**Issue a warning**
```
/warn @WarningUser reason: "First warning - be respectful"
```
→ User receives DM notification + case logged

**View case history**
```
/case 42
```
→ Displays full case details including all images and metadata

### Action Buttons
Each case displays interactive buttons:
- 🔄 **Update** - Modify case details
- ❌ **Revoke** - Remove moderation action
- 📜 **History** - View complete action history
- 📥 **Export** - Download case as JSON/PDF
- 🔗 **Share** - Share case summary
- 🗣️ **Appeal** - Let user appeal decision

---

## 🔧 Configuration

### Environment Variables
```env
# Required
DISCORD_TOKEN=your_token                 # Bot token from Developer Portal

# Optional but Recommended
MOD_LOG_CHANNEL_ID=channel_id            # Where mod actions are logged
MUTED_ROLE_ID=role_id                    # Role used for muting
PREFIX=!                                  # Command prefix (slash commands primary)
```

### Customizing Mod Log Channel
Edit the channel ID in `/cogs/report.py`:
```python
MOD_LOG_CHANNEL_ID = 1234567890123456789
```

### Case Database
Cases are automatically stored in `cases.json`. Structure:
```json
{
  "case_1": {
    "moderator_id": "123456789",
    "target_id": "987654321",
    "type": "timeout",
    "reason": "Spam",
    "images": ["https://..."],
    "timestamp": "2024-01-15T10:30:00Z"
  }
}
```

---

## 📚 Documentation

### Command Reference

#### Timeout
```
/timeout @user <duration> [reason] [images]
```
- Temporarily mutes a user
- Duration: 5m, 1h, 1d, etc.
- Supports image evidence

#### Kick
```
/kick @user [reason] [images]
```
- Removes user from server (can rejoin)
- Supports detailed reasons and proof

#### Ban
```
/ban @user [reason] [images]
```
- Permanently bans user
- Prevents rejoin without unban

#### Mute
```
/mute @user [reason]
```
- Applies muted role
- Removes send message permissions

#### Warn
```
/warn @user <reason> [images]
```
- Issues warning without action
- User receives DM notification
- Case logged for future reference

#### Case
```
/case <case_id>
```
- Retrieves and displays case details
- Shows all metadata and images

---

## 🏗️ Architecture

### Component System

**CaseContainer**
```python
# Displays case information beautifully
- Case ID
- Moderator & Target
- Action Type
- Reason
- Timestamps
- Image Gallery
```

**MediaGallery**
```python
# Professional image display
- Up to 4 images per case
- Responsive layout
- Click to view full size
```

**Action Row**
```python
# Interactive buttons
- One-click actions
- Status-based enabling/disabling
- Real-time feedback
```

### Database Design
```python
# cases.json structure
{
  "case_id": {
    "moderator": User,
    "target": User,
    "type": ModAction,
    "reason": str,
    "images": [URL],
    "timestamp": ISO8601
  }
}
```

---

## 🎓 Learning Objectives

This project teaches:

### 1. **ComponentsV2 UI System**
- Using `ui.Container` for structured layouts
- `ui.MediaGallery` for image displays
- `ui.TextDisplay` for formatted text
- `ui.ActionRow` for button grouping
- `ui.LayoutView` for complex layouts

### 2. **Slash Commands**
- Parameter handling (users, roles, strings)
- Optional vs. required parameters
- Command groups and subcommands
- Permission checks

### 3. **Database Management**
- JSON file handling
- CRUD operations (Create, Read, Update, Delete)
- Data persistence between restarts
- Query optimization

### 4. **Error Handling**
- Permission validation
- User input validation
- API error recovery
- Graceful failure messages

### 5. **File & Image Management**
- Processing attachments
- Storing file URLs
- Building image galleries
- Handling upload errors

---

## 🤝 Contributing

We welcome contributions! Whether you're fixing bugs, adding features, or improving documentation.

### How to Contribute

1. **Fork the Repository**
   ```bash
   # Click 'Fork' on GitHub
   ```

2. **Create a Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make Your Changes**
   - Follow the existing code style
   - Keep functions focused and well-documented
   - Add comments for complex logic

4. **Test Your Changes**
   - Test locally with your Discord server
   - Verify error handling
   - Check UI rendering

5. **Commit & Push**
   ```bash
   git commit -m "Add: description of changes"
   git push origin feature/your-feature-name
   ```

6. **Open a Pull Request**
   - Clear description of changes
   - Link any related issues
   - Await review

### Contribution Guidelines
- ✅ Keep code readable and well-commented
- ✅ Test thoroughly before submitting
- ✅ Follow the existing code style
- ✅ Update documentation if needed
- ✅ One feature per pull request

### Areas for Contribution
- 🐛 Bug fixes and error handling
- ✨ New moderation commands
- 🎨 UI/UX improvements
- 📚 Documentation enhancements
- ⚡ Performance optimizations
- 🔒 Security improvements

---

## 🐛 Troubleshooting

### Bot Won't Start
**Problem:** `Token is invalid` or bot won't connect
- ✅ Verify `DISCORD_TOKEN` in `.env` is correct
- ✅ Ensure bot token, not user token
- ✅ Regenerate token in Developer Portal if needed

### Commands Not Appearing
**Problem:** Slash commands don't show in Discord
- ✅ Run `/sync` if available
- ✅ Wait 1-2 minutes for Discord to update
- ✅ Verify bot has "Use Application Commands" permission
- ✅ Check bot is in your server

### Mute Command Fails
**Problem:** Mute command gives error
- ✅ Create "Muted" role in server
- ✅ Verify bot role is above muted role
- ✅ Set `MUTED_ROLE_ID` in `.env`

### Images Not Displaying
**Problem:** Case shows but images don't load
- ✅ Ensure images were successfully attached
- ✅ Check URLs in `cases.json` are valid
- ✅ Verify bot can access image URLs

### Permission Denied Errors
**Problem:** Commands say "permission denied"
- ✅ Verify bot has admin or necessary permissions
- ✅ Check bot role hierarchy (should be above members)
- ✅ Ensure user running command has mod permissions

---

## 📊 Roadmap

Future enhancements planned:

- [ ] Appeal system with voting
- [ ] Advanced case filtering and search
- [ ] Case statistics dashboard
- [ ] Custom moderation workflows
- [ ] Integration with external logging services
- [ ] Automated enforcement based on rules
- [ ] Multi-mod assignment system
- [ ] Case templates for consistency

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

You are free to:
- ✅ Use for personal and commercial projects
- ✅ Modify the source code
- ✅ Distribute and share
- ✅ Use privately or publicly

Just include the license notice!

---

## 💬 Support & Community

### Getting Help
- 📖 Check the [Documentation](#documentation) section
- 🐛 Search [existing issues](https://github.com/kuwshyDEV/ModerationPlus-Bot/issues)
- 💡 Create a new issue with details

### Report a Bug
Please include:
- What you were trying to do
- Error message or unexpected behavior
- Python and discord.py version
- Steps to reproduce

### Feature Requests
- Describe the desired feature
- Explain the use case
- Suggest implementation approach

---

## 🔗 Resources

### Official Documentation
- [Discord.py Docs](https://discordpy.readthedocs.io/) - Python Discord API wrapper
- [Discord Developer Portal](https://discord.com/developers/applications) - Bot management
- [Discord API Docs](https://discord.com/developers/docs) - API reference

### Related Projects
- [discord.py GitHub](https://github.com/Rapptz/discord.py) - Main library
- [Discord Py Interactions](https://interactions-py.readthedocs.io/) - Alternative library

### Learning Resources
- [Python Docs](https://docs.python.org/3/) - Python language reference
- [Async Programming](https://realpython.com/async-io-python/) - Async/await tutorial

---

## 👤 Credits

**Created with ❤️ by Kuwshy**

### Special Thanks
- discord.py community for excellent library
- Discord for the ComponentsV2 API
- All contributors and bug reporters

---

<div align="center">

### 🌟 Show Your Support

If this project helped you, please consider:
- ⭐ Giving it a star on GitHub
- 🔗 Sharing with friends
- 💬 Providing feedback
- 🤝 Contributing improvements

**Made with ❤️ for Discord Communities**

[⬆ Back to Top](#-moderationplus-bot)

</div>
