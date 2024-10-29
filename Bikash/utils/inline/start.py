from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from Bikash import config
from Bikash import app


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="❰ 𝗒𝖺𝗋𝖽ı𝗆 𝗄𝗈𝗆𝗎𝗍𝗅𝖺𝗋 ❱",
                url=f"https://t.me/{BOT_USERNAME}?start=help",
            )
        ],
        [
            InlineKeyboardButton(
                text="⚙ 𝖻𝗈𝗍 𝖺𝗒𝖺𝗋𝗅𝖺𝗋ı ⚙", callback_data="settings_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="💖 𝖽𝗎𝗒𝗎𝗋𝗎 💖", url=config.SUPPORT_CHANNEL
            ),
            InlineKeyboardButton(
                text="💖 𝖽𝖾𝗌𝗍𝖾𝗄 💖", url=config.SUPPORT_GROUP
            )
        ],
        [           
            InlineKeyboardButton(
                text="📱 𝖺𝖽𝗆𝗂𝗇 📱", url=f"https://t.me/sevimsiz_biri"
            )
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="➕ ❰ 𝖻𝖾𝗇𝗂 𝗀𝗋𝗎𝖻𝗎𝗇𝖺 𝖾𝗄𝗅𝖾 ❱ ➕",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="💖 𝗒𝖺𝗋𝖽𝗂𝗆 💖", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="🥀 𝖽𝗎𝗒𝗎𝗋𝗎 💥", url=config.SUPPORT_CHANNEL
            ),
            InlineKeyboardButton(
                text="🥀 𝖽𝖾𝗌𝗍𝖾𝗄 💥", url=config.SUPPORT_GROUP
            )
        ],
        [           
            InlineKeyboardButton(
                text="📱 YouTube 📱", url=f"https://t.me/sevimsiz_biri"
            )
        ],
        [
            InlineKeyboardButton(
                text="♕ 𝖪𝖴𝖱𝖴𝖢𝖴 ♕", user_id=OWNER
            )
        ]
     ]
    return buttons
