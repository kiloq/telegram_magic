from telethon.sync import TelegramClient
from telethon.tl.functions.photos import UploadProfilePhotoRequest
import random
from time import sleep
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon import functions, types
from telethon import TelegramClient
from telethon.tl.functions.account import SetPrivacyRequest
from telethon.tl.types import InputPrivacyKeyPhoneNumber,\
    InputPrivacyValueDisallowAll
import os
import random

def change_ava(name):
    client = TelegramClient("sessions/" + name, "28854260", "ec674a5adc0cf93bcce37b04eb0bcb30")
    client.connect()
    if not client.is_user_authorized():
        client.disconnect()
        raise Exception("Not authorized")
    client(UploadProfilePhotoRequest(
        client.upload_file("1.jpg")
    ))
    client.disconnect()

def join(name, group):
    client = TelegramClient("sessions/" + name, "28854260", "ec674a5adc0cf93bcce37b04eb0bcb30")
    client.connect()
    if not client.is_user_authorized():
        client.disconnect()
        raise Exception("Not authorized")
    
    client(ImportChatInviteRequest(group))
    result = client(functions.account.UpdateNotifySettingsRequest(
    peer=group,
    settings=types.InputPeerNotifySettings(
        show_previews=False,
        sound=types.NotificationSoundNone(),
        silent = True)))
    print(result)
    client.edit_folder(group, 1)

    client(SetPrivacyRequest(key=InputPrivacyKeyPhoneNumber(),rules=[InputPrivacyValueDisallowAll()]))
    client.disconnect()
