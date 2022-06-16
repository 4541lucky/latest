from telethon.sync import TelegramClient
import csv 
from telethon.errors.rpcerrorlist import UsernameInvalidError, ChannelInvalidError, PhoneNumberBannedError
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon import types, utils, errors
import re
import time

from telethon import functions
from telethon.tl.functions.channels import GetChannelsRequest, GetFullChannelRequest, JoinChannelRequest, InviteToChannelRequest
from telethon.tl.types import PeerChannel
from telethon.tl.functions.contacts import GetContactsRequest
from telethon.tl.functions.messages import AddChatUserRequest

re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"



print("     WELCOME ADDERMANNU DOOT")

print("     MEMBER ADDING AND FOR SOFTWARE - 7060524812  " )

print("     TELEGRAM MEMBERS ADDER TOOL BY ADDERMANNU DOOT        ")

print(re+"##################"+gr+"#####################"+cy+"#############################")                                           

phonecsv = input('Enter Accounts List : ')

with open(f'{phonecsv}.csv', 'r') as f:
    global phlist
    phlist = [row[0] for row in csv.reader(f)]
print('Total account: '+str(len(phlist)))

prchk = input('Enter Y if group has private link else N (Y/N) : ')
if prchk == 'Y':
    id = int(input('Enter Group Id : '))
    prlink = input('Enter Link : ')
elif prchk == 'N':
    id = int(input('Enter Group Id : '))
    prlink = input('Enter Group Username : ')
stop = int(input('Enter Stop : '))
start_from = int(input('start_from Account No : '))-1
upto = int(input('Upto Account No : '))
indexx = 0
global lostboyjourney
lostboyjourney = 0
print('Made By t.me/lostboyjourney')
for pythondeveloper in phlist[start_from:upto]:
    indexx += 1
    
    phone = utils.parse_phone(pythondeveloper)
    print(f"Login {phone}")
    client = TelegramClient(f"sessions/{phone}", 5772103 , '07e52782bd28f933a95d4df8bb5e6e6a')
    client.start(phone)
    print(f'Index : {indexx}')
    try:
        channel = client.get_entity(PeerChannel(id))
    except ValueError:
        if prchk == 'Y':
            client(ImportChatInviteRequest(prlink))
            channel = client.get_input_entity(PeerChannel(id))
#This Script Is Made My T.Me/lostboyjourney           
        elif prchk == 'N':
            client(JoinChannelRequest(prlink))
            channel = client.get_input_entity(PeerChannel(id))
    channelinfo = client(GetFullChannelRequest(channel=channel))
    lostboyjourney = int(channelinfo.full_chat.participants_count)
    print(f'Members: {lostboyjourney}')
    if lostboyjourney >= stop:
        print(f'The Goal Of {stop} Has Been Completed')
        quit()
    
    members = client(GetContactsRequest(hash=0))
    user_to_add = members.users 
    countcon = len(user_to_add)
    print(f'Total : {countcon}')
    
    batchcount = 0
    lol = 0
    while batchcount < countcon:
        semen = [delta for delta in user_to_add[0:100]]
        #print(f'Left {len(lit)}')
        try:
            client(functions.channels.InviteToChannelRequest(
                channel = id,
                users=semen
                ))
        #print(f'Added : {added}')
            batchcount += 10
            for i in range(0,10):
                try:
                    del user_to_add[i]
                except Exception as D:
                    continue
            print(f'BATCH: {batchcount}')
        except errors.RPCError as e:
            erro = e.__class__.__name__
            print(str(erro))
            break
            #continue
        





        
        
