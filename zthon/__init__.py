import signal
import sys
import time
import heroku3
from .Config import Config
from .core.logger import logging
from .core.session import zedub
from .helpers.utils.utils import runasync
from .sql_helper.globals import addgvar, delgvar, gvarstatus

__version__ = "3.1.1"
__license__ = "GNU Affero General Public License v3.0"
__author__ = "Repthon <https://github.com/TOPTH0N/FilesSource1>"
__copyright__ = f"Repthon Copyright (C) 2020 - 2021  {__author__}"

zedub.version = __version__
zedub.tgbot.version = __version__
LOGS = logging.getLogger("𝐒𝐘𝐍𝐓𝐑𝐀𝑳")
bot = zedub

StartTime = time.time()
repversion = "3.1.3"


def close_connection(*_):
    print("تم اغلاق اتصال السورس.")
    runasync(zedub.disconnect())
    sys.exit(143)


signal.signal(signal.SIGTERM, close_connection)


if Config.UPSTREAM_REPO == "Rep":
    UPSTREAM_REPO_URL = "https://github.com/rogerpq/Repthon-_-"
else:
    UPSTREAM_REPO_URL = Config.UPSTREAM_REPO

if Config.PRIVATE_GROUP_BOT_API_ID == 0:
    if gvarstatus("PRIVATE_GROUP_BOT_API_ID") is None:
        Config.BOTLOG = False
        Config.BOTLOG_CHATID = "me"
    else:
        Config.BOTLOG_CHATID = int(gvarstatus("PRIVATE_GROUP_BOT_API_ID"))
        Config.PRIVATE_GROUP_BOT_API_ID = int(gvarstatus("PRIVATE_GROUP_BOT_API_ID"))
        Config.BOTLOG = True
else:
    if str(Config.PRIVATE_GROUP_BOT_API_ID)[0] != "-":
        Config.BOTLOG_CHATID = int("-" + str(Config.PRIVATE_GROUP_BOT_API_ID))
    else:
        Config.BOTLOG_CHATID = Config.PRIVATE_GROUP_BOT_API_ID
    Config.BOTLOG = True

if Config.PM_LOGGER_GROUP_ID == 0:
    if gvarstatus("PM_LOGGER_GROUP_ID") is None:
        Config.PM_LOGGER_GROUP_ID = -100
    else:
        Config.PM_LOGGER_GROUP_ID = int(gvarstatus("PM_LOGGER_GROUP_ID"))
elif str(Config.PM_LOGGER_GROUP_ID)[0] != "-":
    Config.PM_LOGGER_GROUP_ID = int("-" + str(Config.PM_LOGGER_GROUP_ID))

try:
    if Config.HEROKU_API_KEY is not None or Config.HEROKU_APP_NAME is not None:
        HEROKU_APP = heroku3.from_key(Config.HEROKU_API_KEY).apps()[
            Config.HEROKU_APP_NAME
        ]
    else:
        HEROKU_APP = None
except Exception:
    HEROKU_APP = None


# Global Configiables
COUNT_MSG = 0
USERS = {}
COUNT_PM = {}
LASTMSG = {}
CMD_HELP = {}
ISAFK = False
AFKREASON = None
CMD_LIST = {}
SUDO_LIST = {}
# for later purposes
INT_PLUG = ""
LOAD_PLUG = {}

# Variables
BOTLOG = Config.BOTLOG
BOTLOG_CHATID = Config.BOTLOG_CHATID
PM_LOGGER_GROUP_ID = Config.PM_LOGGER_GROUP_ID
