from operator import mod
from pickle import ADDITEMS
from secrets import choice
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from telethon import functions, types
from time import sleep
import random
import os
import modules
import cfg

filenames = next(os.walk("off"), (None, None, []))[2]
for session in filenames:
    try:
        modules.check_session("off/" + session)
    except Exception as e:
       print(session + ": " + str(e))
       if not cfg.DEBUGGING:
           if("banned" in str(e)):
               os.rename("off/"
                + session,"bunned/" + session)
           elif("authorized" in str(e)):
               os.rename("off/" + session,"unauthorized/" + session)
           elif("write in this" in str(e)):
               os.rename("off/" + session,"sessionsall/" + session)
    sleep(1)