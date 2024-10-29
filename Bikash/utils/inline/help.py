from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Bikash import app

def help_pannel(_, START: Union[bool, int] = None):
    first = [
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        )
    ]
    second = [
        InlineKeyboardButton(
            # text=_["BACK_BUTTON"],
            text="📡 𝐠𝐮𝐧𝐜𝐞𝐥𝐥𝐞𝐦𝐞 📡",
            url=f"https://t.me/kumsaldestekkanal",
        ),
        InlineKeyboardButton(
            text="🛠️𝐚𝐝𝐦𝐢𝐧🛠️",
            url=f"t.me/sevimsiz_biri",
        ),
        InlineKeyboardButton(
            text="❌ 𝐂𝐥𝐨𝐬𝐞 ❌", callback_data=f"close"
        ),
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="Admin",
                    callback_data="help_callback hb1",
                ),
                InlineKeyboardButton(
                    text="𝐲𝐞𝐭𝐤𝐢𝐥𝐢",
                    callback_data="help_callback hb2",
                ),
                InlineKeyboardButton(
                    text="𝐛𝐥𝐨𝐤𝐞",
                    callback_data="help_callback hb3",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="𝐫𝐞𝐤𝐥𝐚𝐦",
                    callback_data="help_callback hb4",
                ),
                InlineKeyboardButton(
                    text="𝐝𝐚𝐡𝐚-𝐟𝐚𝐳𝐥𝐚",
                    callback_data="help_callback hb5",
                ),
                InlineKeyboardButton(
                    text="𝐠-𝐛𝐚𝐧",
                    callback_data="help_callback hb12",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Google",
                    callback_data="help_callback hb14",
                ),
                InlineKeyboardButton(
                    text="InFo",
                    callback_data="help_callback hb13",
                ),
                InlineKeyboardButton(
                    text="𝐟𝐨𝐭𝐨ğ𝐫𝐚𝐟",
                    callback_data="help_callback hb15",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="𝐠𝐢𝐭",
                    callback_data="help_callback hb16",
                ),
                InlineKeyboardButton(
                    text="𝐨𝐲𝐧𝐚𝐭",
                    callback_data="help_callback hb8",
                ),
                InlineKeyboardButton(
                    text="Ping",
                    callback_data="help_callback hb7",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Playlist",
                    callback_data="help_callback hb6",
                ),
                InlineKeyboardButton(
                    text="𝐤𝐚𝐲𝐧𝐚𝐤 𝐤𝐨𝐝",
                    callback_data="help_callback hb17",
                ),
                InlineKeyboardButton(
                    text="𝐢𝐥𝐞𝐫𝐢 𝐚𝐥",
                    callback_data="help_callback hb18",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🐯 𝐬𝐮𝐝𝐨 🐯",
                    callback_data="help_callback hb9",
                ),
                InlineKeyboardButton(
                    text="💖 𝐛𝐚𝐬𝐥𝐚𝐭 💖",
                    callback_data="help_callback hb11",
                ),
                InlineKeyboardButton(
                    text="VideoChats",
                    callback_data="help_callback hb10",
                ),
            ],
            mark,
        ]
    )
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    # text=_["BACK_BUTTON"],
                    text="⇦ 𝐠𝐞𝐫𝐢 ⇨",
                    callback_data=f"settings_back_helper",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"], callback_data=f"close"
                )
            ]
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="Back",
                callback_data="settings_back_helper",
            ),
        ],
    ]
    return buttons
