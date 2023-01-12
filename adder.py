from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError, UserChannelsTooMuchError, UserNotMutualContactError, ChatAdminRequiredError, \
UserKickedError, FloodWaitError, UserBannedInChannelError
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.sessions import StringSession
import traceback
import random
import os
import cfg
import asyncio
import pandas as pd

NUN_OF_INVITES = 50
SLEEP_TIME_1 = 100
SLEEP_TIME_2 = 100
# USERS = []
# with open(r"ListGood.csv", encoding='UTF-8') as f:  #Enter your file name
#     rows = csv.reader(f,delimiter=",",lineterminator="\n")
#     next(rows, None)
#     for row in rows:
#         user = {}
#         user['username'] = row[0]
#         # user['id'] = int(row[1])
#         # user['access_hash'] = int(row[2])
#         # user['name'] = row[3]
#         USERS.append(user)
USERS = pd.read_csv("ListGood.csv", encoding='UTF-8').iterrows()
total = 0
# if "+" in cfg.GROUP_LINK:cfg.GROUP_LINK = cfg.GROUP_LINK[1:]
# print(type(next(USERS)[1]['username']))
# input("Нажмите Enter для запуска...")

async def invite(client:TelegramClient, session):
    await client.start()
    for i in range(NUN_OF_INVITES):
        user = next(USERS)[1]
        # if n % 45 == 0:
        #     client.disconnect()
        #     return True
        try:
            await asyncio.sleep(2)
            try: 
                print(str(i)  + " - " + session + " - Добавлен Пользователь: {}".format(user['username']))
            except: None
             
            # if mode == 1:
            #     if user['username'] == "":
            #         continue
            #     user_to_add = client.get_input_entity(user['username'])
            # elif mode == 2:
            # user_to_add = InputPeerUser(user['id'], user['access_hash'])
            if type(user['username']) == float:
                i-=1
                continue
            # await client(InviteToChannelRequest(1747061617, [("@" + user['username'])]))
            await client(InviteToChannelRequest("                                           ", [("@" + user['username'])]))
            await asyncio.sleep(random.randrange(60, 80))
        except PeerFloodError:
            print(session + " - Flood Error From Telegram. 'Ошибка Флуда'")
            # await client.disconnect()
            # os.rename("sessions/" + session,"flooded/" + session)
            return
        except FloodWaitError:
            print(session + " - Flood Error From Telegram. 'Ошибка Флуда'")
            await client.disconnect()
            # os.rename("sessions/" + session,"flooded/" + session)
            return
        except UserPrivacyRestrictedError:
            print(session + " - Настройки Пользователя не позволяют Добавить его. Пропускаю")
            i-=1
            await asyncio.sleep(20)
        except UserChannelsTooMuchError:
            print(session + " - Пользователь имеет слишком много каналов. Пропускаю")
            i-=1
            await asyncio.sleep(20)
        except UserNotMutualContactError:
            print(session + " - Пользователь не в контакте. Пропускаю")
            i-=1
            await asyncio.sleep(20)
        except ChatAdminRequiredError:
            print(session + " - Необходимы права Администратора. Пропускаю")
            i-=1
            await asyncio.sleep(20)
        except UserKickedError:
            print(session + " - Пользователь заблокирован. Пропускаю")
            i-=1
            await asyncio.sleep(20)
        except ValueError:
            print(session + " - Не удалось добавить пользователя. Пропускаю")
            i-=1
            await asyncio.sleep(20)
        except UserBannedInChannelError:
            print(session + " - Пользователь забанен в канале. Пропускаю")
            i-=1
            await asyncio.sleep(20)
        except:
            # if("can't" in str(e)):
            #     await client.disconnect()
            #     os.rename("sessions/" + session,"strange/" + session)
            #     return
            # i-=1
            # traceback.print_exc()
            # await asyncio.sleep(1)
            # print(session + " - Произошла Ошибка! Продолжу через 5 секунд...! : " + str(e))
            await asyncio.sleep(20)




with open("proxies.txt","r",encoding="utf-8") as f:
    proxies = f.readlines(0)

    
cors = []
async def main():
    n = 0
    sessions = next(os.walk("sessions"), (None, None, []))[2]
    for session in sessions:
        n += 1
        proxy=proxies.pop(0)
        try:
            if session.endswith(".txt"):
                with open("sessions/" + session, "r") as f:
                    session_string = f.read()
                client_session = StringSession(session_string)
            else:
                client_session = "sessions/" + session
            cors.append(invite(TelegramClient(client_session, cfg.API_ID, cfg.API_HASH, proxy={
                'proxy_type': 'socks5',
                'addr': proxy.split("@")[1].split(":")[0],
                'port': int(proxy.split("@")[1].split(":")[1]),
                'username': proxy.split("@")[0].split(":")[0],
                'password': proxy.split("@")[0].split(":")[1]
            }), session))
        except Exception as e:
            print(str(e))
        try: print(str(n) + " - " + proxy)
        except: None
    await asyncio.wait(cors)
    # await asyncio.gather(cors)
asyncio.run(main())