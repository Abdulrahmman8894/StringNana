from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Halo 
━━━━━━━━━━━━━━━━━━━━━━━━
{}
Kalo lu gak percaya bot ini, 
1) gak usah baca pesan ini anj
2) blokir bot atau delete chat ya tod
━━━━━━━━━━━━━━━━━━━━━━━━
By [Rzydx](https//t.me/Ngapain_Ngetag)
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("🔥 sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ 🔥", callback_data="generate")],
        [InlineKeyboardButton(text="ᴋᴇᴍʙᴀʟɪ", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("🔥 sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ 🔥", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("🔥 sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ 🔥", callback_data="generate")],
        [InlineKeyboardButton("ᴍᴀɪɴᴛᴀɴᴇᴅ ʙʏ", url="https://t.me/Ngapain_Ngetag")],
        [
            InlineKeyboardButton("ᴄᴀʀᴀ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ sᴀʏᴀ ❔", callback_data="help"),
            InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data="about")
        ],
        [InlineKeyboardButton("ɪɴғᴏ ʙᴏᴛ ʟᴀɪɴ", url="https://t.me/Diskras")],
    ]

    # Help Message
    HELP = """
✨ **Available Commands** ✨

/about - Tentang Bot ini
/help - This Message
/start - Mulai Bot
/generate - Mulai Generating Session
/cancel - Membatalkan process
/restart - Membatalkan process
"""

    # About Message
    ABOUT = """
**About This Bot** 

Sebuah telegram bot untuk mengambil pyrogram dan telethon string session by @AnyaStringbot

Group Support : [ɢᴀʙᴜɴɢ](https://t.me/Diskras)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : [Rzydx](https://t.me/Ngapain_Ngetag)
    """
