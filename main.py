from operator import mod
from pickle import ADDITEMS
from secrets import choice
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors import FloodWaitError
from telethon import functions, types
from time import sleep
import random
import os
import modules
import cfg


filenames = next(os.walk("sessions"), (None, None, []))[2]
# random.shuffle(filenames)
def imulate(filenames):
    adverts = cfg.ADVERTS.copy()
    random.shuffle(adverts)
    while True:
        for session in filenames:
            try:
                if len(adverts) == 0:
                    adverts = cfg.ADVERTS.copy()
                    random.shuffle(adverts)
                    print(len(adverts))
                advert = adverts.pop(0)
                with modules.check_session("sessions/" + session) as client:
                    modules.send_advert(client, advert)
                    print(session + " sended")
            except FloodWaitError:
                os.rename("sessions/"
                         + session,"bunned/" + session)
            except Exception as e:
                print(session + ": " + str(e))
                if not cfg.DEBUGGING:
                    if("banned" in str(e)):
                        os.rename("sessions/"
                         + session,"bunned/" + session)
                    elif("authorized" in str(e)):
                        os.rename("sessions/" + session,"unauthorized/" + session)
                    elif("write in this" in str(e)):
                        os.rename("sessions/" + session,"sessionsall/" + session)
            
            sleep(10 + random.randint(0,25))
        filenames = next(os.walk("sessions"), (None, None, []))[2]
        # random.shuffle(filenames)


modules.join_all(next(os.walk("sessionsall"), (None, None, []))[2])
# imulate(filenames)