Discord ModerationPlus Bot

**Overview**
This open-source Discord moderation bot, built with discord.py's ComponentsV2 (Bot UI Kit), demonstrates modern slash command moderation tools using the ui.Container and ui.MediaGallery features. It serves as an educational resource for developers learning to implement interactive UI components in Discord bots.

**Why Open-Source?**
- Educational Purpose: Designed to teach developers how to use discord.py's ComponentsV2 branch (feat/components-v2) for creating rich, interactive moderation interfaces.
- Community Learning: Encourages collaboration, code review, and contributions to explore new UI features like ui.LayoutView, ui.TextDisplay, and ui.MediaGallery.
- Transparency: Open code allows learners to study real-world implementation of slash commands, error handling, and JSON-based case storage.

**Features**
- Slash Commands: /testing, /timeout, /kick, /ban, /warn, /report, /mute, /unban, /unmute, /case for moderation tasks.
- UI Components: Uses CaseContainer for consistent UI with dynamic case IDs, user data, reasons, proof (images), and timestamps.
- JSON Database: Stores case details (moderator, target, type, reason, file URLs) in cases.json for persistence and retrieval.
- Error Handling: Robust checks for permissions, invalid inputs, and API errors.
- Image Support: Handles up to 4 image attachments per command, displayed in a MediaGallery.

**File Structure**
```
project_root/
├── cogs/
│   ├── timeout.py      # Timeout command with duration
│   ├── kick.py        # Kick command
│   ├── ban.py         # Ban command
│   ├── warn.py        # Warn command with DM
│   ├── report.py      # Report to mod log
│   ├── mute.py        # Mute with role
│   ├── unban.py       # Unban by user ID
│   ├── unmute.py      # Remove mute role
│   ├── case.py        # Retrieve case by ID
├── utils/
│   ├── __init__.py    # Package marker
│   ├── db.py          # JSON database for cases
│   └── case.py        # CaseContainer for UI
├── index.py           # Main bot with cog loading
├── cases.json         # Case storage
└── .env               # DISCORD_TOKEN
```

**Setup**

Clone Repository:git clone [<repository-url>](https://github.com/kuwshyDEV/ModerationPlus-Bot)
cd project_root
 
Configure .env:DISCORD_TOKEN=your-bot-token

Create Muted Role: In your Discord server, create a "Muted" role with no send message/speak permissions.
Set Mod Log Channel: Update `mod_log_channel_id` in `report.py` with your channel ID.

Run Bot: `python index.py`



**Usage**
- Commands: Use /timeout @user 5, /mute @user 10, /kick @user, /ban @user, /warn @user, /report @user, /unban 123456789012345678, /unmute @user, /case 1 with optional reasons/images.
- UI: Commands display a CaseContainer with case ID, target, moderator, reason, proof (images), timestamp, and action buttons (Update, Revoke, History, Export, Share, Appeal).
- Database: Cases stored in cases.json for retrieval via /case.

**Learning Objectives**
- ComponentsV2: Understand ui.Container, ui.MediaGallery, ui.TextDisplay, ui.ActionRow, and ui.LayoutView.
- Slash Commands: Implement commands with dynamic parameters (user, reason, images, duration).
- Database: Learn JSON-based case storage and retrieval.
- Error Handling: Handle permissions, API errors, and invalid inputs.
- Attachments: Manage image uploads with discord.File and MediaGallery.

**Contributing**
This project is for educational purposes. Contributions are welcome to enhance features or fix bugs. Please:
- Follow the coding style (compact, commented, robust).
- Test changes with ComponentsV2 branch.
- Submit pull requests with clear descriptions.

**License**
MIT License. Use, modify, and share for educational purposes.
