from time import sleep
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon import functions, types
from telethon import TelegramClient
from telethon.tl.functions.account import SetPrivacyRequest
from telethon.sessions import StringSession
from telethon.tl.types import InputPrivacyKeyPhoneNumber,\
    InputPrivacyValueDisallowAll
import os
import cfg
import random
import datetime

def check_session(session_path):
    if session_path.endswith(".txt"):
        with open(session_path, "r") as f:
            session = f.read()
        client = TelegramClient(StringSession(session), api_id=cfg.API_ID, api_hash=cfg.API_HASH)
    else: client = TelegramClient(session_path, api_id=cfg.API_ID, api_hash=cfg.API_HASH)
    client.connect()
    if not client.is_user_authorized():
        client.disconnect()
        raise Exception("Not authorized")
    else:
        return client

def join_all(filenames):
    print(filenames)
    for session in filenames:
        try:
            with check_session("sessionsall/" + session) as client:
                if '+' in cfg.GROUP_LINK: client(client(ImportChatInviteRequest(cfg.GROUP_LINK[1:])))
                else: client(JoinChannelRequest(cfg.GROUP_LINK))

                result = client(functions.account.UpdateNotifySettingsRequest(
                peer=cfg.GROUP_LINK,
                settings=types.InputPeerNotifySettings(
                    # show_previews=False,
                    mute_until=datetime.date(2030, 12, 4),
                    # sound=types.NotificationSoundNone(),
                    # silent = False
                    )))
                print(result)
                result = client.edit_folder(cfg.GROUP_LINK, 1)
                print(result)
                client(SetPrivacyRequest(key=InputPrivacyKeyPhoneNumber(),rules=[InputPrivacyValueDisallowAll()]))

                print(session + " joined")
            client.disconnect()
            print("Move to ok")
            os.rename("sessionsall/" + session,"sessions/" + session)
        except Exception as e:
            print(session + ": " + str(e))
            if not cfg.DEBUGGING:
                if("banned" in str(e)):
                    os.rename("sessionsall/" + session,"bunned/" + session)
                else:
                    os.rename("sessionsall/" + session,"unauthorized/" + session)
        
        sleep(2)

def send_advert(client, advert):
    try:
        client.send_message(cfg.GROUP_LINK,advert)
        # print(client.get_me().stringify() + " sended")
        client.disconnect()
    except Exception as e:
        raise e


