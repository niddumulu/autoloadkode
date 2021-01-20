import time
import os

from telethon import TelegramClient, sync, events, utils
api_id = 682610
api_hash = '030132b51d598e464419ccee7f20212d'
client = TelegramClient('useravatar', api_id, api_hash).start()

seconds = int(0)
minutes = int(0)

run = "dia"
while run.lower() == "dia":
    if seconds == 3:
        for message in client.iter_messages('niddumulu', limit=1):
            (utils.get_display_name(message.sender), message.message)
            pesannidd = (message.message)
            #print (pesan)
            varilkan = "varilkan"
            client.send_message('resiavatarbot', varilkan)

    if seconds == 25:
       for message in client.iter_messages('resiavatarbot', limit=1):
          (utils.get_display_name(message.sender), message.message)
          pesan = (message.message)
          #print (pesan)

          client.send_message('MissZiziBot', pesan)

    if seconds == 45:
      for message in client.iter_messages('MissZiziBot', limit=1):
          (utils.get_display_name(message.sender), message.message)
          pesanhasil = (message.message)
          #print (pesanhasil)
          client.send_message('saveBigdatabot', pesanhasil)
    
    if seconds == 59:
        
       run = "diaa"
    os.system('clear')
    seconds = (seconds + 1)
    print(seconds)
    time.sleep(1)
