# LikeClean

A simple Selenium tool to bulk unlike liked Instagram posts and reels.

## Features

* Bulk unlike Instagram posts and reels
* Automatically repeats until all likes are removed
* Uses the Instagram web interface
* No Instagram API required

## Requirements

* Python 3.10+
* Google Chrome
* ChromeDriver
* Selenium 4.49.0

## Installation

```bash
git clone https://github.com/Anun-rgb/LikeClean
cd LikeClean
pip install selenium==4.49.0
```

## Usage

Run the script:

```bash
python3 IGLikeClean.py
```

Chrome will open and launch Instagram.

1. Log in to your Instagram account in Chrome.
2. Return to the terminal.
3. Press `Enter`.
4. LikeClean will automatically start removing your liked posts and reels.

The script processes the likes in batches and continues until there are no more liked posts.

## Disclaimer

This project is intended for personal and educational use.

Use it at your own risk and make sure your use complies with Instagram's terms of service.

