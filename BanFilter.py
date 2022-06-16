from telethon.sync import TelegramClient
from telethon import utils
from telethon.errors.rpcerrorlist import PhoneNumberBannedError
import csv
import configparser
print("                                     ONLY FOR EDUCATIONAL AND RESEARCH PURPOSE")

print("                          FOR PURCHASING THIS TOOL PLEASE CONTACT - varun800358@gmail.com" )

print("                                     TELEGRAM MEMBERS ADDER TOOL BY VARUN SHARMA          ")

print("                                     PLEASE JOIN OUR GROUP - @yamrajmemberadder           ")


config = configparser.ConfigParser()
config.read("config.ini")
export_phone = config['Telegram']['export_phone']
export_api_id = config['Telegram']['export_api_id']
export_api_hash = config['Telegram']['export_api_hash']
from_group = config['Telegram']['from_channel']


api_id = int(export_api_id)   
api_hash = str(export_api_hash)
MadeByDeltaXd = []



done = False
with open('phone.csv', 'r') as f:
    str_list = [row[0] for row in csv.reader(f)]


    po = 0
    for unparsed_phone in str_list:
        po += 1
        
       
        phone = utils.parse_phone(unparsed_phone)
        
        print(f"Login {phone}")
        client = TelegramClient(f"sessions/{phone}", api_id, api_hash)
        #client.start(phone)
        client.connect()
        if not client.is_user_authorized():
            try:
                print('This Phone Has Been Revoked')
                delta_xd = str(po)
                delta_op = str(unparsed_phone)
                MadeByDeltaXd.append(delta_op)
                continue
                
            except PhoneNumberBannedError:
                print('Ban')
                delta_xd = str(po)
                delta_op = str(unparsed_phone)
                MadeByDeltaXd.append(delta_op)
                

                continue
            
        

        #client.disconnect()
        print()
    done = True
    print('List Of Banned Numbers')
    print(*MadeByDeltaXd,sep='\n')
    print('Saved In BanNumers.csv')
    with open('BanNumbers.csv', 'w', encoding='UTF-8') as writeFile:
        writer = csv.writer(writeFile, delimiter=",", lineterminator="\n")

        writer.writerows(MadeByDeltaXd)
def autoremove():
    import csv
    import os


    collection = []
    nc = []
    collection1 = []
    nc1 = []
    maind = []

    with open ("phone.csv","r") as infile:
        for line in infile:
            collection.append(line)



    for x in collection:
        mod_x = str(x).replace("\n","")
        nc.append(mod_x)


    with open ("BanNumbers.csv") as infile, open("outfile.csv","w") as outfile:
        for line in infile:
            outfile.write(line.replace(",",""))


    with open ("outfile.csv","r") as outfile:
        for line1 in outfile:
            collection1.append(line1)


    for i in collection1:
        mod_i = str(i).replace("\n","")
        nc1.append(mod_i)


    unique = set(nc)
    unique1 = set(nc1)

    itd = unique.intersection(unique1)

    for x in nc:
        if x not in itd:
            
            maind.append(x)


    with open('unban.csv', 'w', encoding='UTF-8') as writeFile:
        writer = csv.writer(writeFile, lineterminator="\n")
        writer.writerows(maind)
        
        


    with open ("unban.csv") as last, open("phone.csv","w") as final:
        for line3 in last:
            mod_i = str(line3).replace("\n","")
            final.write(mod_i)

    os.remove("phone.csv")
    os.rename("unban.csv","phone.csv")
    print("Done,All Banned Number Have Been Removed")

def dellst():
    import csv
    import os

    with open ("phone.csv") as infile, open("unban.csv","w") as outfile:
        for line in infile:
            outfile.write(line.replace(",",""))

    os.remove("phone.csv")
    os.rename("unban.csv","phone.csv")

    print("complete")

autoremove()
dellst()


    

    

input("Done!" if done else "Error!")
