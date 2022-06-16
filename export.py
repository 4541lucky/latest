from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError, ChatWriteForbiddenError
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon import types, utils
import sys
import csv
import configparser
import traceback
import time
from telethon.sessions import StringSession

config = configparser.ConfigParser()
config.read("config.ini")
export_phone = config['Telegram']['export_phone']
export_api_id = config['Telegram']['export_api_id']
export_api_hash = config['Telegram']['export_api_hash']
from_group = config['Telegram']['from_channel']
last_seen = config['Telegram']['last_seen']
last = int(last_seen)


api_id = int(export_api_id)   
api_hash = str(export_api_hash)

phone = int(export_phone)


client = TelegramClient(f"sessions/{phone}", api_id, api_hash)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))

print('Fetching Members...')
all_participants = []

#enter target group or channel
target = from_group

all_participants = client.get_participants(target)
    

print('Saving In file...')
with open("data.csv","w",encoding='UTF-8') as f:#Enter your file name.
    writer = csv.writer(f, delimiter=",", lineterminator="\n")
    writer.writerow(['sr. no.','username', 'user id', 'name', 'group', 'Status'])
    i = 0
    for user in all_participants:
        nam = utils.get_display_name(user)
        status = 31634268763763

        i += 1
        if user.username:
            username = user.username
        else:
            username = ""
        if isinstance(user.status, types.UserStatusOnline):
            status = 1
        
        elif isinstance(user.status, types.UserStatusOffline):
            if time.time()-(user.status.was_online).timestamp() <= last:
                status = 2
            else:
                status = 31634268763763
        
        
        writer.writerow([i,username, user.id, nam, target , status])
print('Members Scraped Successfully.')

