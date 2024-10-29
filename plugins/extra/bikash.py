# Power By @BikashHalder & @AdityaHalder 
# Join @BikashGadgetsTech For More Update
# Join @AdityaCheats For Hack
# Join Our Chats @Bgt_Chat & @Adityadiscus 

from pyrogram import Client, filters

from Bikash import app

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@app.on_message(
    filters.command("bikash")
    & filters.group)
async def repo(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/Help-08-24-13",
        caption=f"""🥀 bize destek olduğun için teşekkür ederiz:
  [KAYNAK KOD ](https://github.com/kumsalfed5456/kumsalXmusic)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🥀 admin 🥀", url=f"https://t.me/sevimsiz_biri")
            ],          
            [
                    InlineKeyboardButton(
                        "🥀 destek 🥀", url=f"https://t.me/kumsaldestekkanal")
                ],
                [
                    InlineKeyboardButton(
                        "🥀 sohbet 🥀", url=f"https://t.me/GeceSohbettr"
                    ),
                    InlineKeyboardButton(
                        "🥀 𝐔𝐩𝐝𝐚𝐭𝐞𝐬 🥀", url=f"https://t.me/Ragnarben")
                ]
            ]
        ),
    ) 

# Power By @BikashHalder & @AdityaHalder 
# Join @BikashGadgetsTech For More Update
# Join @AdityaCheats For Hack
# Join Our Chats @Bgt_Chat & @Adityadiscus 