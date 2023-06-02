import os
from Nobita_X_Robot import telethn as tbot
from Nobita_X_Robot.events import register
from telethon import events
try:
	from phlogo import generate
except ModuleNotFoundError:
	os.system("pip install phlogo")
	from phlogo import generate

@register(pattern="^[!/.]phlogo ?(.*)")
async def ph(event):
	query = event.pattern_match.group(1)
	await event.message.delete()
	if query == "":
		await event.reply("ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ʙʀᴜʜ, ᴇ.ɢ.: `/phlogo star boi`")
		return
	try:
		p = query.split(" ", 1)[0]
		h = query.split(" ", 1)[1]
	except:
		await event.reply("sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ, ᴛʀʏ ɢɪᴠɪɴɢ ᴛᴡᴏ ᴡᴏʀᴅs. ᴇ.ɢ.: `/phlogo star boi`")
		return
	result = generate(f"{p}",f"{h}")
	pic = "ph.png"
	result.save(pic, "png")
	await tbot.send_file(event.chat_id, pic, reply_to=event.reply_to_msg_id, forcedocument=False)
	os.remove(pic)


@register(pattern="^[!/.]phst ?(.*)")
async def ph(event):
	query = event.pattern_match.group(1)
	try:
		await event.message.delete()
	except:
		pass
	if query == "":
		await event.reply("ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ʙʀᴜʜ, ᴇ.ɢ.: `/phst star boi`")
		return
	try:
		p = query.split(" ", 1)[0]
		h = query.split(" ", 1)[1]
	except:
		await event.reply("sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ, ᴛʀʏ ɢɪᴠɪɴɢ ᴛᴡᴏ ᴡᴏʀᴅs. ᴇ.ɢ.: `/phst Razer Bot`")
		return
	result = generate(f"{p}",f"{h}")
	stc = "ph.webp"
	result.save(stc, "webp")
	await tbot.send_file(event.chat_id, stc, reply_to=event.reply_to_msg_id, forcedocument=False)
	os.remove(stc)

__mod_name__ = "🌹ᴘ-ʜᴜʙ Lᴏɢᴏ🌹"
__help__ = """PᴏʀɴHᴜʙ Lᴏɢᴏ
ᴜsᴀɢᴇ:
⋗ /phlogo <word1> <word2> | Tᴏ ɢᴇɴᴇʀᴀᴛᴇ ʟᴏɢᴏ ᴀs ɪᴍᴀɢᴇ
⋗ /phst <word1> <word2> | Tᴏ ɢᴇɴᴇʀᴀᴛᴇ ʟᴏɢᴏ ᴀs sᴛɪᴄᴋᴇʀ
"""
