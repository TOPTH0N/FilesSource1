# Repthon🔥
# Repthon - Baqir
# Copyright (C) 2023 RepthonArabic . All Rights Reserved
#
# This file is a part of < https://github.com/RepthonArabic/RepthonAr/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/RepthonArabic/RepthonAr/blob/master/LICENSE/>.


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
from ..core.managers import edit_delete, edit_or_reply
from ..helpers import media_type
from ..helpers.utils import reply_id




#Code by T.me/zzzzl1l
@zedub.zed_cmd(pattern=f"تيك(?: |$)(.*)")
async def baqir_tiktok(event):
    LAN = event.pattern_match.group(1)
    if LAN: #Write Code By T.me/zzzzl1l
        ROGER = LAN
    elif event.is_reply:
        ROGER = await event.get_reply_message()
    else:
        return await edit_or_reply(event, "**⎉╎بالـࢪد ؏ــلى رابـط تيـك تـوك**")
    chat = "@downloader_tiktok_bot" #Code by T.me/zzzzl1l
    rep = await edit_or_reply(event, "**⎉╎جـارِ التحميـل من تيـك تـوك ...**")
    async with borg.conversation(chat) as conv: #Code by T.me/zzzzl1l
        try:
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message(ROGER) #Code by T.me/zzzzl1l
            repthon = await conv.get_response()
            await rep.delete()
            await borg.send_file(
                event.chat_id,
                repthon,
                caption=f"<b>⎉╎تم تحميل الفيديـو .. بنجاح 🎬</b>",
                parse_mode="html",
            )
        except YouBlockedUserError: #Code by T.me/zzzzl1l
            await zedub(unblock("downloader_tiktok_bot"))
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message(ROGER)
            repthon = await conv.get_response()
            await rep.delete()
            await borg.send_file(
                event.chat_id,
                repthon,
                caption=f"<b>⎉╎تم تحميل الفيديـو .. بنجاح 🎬</b>",
                parse_mode="html",
            )
