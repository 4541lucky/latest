from telethon.sync import TelegramClient
import csv 
from telethon.errors.rpcerrorlist import UsernameInvalidError, ChannelInvalidError, PhoneNumberBannedError
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon import types, utils, errors
import re
from telethon.tl.functions.channels import GetChannelsRequest, GetFullChannelRequest, JoinChannelRequest, InviteToChannelRequest
from telethon.tl.types import PeerChannel
from telethon.tl.functions.contacts import GetContactsRequest
from telethon.tl.functions.messages import AddChatUserRequest

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
deltaxd_ko_credit_nhi_dene_wala_chakka_hai = int(input('From Account No : '))-1
arshwomen_kepas_lund_nhi_hai = int(input('Upto Account No : '))
indexx = 0
global lauda_kartik_malani
lauda_kartik_malani = 0
print('Made By t.me/DeltaXd')
for deltaxd in phlist[deltaxd_ko_credit_nhi_dene_wala_chakka_hai:arshwomen_kepas_lund_nhi_hai]:
    indexx += 1
    print(f'Index : {indexx}')
    phone = utils.parse_phone(deltaxd)
    print(f"Login {phone}")
    client = TelegramClient(f"sessions/{phone}",5772103, '07e52782bd28f933a95d4df8bb5e6e6a')
    client.start(phone)
    try:
        channel = client.get_entity(PeerChannel(id))
    except ValueError:
        if prchk == 'Y':
            client(ImportChatInviteRequest(prlink))
            channel = client.get_input_entity(PeerChannel(id))
            
        elif prchk == 'N':
            client(JoinChannelRequest(prlink))
            channel = client.get_input_entity(PeerChannel(id))
    channelinfo = client(GetFullChannelRequest(channel=channel))
    lauda_kartik_malani = int(channelinfo.full_chat.participants_count)
    print(f'Members: {lauda_kartik_malani}')
    if lauda_kartik_malani >= stop:
        print(f'The Goal Of {stop} Has Been Completed')
        quit()
    contacts = client(GetContactsRequest(hash=0))
    
    deltaadd = 0
    for deltaop in contacts.users:
        deltaadd += 1
        
        try:
            client(InviteToChannelRequest(channel=id, users=[deltaop]))
            print(f'{deltaadd} - {deltaop.id} - DONE')
        except errors.RPCError as e:
            erro = e.__class__.__name__
            print(f'{deltaadd} - {deltaop.id} - {erro}')
            continue
            