from time import sleep
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from telethon import functions, types
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.functions.account import SetPrivacyRequest
from telethon.tl.types import InputPrivacyKeyPhoneNumber,\
    InputPrivacyValueDisallowAll
import os
import cfg
import random
import datetime

with open("sessions.txt", "r") as f:
    sessions = f.readlines()
for session in sessions:
    session = session.strip()
    client = TelegramClient(StringSession(session), cfg.API_ID, cfg.API_HASH)
    client.connect()
    num = client.get_me().phone
    if client.is_user_authorized():
        with open("sessionsall/" + num + ".txt", "w") as f:
            f.write(session)
    client.disconnect()


