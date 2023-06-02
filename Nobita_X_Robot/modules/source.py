from platform import python_version as y

from pyrogram import __version__ as z
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import __version__ as o
from telethon import __version__ as s

from Nobita_X_Robot import OWNER_ID, dispatcher
from Nobita_X_Robot import pbot as client

Star = "https://telegra.ph/file/26b5ac4684af8c68ebdce.jpg"


@client.on_message(filters.command(["repo", "source"]))
async def repo(client, message):
    await message.reply_photo(
        photo=Star,
        caption=f"""**ʜᴇʏ​ {message.from_user.mention()},\n\nɪ ᴀᴍ [{dispatcher.bot.first_name}](t.me/{dispatcher.bot.username})**

╔═════ஜ۩۞۩ஜ════╗

 🌹️𝗠𝗔𝗗𝗘 𝗕𝗬 [ησвι](tg://user?id={OWNER_ID})🌹
  
╚═════ஜ۩۞۩ஜ════╝

**[{dispatcher.bot.first_name}](t.me/{dispatcher.bot.username}) sᴏᴜʀᴄᴇ ɪs ɴᴏᴡ ᴩᴜʙʟɪᴄ ᴀɴᴅ ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ ᴍᴀᴋᴇ ʏᴏᴜʀ ᴏᴡɴ ʙᴏᴛ.**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•✨ᴏᴡɴᴇʀ✨",f"tg://user?id={OWNER_ID}"
                    ),
                    InlineKeyboardButton(
                        "✨ʀᴇᴘᴏ✨",
                        url="https://github.com/jaisingh007i/NOBITA-X_ROBOT",
                    ),
                ]
            ]
        ),
    )


__mod_name__ = "✨Rᴇᴩᴏ✨"
_help__ = """
 /repo  ᴛᴏ ɢᴇᴛ ʀᴇᴘᴏ 
 /source ᴛᴏ ɢᴇᴛ ʀᴇᴘᴏ
"""
