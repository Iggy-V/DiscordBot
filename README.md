# 🤖 Discord Bot for daily LeetCode Problems 🤖

## Overview
This Discord bot is designed to automatically post a random easy-level (or other level) LeetCode problem daily in a specified channel. It is ideal for coding communities that want to encourage daily coding practice among their members.

## Features
- **Daily Problem Posting:** Sends a random easy LeetCode problem to a designated Discord channel.
- **Problem Tracking:** Tracks which problems have been posted to avoid repetitions.
- **Automatic Updates:** Once a problem is posted, it is marked as used in the dataset.

## Setup
To get the bot running, you'll need to follow these setup instructions:

### Prerequisites
- Python 3.8 or newer
- Discord account and a bot token
- Server where the bot can be deployed

### Dependencies
Install the required Python packages:
```bash
pip install discord pandas python-dotenv
```

### Running it automatically
- Upload the code base to a cloud service (like AWS or Heroku)
- Use Windows/Linux task scheduler (currently using this one)
- Run it on a Raspberry Pi
