from datetime import datetime

from telethon.utils import get_display_name

from zthon import zedub
from zthon.core.logger import logging

from ..Config import Config
from ..core import CMD_INFO, PLG_INFO
from ..core.data import _sudousers_list, sudo_enabled_cmds
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import get_user_from_event, mentionuser
from ..sql_helper import global_collectionjson as sql
from ..sql_helper import global_list as sqllist
from ..sql_helper.globals import addgvar, delgvar, gvarstatus

plugin_category = "الادوات"

LOGS = logging.getLogger(__name__)

ZDEV = gvarstatus("sudoenable") or "true"

BaqirDV_cmd = (
    "𓆩 [𝗦𝗼𝘂𝗿𝗰𝗲 Syntral 𝗖𝗼𝗻𝗳𝗶𝗴 - اوامــر المطـور المســاعد](t.me/Syntral) 𓆪\n\n"
    "**✾╎قائـمـه اوامـر رفـع المطـور المسـاعـد 🧑🏻‍💻✅ 🦾 :** \n"
    "**- اضغـط ع الامـر للنسـخ ثـم استخـدمهـا بالتـرتيـب** \n\n"
    "**⪼** `.رفع مطور` \n"
    "**- لـ رفـع الشخـص مطـور مسـاعـد معـك بالبـوت** \n\n"
    "**⪼** `.تنزيل مطور` \n"
    "**- لـ تنزيـل الشخـص مطـور مسـاعـد مـن البـوت** \n\n"
    "**⪼** `.وضع المطور تفعيل` \n"
    "**لـ تفعيـل وضـع المطـورين المسـاعدين** \n\n"
    "**⪼** `.وضع المطور تعطيل` \n"
    "**لـ تعطيـل وضـع المطـورين المسـاعدين** \n\n"
    "**⪼** `.تحكم الكل` \n"
    "**- اعطـاء المطـورين المرفـوعيـن صلاحيـة التحكـم الكـاملـه بالاوامــر ✓** \n\n"
    "**⪼** `.ايقاف تحكم الكل` \n"
    "**- ايقـاف صلاحيـة التحكـم الكـاملـه بالاوامــر للمطـورين المرفـوعيـن ✓** \n\n"
    "**🛃 ملاحظـة مهمـه:**\n"
    "لـرفع مطـور ارسـل الامـر (.رفع مطور) بالـرد ع الشخص ثـم الامر (.وضع المطور تفعيل) لتفعيـل وضع المطور ثم (.تحكم الكل) .. الاوامـر الثاني والثالث فقط تدزهن اول مـره\n\n"
    "\n𓆩 [ALSiD](t.me/S_i_D) 𓆪"
)


async def _init() -> None:
    sudousers = _sudousers_list()
    Config.SUDO_USERS.clear()
    for user_d in sudousers:
        Config.SUDO_USERS.add(user_d)


def get_key(val):
    for key, value in PLG_INFO.items():
        for cmd in value:
            if val == cmd:
                return key
    return None


@zedub.zed_cmd(
    pattern="وضع المطور (تفعيل|تعطيل)$",
    command=("وضع المطور", plugin_category),
    info={
        "header": "لـ تفعيـل/تعطيـل وضـع المطــور وفتـح/قفـل التحكـم لـ المطــور",
        "الاستـخـدام": "{tr}وضع المطور تفعيل / تعطيل",
    },
)
async def chat_blacklist(event):
    "لـ تفعيـل/تعطيـل وضـع المطــور وفتـح/قفـل التحكـم لـ المطــور"
    input_str = event.pattern_match.group(1)
    sudousers = _sudousers_list()
    if input_str == "تفعيل":
        if gvarstatus("sudoenable") is not None:
            return await edit_delete(event, "**- وضـع المطــور فـي وضـع التفعيـل مسبقــاً ✓**")
        addgvar("sudoenable", "true")
        text = "**✾╎تـم تفعـيل وضـع المطــور المسـاعـد .. بنجــاح✓**\n\n"
        if len(sudousers) != 0:
            text += (
                "**✾╎يتم الان اعـادة تشغيـل بـوت السيد انتظـر 2-1 دقيقـه ▬▭ ...**"
            )
            msg = await edit_or_reply(
                event,
                text,
            )
            return await event.client.reload(msg)
        text += "**- انت لـم تقـم برفـع احـد بعـد**"
        return await edit_or_reply(
            event,
            text,
        )
    if gvarstatus("sudoenable") is not None:
        delgvar("sudoenable")
        text = "**✾╎تـم تعطيـل وضـع المطــور المسـاعـد .. بنجــاح✓**\n\n"
        if len(sudousers) != 0:
            text += (
                "**✾╎يتم الان اعـادة تشغيـل بـوت السيد انتظـر 2-1 دقيقـه ▬▭ ...**"
            )
            msg = await edit_or_reply(
                event,
                text,
            )
            return await event.client.reload(msg)
        text += "**You haven't added any chat to blacklist yet.**"
        return await edit_or_reply(
            event,
            text,
        )
    await edit_delete(event, "**- وضـع المطــور فـي وضـع التعطيـل مسبقــاً ✓**")


@zedub.zed_cmd(
    pattern="رفع مطور(?:\s|$)([\s\S]*)",
    command=("رفع مطور", plugin_category),
    info={
        "header": "لـ رفـع مطـورين فـي بـوتك",
        "الاستـخـدام": "{tr}رفع مطور بالـرد / المعرف / الايدي",
    },
)
async def add_sudo_user(event):
    "لـ رفـع مطـورين فـي بـوتك"
    replied_user, error_i_a = await get_user_from_event(event)
    if replied_user is None:
        return
    if replied_user.id == event.client.uid:
        return await edit_delete(event, "** عـذراً .. لايمكـنـك رفـع نفسـك**")
    if replied_user.id in _sudousers_list():
        return await edit_delete(
            event,
            f"**✾╎المستخـدم**  {mentionuser(get_display_name(replied_user),replied_user.id)}  **موجـود بالفعـل فـي قائمـة مطـورين البـوت 🧑🏻‍💻...**",
        )
    date = str(datetime.now().strftime("%B %d, %Y"))
    userdata = {
        "chat_id": replied_user.id,
        "chat_name": get_display_name(replied_user),
        "chat_username": replied_user.username,
        "date": date,
    }
    try:
        sudousers = sql.get_collection("sudousers_list").json
    except AttributeError:
        sudousers = {}
    sudousers[str(replied_user.id)] = userdata
    sql.del_collection("sudousers_list")
    sql.add_collection("sudousers_list", sudousers, {})
    output = f"**✾╎تـم رفـع**  {mentionuser(userdata['chat_name'],userdata['chat_id'])}  **مطـور مسـاعـد معـك فـي البـوت 🧑🏻‍💻...**\n\n"
    output += "**✾╎يتم الان اعـادة تشغيـل بـوت السيد انتظـر 2-1 دقيقـه ▬▭ ...**"
    msg = await edit_or_reply(event, output)
    await event.client.reload(msg)


@zedub.zed_cmd(
    pattern="تنزيل مطور(?:\s|$)([\s\S]*)",
    command=("تنزيل مطور", plugin_category),
    info={
        "header": "لـ تنزيـل مطـور مـن بـوتك",
        "الاستـخـدام": "{tr}تنزيل مطور بالـرد / المعرف / الايدي",
    },
)
async def _(event):
    "لـ تنزيـل مطـور مـن بـوتك"
    replied_user, error_i_a = await get_user_from_event(event)
    if replied_user is None:
        return
    try:
        sudousers = sql.get_collection("sudousers_list").json
    except AttributeError:
        sudousers = {}
    if str(replied_user.id) not in sudousers:
        return await edit_delete(
            event,
            f"** - المسـتخـدم :** {mentionuser(get_display_name(replied_user),replied_user.id)} \n\n**- انـه ليـس في قائمـة مطـورين البــوت.**",
        )
    del sudousers[str(replied_user.id)]
    sql.del_collection("sudousers_list")
    sql.add_collection("sudousers_list", sudousers, {})
    output = f"**✾╎تـم تنـزيـل**  {mentionuser(get_display_name(replied_user),replied_user.id)}  **مـن قـائمـة مطـورين البـوت 🧑🏻‍💻...**\n\n"
    output += "**✾╎يتم الان اعـادة تشغيـل بـوت السيد انتظـر 2-1 دقيقـه ▬▭ ...**"
    msg = await edit_or_reply(event, output)
    await event.client.reload(msg)


@zedub.zed_cmd(
    pattern="المطورين$",
    command=("المطورين", plugin_category),
    info={
        "header": "لـ عـرض قائمــه بمطـورين بــوتك",
        "الاستـخـدام": "{tr}المطورين",
    },
)
async def _(event):
    "لـ عـرض قائمــه بمطـورين بــوتك"
    sudochats = _sudousers_list()
    try:
        sudousers = sql.get_collection("sudousers_list").json
    except AttributeError:
        sudousers = {}
    if len(sudochats) == 0:
        return await edit_delete(
            event, "**•❐• لا يـوجـد هنـاك مطـورين في قائمــة مـطـورين البــوت الخـاص بـك الى الان**"
        )
    result = "**•❐• قائمــة مـطـورين البــوت الخـاص بـك مـن Syntral :**\n\n"
    for chat in sudochats:
        result += f"**🧑🏻‍💻╎المطــور :** {mentionuser(sudousers[str(chat)]['chat_name'],sudousers[str(chat)]['chat_id'])}\n\n"
        result += f"**- تـم رفعـه بتـاريـخ :** {sudousers[str(chat)]['date']}\n\n"
    await edit_or_reply(event, result)


@zedub.zed_cmd(
    pattern="تحكم(s)?(?:\s|$)([\s\S]*)",
    command=("تحكم", plugin_category),
    info={
        "header": "To enable cmds for sudo users.",
        "flags": {
            "عام": "Will enable all cmds for sudo users. (except few like eval, exec, profile).",
            "الكل": "Will add all cmds including eval,exec...etc. compelete sudo.",
            "امر": "Will add all cmds from the given plugin names.",
        },
        "usage": [
            "{tr}تحكم عام",
            "{tr}تحكم الكل",
            "{tr}addscmd -p <plugin names>",
            "{tr}addscmd <commands>",
        ],
        "مثــال": [
            "{tr}addscmd -p autoprofile botcontrols i.e, for multiple names use space between each name",
            "{tr}addscmd ping alive i.e, for multiple names use space between each name",
        ],
    },
)
async def _(event):  # sourcery no-metrics
    "To enable cmds for sudo users."
    input_str = event.pattern_match.group(2)
    errors = ""
    sudocmds = sudo_enabled_cmds()
    if not input_str:
        return await edit_or_reply(
            event, "__Which command should i enable for sudo users . __"
        )
    input_str = input_str.split()
    if input_str[0] == "عام":
        zedevent = await edit_or_reply(event, "__Enabling all safe cmds for sudo....__")
        totalcmds = CMD_INFO.keys()
        flagcmds = (
            PLG_INFO["botcontrols"]
            + PLG_INFO["الوقتي"]
            + PLG_INFO["التحديث"]
            + PLG_INFO["الاوامر"]
            + PLG_INFO["هيروكو"]
            + PLG_INFO["الادمن"]
            + PLG_INFO["الحمايه"]
            + PLG_INFO["الاغاني"]
            + PLG_INFO["المجموعه"]
            + PLG_INFO["اعاده تشغيل"]
            + PLG_INFO["تحويل الصيغ"]
            + PLG_INFO["المطور"]
            + PLG_INFO["بوت الحمايه"]
            + ["gauth"]
            + ["greset"]
        )
        loadcmds = list(set(totalcmds) - set(flagcmds))
        if len(sudocmds) > 0:
            sqllist.del_keyword_list("sudo_enabled_cmds")
    elif input_str[0] == "الكل":
        zedevent = await edit_or_reply(
            event, "__Enabling compelete sudo for users....__"
        )
        loadcmds = CMD_INFO.keys()
        if len(sudocmds) > 0:
            sqllist.del_keyword_list("sudo_enabled_cmds")
    elif input_str[0] == "امر":
        zedevent = event
        input_str.remove("امر")
        loadcmds = []
        for plugin in input_str:
            if plugin not in PLG_INFO:
                errors += (
                    f"`{plugin}` __There is no such plugin in your ZThon__.\n"
                )
            else:
                loadcmds += PLG_INFO[plugin]
    else:
        zedevent = event
        loadcmds = []
        for cmd in input_str:
            if cmd not in CMD_INFO:
                errors += f"`{cmd}` __There is no such command in your ZThon__.\n"
            elif cmd in sudocmds:
                errors += f"`{cmd}` __Is already enabled for sudo users__.\n"
            else:
                loadcmds.append(cmd)
    for cmd in loadcmds:
        sqllist.add_to_list("sudo_enabled_cmds", cmd)
    result = f"**✾╎تـم تفعيـل التحكـم الكـامل لـ**  `{len(loadcmds)}` **امـر 🧑🏻‍💻✅**\n"
    output = (
        result + "**✾╎يتم الان اعـادة تشغيـل بـوت السيد انتظـر 2-1 دقيقـه ▬▭ ...**\n"
    )
    if errors != "":
        output += "\n**- خطــأ :**\n" + errors
    msg = await edit_or_reply(zedevent, output)
    await event.client.reload(msg)


@zedub.zed_cmd(
    pattern="ايقاف تحكم(s)?(?:\s|$)([\s\S]*)?",
    command=("ايقاف تحكم", plugin_category),
    info={
        "header": "To disable given cmds for sudo.",
        "flags": {
            "-all": "Will disable all enabled cmds for sudo users.",
            "-flag": "Will disable all flaged cmds like eval, exec...etc.",
            "-p": "Will disable all cmds from the given plugin names.",
        },
        "الاستـخـدام": [
            "{tr}rmscmd -all",
            "{tr}rmscmd -flag",
            "{tr}rmscmd -p <plugin names>",
            "{tr}rmscmd <commands>",
        ],
        "مثــال": [
            "{tr}rmscmd -p autoprofile botcontrols i.e, for multiple names use space between each name",
            "{tr}rmscmd ping alive i.e, for multiple commands use space between each name",
        ],
    },
)
async def _(event):  # sourcery no-metrics
    "To disable cmds for sudo users."
    input_str = event.pattern_match.group(2)
    errors = ""
    sudocmds = sudo_enabled_cmds()
    if not input_str:
        return await edit_or_reply(
            event, "__Which command should I disable for sudo users . __"
        )
    input_str = input_str.split()
    if input_str[0] == "الكل":
        zedevent = await edit_or_reply(
            event, "__Disabling all enabled cmds for sudo....__"
        )
        flagcmds = sudocmds
    elif input_str[0] == "-flag":
        zedevent = await edit_or_reply(
            event, "__Disabling all flagged cmds for sudo.....__"
        )
        flagcmds = (
            PLG_INFO["botcontrols"]
            + PLG_INFO["الوقتي"]
            + PLG_INFO["التحديث"]
            + PLG_INFO["الاوامر"]
            + PLG_INFO["هيروكو"]
            + PLG_INFO["الادمن"]
            + PLG_INFO["الحمايه"]
            + PLG_INFO["الاغاني"]
            + PLG_INFO["المجموعه"]
            + PLG_INFO["اعاده تشغيل"]
            + PLG_INFO["تحويل الصيغ"]
            + PLG_INFO["المطور"]
            + PLG_INFO["بوت الحمايه"]
            + ["gauth"]
            + ["greset"]
        )
    elif input_str[0] == "امر":
        zedevent = event
        input_str.remove("امر")
        flagcmds = []
        for plugin in input_str:
            if plugin not in PLG_INFO:
                errors += (
                    f"`{plugin}` __There is no such plugin in your ZThon__.\n"
                )
            else:
                flagcmds += PLG_INFO[plugin]
    else:
        zedevent = event
        flagcmds = []
        for cmd in input_str:
            if cmd not in CMD_INFO:
                errors += f"`{cmd}` __There is no such command in your ZThon__.\n"
            elif cmd not in sudocmds:
                errors += f"`{cmd}` __Is already disabled for sudo users__.\n"
            else:
                flagcmds.append(cmd)
    count = 0
    for cmd in flagcmds:
        if sqllist.is_in_list("sudo_enabled_cmds", cmd):
            count += 1
            sqllist.rm_from_list("sudo_enabled_cmds", cmd)
    result = f"**✾╎تـم تعطيـل التحكـم الكـامل لـ**  `{count}` **امـر 🧑🏻‍💻✅**\n"
    output = (
        result + "**✾╎يتم الان اعـادة تشغيـل بـوت السيد انتظـر 2-1 دقيقـه ▬▭ ...**\n"
    )
    if errors != "":
        output += "\n**- خطــأ :**\n" + errors
    msg = await edit_or_reply(zedevent, output)
    await event.client.reload(msg)


@zedub.zed_cmd(
    pattern="vscmds( -d)?$",
    command=("vscmds", plugin_category),
    info={
        "header": "To show list of enabled cmds for sudo.",
        "description": "will show you the list of all enabled commands",
        "flags": {"-d": "To show disabled cmds instead of enabled cmds."},
        "الاستـخـدام": [
            "{tr}vscmds",
            "{tr}vscmds -d",
        ],
    },
)
async def _(event):  # sourcery no-metrics
    "To show list of enabled cmds for sudo."
    input_str = event.pattern_match.group(1)
    sudocmds = sudo_enabled_cmds()
    clist = {}
    error = ""
    if not input_str:
        text = "**The list of sudo enabled commands are :**"
        result = "**SUDO ENABLED COMMANDS**"
        if len(sudocmds) > 0:
            for cmd in sudocmds:
                plugin = get_key(cmd)
                if plugin in clist:
                    clist[plugin].append(cmd)
                else:
                    clist[plugin] = [cmd]
        else:
            error += "__You haven't enabled any sudo cmd for sudo users.__"
        count = len(sudocmds)
    else:
        text = "**The list of sudo disabled commands are :**"
        result = "**SUDO DISABLED COMMANDS**"
        totalcmds = CMD_INFO.keys()
        cmdlist = list(set(totalcmds) - set(sudocmds))
        if cmdlist:
            for cmd in cmdlist:
                plugin = get_key(cmd)
                if plugin in clist:
                    clist[plugin].append(cmd)
                else:
                    clist[plugin] = [cmd]
        else:
            error += "__You have enabled every cmd as sudo for sudo users.__"
        count = len(cmdlist)
    if error != "":
        return await edit_delete(event, error, 10)
    pkeys = clist.keys()
    n_pkeys = [i for i in pkeys if i is not None]
    pkeys = sorted(n_pkeys)
    output = ""
    for plugin in pkeys:
        output += f"• {plugin}\n"
        for cmd in clist[plugin]:
            output += f"`{cmd}` "
        output += "\n\n"
    finalstr = (
        result
        + f"\n\n**SUDO TRIGGER: **`{Config.SUDO_COMMAND_HAND_LER}`\n**Commands:** {count}\n\n"
        + output
    )
    await edit_or_reply(event, finalstr, aslink=True, linktext=text)


zedub.loop.create_task(_init())



# Copyright (C) 2022 Zed-Thon . All Rights Reserved
@zedub.zed_cmd(pattern="المساعد")
async def cmd(baqir):
    await edit_or_reply(baqir, BaqirDV_cmd)


