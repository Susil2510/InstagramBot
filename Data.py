from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

**Welcome to {}**

**I can download profile pictures, videos, images and reels from instagram along with post caption.
You can also authorize me to download private posts.**

**Use below buttons to learn more.**

**By @TheBotsWorldachannel**
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("✨ Bot Status and More Bots ✨", url="https://t.me/TheBotsWorldChannel")],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("🎪 About 🎪", callback_data="about")
        ],
            InlineKeyboardButton(" 🇺🇸Donate Withought Using Money", url="https://t.me/BuyLikeRobot?start=1272416568")
        ],
        [InlineKeyboardButton("♥ Developer ♥", url="https://t.me/ToxicDeeModderr")],
    ]

    # Help Message
    HELP = """
1) **Images, Videos and Reels**
Send the link here to get the post contents including caption.

2) **Profile Pictures**
Use the command `/profile_pic` or `/dp` along with instagram username to get its profile picture.
Example : `/dp TeslaProgrammer`

3) **Private Posts**
Authorize the bot to download private posts. Use /auth

**Note** : Stories and IGTV are not supported.

Use /auth to authorize and /unauth to unauthorize.
"""

    # About Message
    ABOUT = """
**About This Bot** 

A telegram bot to download instagram content by @ToxicDeeModderr

Source Code : [Click Here](https://t.me/ToxicDeeModderr)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @ToxicGamingVpn
    """
