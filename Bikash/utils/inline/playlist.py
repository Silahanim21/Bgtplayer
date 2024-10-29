from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def botplaylist_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="🤫 𝗉𝖾𝗋𝗌𝗈𝗇𝖾𝗅 🤫",
                callback_data="get_playlist_playmode",
            ),
            InlineKeyboardButton(
                text="🌎 𝗀𝗅𝗈𝖻𝖺𝗅 🌏", callback_data="get_top_playlists"
            ),
        ],
        [           
            InlineKeyboardButton(
                text="📱 𝗋𝖾𝗄𝗅𝖺𝗆.𝖺ş 📱", url=f"https://t.me/sevimsiz_biri"
            ),
        ],
        [
            InlineKeyboardButton(
                text="❌ 𝗀𝖾𝗋𝗂 ❌", callback_data="close"
            ),
        ],
    ]
    return buttons


def top_play_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝗅𝗂𝗌𝗍𝖾 𝗍𝗈𝗉 10", callback_data="SERVERTOP"
            )
        ],
        [
            InlineKeyboardButton(
                text="🤫 𝗉𝖾𝗋𝗌𝗈𝗇𝖾𝗅 🤫", callback_data="SERVERTOP user"
            )
        ],
        [
            InlineKeyboardButton(
                text="🌍 𝗀𝖾𝗇𝖾𝗅 🌏", callback_data="SERVERTOP global"
            ),
            InlineKeyboardButton(
                text="𝗀𝗋𝗎𝗉's", callback_data="SERVERTOP chat"
            )
        ],
        [           
            InlineKeyboardButton(
                text="📱 𝐘𝐨𝐮𝐭𝐮𝐛𝐞 📱", url=f"https://youtube.com/@BikashGadgetsTech"
            ),
        ],
        [
            InlineKeyboardButton(
                text="◁ 𝗀𝖾𝗋𝗂 ◁", callback_data="get_playmarkup"
            ),
            InlineKeyboardButton(
                text="❌ 𝗄𝖺𝗉𝖺𝗍 ❌", callback_data="close"
            ),
        ],
    ]
    return buttons


def get_playlist_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝖺𝗎𝖽𝗂𝗈 🔊", callback_data="play_playlist a"
            ),
            InlineKeyboardButton(
                text="𝗏𝗂𝖽𝖾𝗈 📽️", callback_data="play_playlist v"
            ),
        ],
        [
            InlineKeyboardButton(
                text="◁ 𝗀𝖾𝗋𝗂 ◁", callback_data="home_play"
            ),
            InlineKeyboardButton(
                text="❌ 𝗄𝖺𝗉𝖺𝗍 ❌", callback_data="close"
            ),
        ],
    ]
    return buttons


def top_play_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝐓𝐨𝐩 10 𝐏𝐥𝐚𝐲 𝐋𝐢𝐬𝐭", callback_data="SERVERTOP"
            )
        ],
        [
            InlineKeyboardButton(
                text="🤫 𝗉𝖾𝗋𝗌𝗈𝗇𝖾𝗅 🤫", callback_data="SERVERTOP Personal"
            )
        ],
        [
            InlineKeyboardButton(
                text="🌏 𝗀𝖾𝗇𝖾𝗅 🌎", callback_data="SERVERTOP Global"
            ),
            InlineKeyboardButton(
                text="☘ 𝗀𝗋𝗎𝗉'𝐬 ☘", callback_data="SERVERTOP Group"
            )
        ],
        [
            InlineKeyboardButton(
                text="◁ 𝗄𝖺𝗉𝖺𝗍 ◁", callback_data="get_playmarkup"
            ),
            InlineKeyboardButton(
                text="❌ 𝗀𝖾𝗋𝗂 ❌", callback_data="close"
            ),
        ],
    ]
    return buttons


def failed_top_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="◁ 𝗀𝖾𝗋𝗂 ◁",
                callback_data="get_top_playlists",
            ),
            InlineKeyboardButton(
                text="❌ 𝗄𝖺𝗉𝖺𝗍 ❌", callback_data="close"
            ),
        ],
    ]
    return buttons


def warning_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="🚫 𝗌𝗂𝗅 🚫",
                    callback_data="delete_whole_playlist",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="◁ 𝗀𝖾𝗋𝗂 ◁",
                    callback_data="del_back_playlist",
                ),
                InlineKeyboardButton(
                    text="❌ 𝗄𝖺𝗉𝖺𝗍 ❌",
                    callback_data="close",
                ),
            ],
        ]
    )
    return upl


def close_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="❌ kapat ❌",
                    callback_data="close",
                ),
            ]
        ]
    )
    return upl
