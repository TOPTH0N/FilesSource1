# Syntral - Syntral
# Copyright (C) 2023 Syntrel. All Rights Reserved
#
# This file is a part of < https://github.com/TOPTH0N/FilesSource1/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TOPTH0N/FilesSource1/blob/master/LICENSE/>.
""" 
OpenAi & ChatGpt for Syntral™ t.me/Syntral
Write file by AhMeD, ALSiD t.me/S_i_D, t.me/zqqqzq
ها خماط بعدك تخمط مني .. ماتستحي ؟
متى راح تصير مطور وانت مقضيها خمط تعب وحقوق الناس
ههههههههههههههههههههههههههههههههههههههههههههههههههههههه
"""

import requests
import asyncio
import os
import sys
import urllib.request
from datetime import timedelta
from telethon import events
from telethon.errors import FloodWaitError
from telethon.tl.functions.messages import GetHistoryRequest, ImportChatInviteRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest as unblock
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from . import zedub
from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import reply_id

plugin_category = "البوت"


# code by t.me/zqqqzq
@zedub.zed_cmd(pattern="السيد(?: |$)(.*)")
async def zelzal_gpt(event):
    zilzal = event.pattern_match.group(1)
    zzz = await event.get_reply_message()
    chat = "@GPT4Telegrambot" #code by t.me/zqqqzq
    if not zilzal and not event.reply_to_msg_id:
        return await edit_or_reply(event, "**⎉╎بالـرد ع سـؤال او باضـافة السـؤال للامـر**\n**⎉╎مثـــال :**\n`.السيد من هو مكتشف الجاذبية الارضية`")
    if not zilzal and event.reply_to_msg_id and zzz.text: #code by t.me/zqqqzq
        zelzal = zzz.text
    if not event.reply_to_msg_id: #code by t.me/zqqqzq
        zelzal = event.pattern_match.group(1)
    zed = await edit_or_reply(event, "**⎉╎جـارِ الاتصـال بـ الذكـاء الاصطنـاعـي\n⎉╎الرجـاء الانتظـار .. لحظـات**")
    async with borg.conversation(chat) as conv: #code by t.me/zqqqzq
        try:
            await conv.send_message(zelzal)
            zzzthon = await conv.get_response()
            ahmed = zzzthon.text
            if "another 8 seconds" in zzzthon.text: #code by t.me/zqqqzq
                aa = ahmed.replace("⏳ Please wait another 8 seconds before sending the next question . . .", "**⎉╎يُرجى الانتظار 8 ثوانٍ ⏳\n⎉╎بين ارسـال كل سـؤال والتـالي**") 
                await event.delete()
                return await borg.send_message(event.chat_id, aa)
            await asyncio.sleep(5)
            zedthon = await conv.get_response()
            malath = zedthon.text
            if "understanding" in zedthon.text: #code by t.me/zqqqzq
                aa = malath.replace("⏳ Please wait another 8 seconds before sending the next question . . .", "**- عـذراً .. لم أفهم سؤالك\n- قم بـ إعادة صياغته من فضلك؟!**") 
                await event.delete()
                return await borg.send_message(event.chat_id, aa)
            await zed.delete()
            await borg.send_message(event.chat_id, f"**س/ {zelzal}\n\n{malath}**\n\n───────────────────\nSyntrel 𝗨**ꜱᴇʀʙᴏᴛ** 𝗧**ᴏᴏʟꜱ**\n\t\t\t\t\t\t\t\tSyntrel • ᴼᵖᵉⁿᴬᴵ")
        except YouBlockedUserError: #code by t.me/zqqqzq
            await zedub(unblock("GPT4Telegrambot"))
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message(zelzal)
            zzzthon = await conv.get_response()
            ahmed = zzzthon.text
            if "another 8 seconds" in zzzthon.text: #code by t.me/zqqqzq
                aa = ahmed.replace("⏳ Please wait another 8 seconds before sending the next question . . .", "**⎉╎يُرجى الانتظار 8 ثوانٍ ⏳\n⎉╎بين ارسـال كل سـؤال والتـالي**") 
                await event.delete()
                return await borg.send_message(event.chat_id, aa)
            await asyncio.sleep(5)
            zedthon = await conv.get_response()
            malath = zedthon.text
            if "understanding" in zedthon.text: #code by t.me/zqqqzq
                aa = malath.replace("I'm sorry, I'm not quite understanding the question. Could you please rephrase it?", "**- عـذراً .. لم أفهم سؤالك\n- قم بـ إعادة صياغته من فضلك؟!**") 
                await event.delete()
                return await borg.send_message(event.chat_id, aa)
            if "Please wait a moment" in zedthon.text: #code by t.me/zqqqzq
                await asyncio.sleep(5)
                zedthon = await conv.get_response()
                malath = zedthon.text
            await zed.delete()
            await borg.send_message(event.chat_id, f"**س/ {zelzal}\n\n{malath}**\n\n───────────────────\nSyntrel 𝗨**ꜱᴇʀʙᴏᴛ** 𝗧**ᴏᴏʟꜱ**\n\t\t\t\t\t\t\t\tᶻᵉˡᶻᵃˡ • ᴼᵖᵉⁿᴬᴵ")


# تخمــط اهينـــك Fak-You

# code by t.me/zqqqzq
@zedub.zed_cmd(pattern="س(?: |$)(.*)")
async def zelzal_gpt(event):
    zilzal = event.pattern_match.group(1)
    zzz = await event.get_reply_message()
    chat = "@GPT4Telegrambot" #code by t.me/zqqqzq
    if not zilzal and not event.reply_to_msg_id:
        return await edit_or_reply(event, "**⎉╎بالـرد ع سـؤال او باضـافة السـؤال للامـر**\n**⎉╎مثـــال :**\n`.السيد من هو مكتشف الجاذبية الارضية`")
    if not zilzal and event.reply_to_msg_id and zzz.text: #code by t.me/zqqqzq
        zelzal = zzz.text
    if not event.reply_to_msg_id: #code by t.me/zqqqzq
        zelzal = event.pattern_match.group(1)
    zed = await edit_or_reply(event, "**⎉╎جـارِ الاتصـال بـ الذكـاء الاصطنـاعـي\n⎉╎الرجـاء الانتظـار .. لحظـات**")
    async with borg.conversation(chat) as conv: #code by t.me/zqqqzq
        try:
            await conv.send_message(zelzal)
            zzzthon = await conv.get_response()
            ahmed = zzzthon.text
            if "another 8 seconds" in zzzthon.text: #code by t.me/zqqqzq
                aa = ahmed.replace("⏳ Please wait another 8 seconds before sending the next question . . .", "**⎉╎يُرجى الانتظار 8 ثوانٍ ⏳\n⎉╎بين ارسـال كل سـؤال والتـالي**") 
                await event.delete()
                return await borg.send_message(event.chat_id, aa)
            await asyncio.sleep(5)
            zedthon = await conv.get_response()
            malath = zedthon.text
            if "understanding" in zedthon.text: #code by t.me/zqqqzq
                aa = malath.replace("⏳ Please wait another 8 seconds before sending the next question . . .", "**- عـذراً .. لم أفهم سؤالك\n- قم بـ إعادة صياغته من فضلك؟!**") 
                await event.delete()
                return await borg.send_message(event.chat_id, aa)
            if "Please wait a moment" in zedthon.text: #code by t.me/zqqqzq
                await asyncio.sleep(5)
                zedthon = await conv.get_response()
                malath = zedthon.text
            await zed.delete()
            await borg.send_message(event.chat_id, f"**س/ {zelzal}\n\n{malath}**\n\n───────────────────\nSyntrel 𝗨**ꜱᴇʀʙᴏᴛ** 𝗧**ꜱᴇʀʙᴏᴛ**\n\t\t\t\t\t\t\t\tSyntrel • ᴼᵖᵉⁿᴬᴵ")
        except YouBlockedUserError: #code by t.me/zqqqzq
            await zedub(unblock("GPT4Telegrambot"))
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message(zelzal)
            zzzthon = await conv.get_response()
            ahmed = zzzthon.text
            if "another 8 seconds" in zzzthon.text: #code by t.me/zqqqzq
                aa = ahmed.replace("⏳ Please wait another 8 seconds before sending the next question . . .", "**⎉╎يُرجى الانتظار 8 ثوانٍ ⏳\n⎉╎بين ارسـال كل سـؤال والتـالي**") 
                await event.delete()
                return await borg.send_message(event.chat_id, aa)
            await asyncio.sleep(5)
            zedthon = await conv.get_response()
            malath = zedthon.text
            if "understanding" in zedthon.text: #code by t.me/zqqqzq
                aa = malath.replace("I'm sorry, I'm not quite understanding the question. Could you please rephrase it?", "**- عـذراً .. لم أفهم سؤالك\n- قم بـ إعادة صياغته من فضلك؟!**") 
                await event.delete()
                return await borg.send_message(event.chat_id, aa)
            await zed.delete()
            await borg.send_message(event.chat_id, f"**س/ {zelzal}\n\n{malath}**\n\n───────────────────\nSyntral 𝗨**ꜱᴇʀʙᴏᴛ** 𝗧**ᴏᴏʟꜱ**\n\t\t\t\t\t\t\t\tSyntral • ᴼᵖᵉⁿᴬᴵ")
