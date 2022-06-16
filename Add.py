from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser, PeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError, ChatWriteForbiddenError, UserAlreadyParticipantError
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.functions.channels import GetFullChannelRequest, JoinChannelRequest
from telethon import types, utils, errors, functions
import configparser
import sys
import csv
from csv import reader
import traceback
import time
import random
from telethon.sessions import StringSession
from telethon.errors.rpcerrorlist import FloodWaitError

delta = int(input("In Which Account You Want To Add Contacts\nEnter: "))

config = configparser.ConfigParser()
config.read("config.ini")
lastname = config['Telegram']['last_name']
from_group = config['Telegram']['from_channel']
    
with open('phone.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    list_of_rows = list(csv_reader)    
    row_number = delta
    col_number = 1
    value = list_of_rows[row_number - 1][col_number - 1]
    
with open('api.csv', 'r') as api_obj_id:
    csv_reader = reader(api_obj_id)
    list_of_rows = list(csv_reader)
    row_number = delta
    col_number = 1
    deltaop = list_of_rows[row_number - 1][col_number - 1]
    
with open('api.csv', 'r') as hash_obj:
    csv_reader = reader(hash_obj)
    list_of_rows = list(csv_reader)  
    row_number = delta
    col_number = 2
    deltaxd = list_of_rows[row_number - 1][col_number - 1]
    
api_id = int(deltaop)
api_hash = str(deltaxd)
pphone = value
print("Made By t.me/deltaxd")


global status
status = "DO"


def autos():
    
    
    phone = utils.parse_phone(pphone)

    client = TelegramClient(f"sessions/{phone}", api_id, api_hash)

    client.connect()
    if not client.is_user_authorized():
        print('some thing has changed')
        client.send_code_request(phone)
        client.sign_in(phone, input    ('Enter the code: '))


    input_file = 'data.csv'
    users = []
    with open(input_file, encoding='UTF-8') as f:
        rows = csv.reader(f, delimiter=",", lineterminator="\n")
        next(rows, None)
        for row in rows:
            user = {}
            user['srno'] = row[0]
            user['username'] = row[1]
            user['id'] = int(row[2])
        #user['access_hash'] = int(row[2])
            user['name'] = row[3]
            users.append(user)

    startfrom = int(input("Start From = "))
    endto = int(input("End To = "))


    
    it = 0
    for user in users:
        if (int(startfrom) <= int    (user['srno'])) and (int(user['srno']) <= int(endto)):
            try:
                it += 1
                
                name = user['name']
                tesp = client.get_participants(from_group, search=name)
                user = tesp[0]
            
                    
                
                client(functions.contacts.AddContactRequest(
                    id=user,
                    first_name=str(name),
                    last_name=' ',
                    phone='gdf',
                    add_phone_privacy_exception=True))
                status = f'{it} - done'
                

                
            except errors.RPCError as e:
                status = e.__class__.__name__

            except FloodWaitError as e:
                print(e.seconds)
                time.sleep(e.seconds)
        
    
        

            except:
                traceback.print_exc()
                print("Unexpected Error")
                continue
       
            print(f"{status}")
            #print(f"ADDING {user['name']} TO {channel_username} TOTAL: {countt} - {status}")
        elif int(user['srno']) > int(endto):
            print("Members Added Successfully!")
            stat = input('Done!\nChoose From Below:\n\n1 - Repeat The Script\nOR Just Hit Enter To Quit\n\nEnter: ')
            if stat == '1':
                autos()
            else:
                quit()
             
autos()    

