from telethon import TelegramClient, sync, events, utils
api_id = 682610 
api_hash = '030132b51d598e464419ccee7f20212d' 
client = TelegramClient('anon', api_id, api_hash).start()
@client.on(events.NewMessage()) 
async def handler(event): 
     sender = await event.get_sender()
     name = utils.get_display_name(sender)
     print(name, 'said', event.text, '!')     
try :
      client.run_until_disconnected()
finally: 
      client.disconnect()
