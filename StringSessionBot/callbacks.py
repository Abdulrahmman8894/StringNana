from Data import Data
from pyrogram import Client
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from StringSessionBot.generate import generate_session, ERROR_MESSAGE


# Callbacks
@Client.on_callback_query()
async def _callbacks(bot: Client, callback_query: CallbackQuery):
    user = await bot.get_me()
    # user_id = callback_query.from_user.id
    mention = user["mention"]
    query = callback_query.data.lower()
    if query.startswith("home"):
        if query == 'home':
            chat_id = callback_query.from_user.id
            message_id = callback_query.message.message_id
            await bot.edit_message_text(
                chat_id=chat_id,
                message_id=message_id,
                text=Data.START.format(callback_query.from_user.mention, mention),
                reply_markup=InlineKeyboardMarkup(Data.buttons),
            )
    elif query == "about":
        chat_id = callback_query.from_user.id
        message_id = callback_query.message.message_id
        await bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=Data.ABOUT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(Data.home_buttons),
        )
    elif query == "help":
        chat_id = callback_query.from_user.id
        message_id = callback_query.message.message_id
        await bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text="**Here's How to use me**\n" + Data.HELP,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(Data.home_buttons),
        )
    elif query == "generate":
        await callback_query.message.reply(
            "𝗦𝘁𝗿𝗶𝗻𝗴 𝗦𝗲𝘀𝘀𝗶𝗼𝗻 𝗠𝗮𝗻𝗮 𝗬𝗮𝗻𝗴 𝗶𝗻𝗴𝗶𝗻 𝗔𝗻𝗱𝗮 𝗕𝘂𝗮𝘁?
             • 𝗧𝗲𝗹𝗲𝘁𝗵𝗼𝗻 𝗨𝗻𝘁𝘂𝗸 (𝗨𝘀𝗲𝗿𝗯𝗼𝘁)
             • 𝗣𝘆𝗿𝗼𝗴𝗿𝗮𝗺 𝗨𝗻𝘁𝘂𝗸 (𝗕𝗢𝗧 𝗠𝘂𝘀𝗶𝗰)",
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("ᴘʏʀᴏɢʀᴀᴍ", callback_data="pyrogram"),
                InlineKeyboardButton("ᴛᴇʟᴇᴛʜᴏɴ", callback_data="telethon")
            ]])
        )
    elif query in ["pyrogram", "telethon"]:
        await callback_query.answer()
        try:
            if query == "pyrogram":
                await generate_session(bot, callback_query.message)
            else:
                await generate_session(bot, callback_query.message, telethon=True)
        except Exception as e:
            await callback_query.message.reply(ERROR_MESSAGE.format(str(e)))
