
from telethon import TelegramClient, events
import re

# Your Telegram API credentials


chat_username = 'target_chat_username'

# Destination chat where you want to paste the message
andryunin_channel_id = -1001757653881
web3_zapiski_spekulanta_id = -1001803149966
english_chat_andyunin1 = 6068731027
english_chat_andyunin2 = 414371773
english_chat_andyunin_channel_profile_user = -1001864362503
destination_chat_id = -1002005258096
group_to_parse = [-1001757653881, -1001864362503]
from_users_parse = [andryunin_channel_id, web3_zapiski_spekulanta_id, english_chat_andyunin1, english_chat_andyunin2, english_chat_andyunin_channel_profile_user]

# Connect to Telegram
client = TelegramClient('session_name', api_id, api_hash)

@client.on(events.NewMessage(chats=group_to_parse)) #, from_users=[380472185]
async def copy_message(event):
    try:
        # Extract text from the received message
        if(1==1 or event.message.sender_id == None or event.message.sender_id in from_users_parse):
            sender = await event.get_sender()

        # Extract sender's name
            #sender_name = f"{sender.first_name} {sender.last_name}" if sender.last_name else sender.first_name
            # pattern = r'[1-9A-HJ-NP-Za-km-z]{32,44}'

            # matches = re.findall(pattern, event.message.text)
            # bought = False
            # if matches:
            #     await client.send_message(6997957200, matches[0])
            # if(not bought and 'dexscreener' in event.message.text):
            #     await client.send_message(6997957200, event.message.text)
                
            #await client.forward_messages(, event.message)
            # chat_link = 'andryunin_chat'
            # text = 'Андрюнин '
            # if(event.chat_id == -1001864362503):
            #     text += 'eng'
            #     chat_link = 'TradingFoundersLoungebyGotbit'
            # text += '\r\n'
            # text += f'[Линк на сообщение](https://t.me/{chat_link}/{event.id})'
            # text += '\r\n'
            # text += '\r\n'
            # event.message.text = text+event.message.text
            
            await client.send_message(destination_chat_id, event.message)
            print("Message copied successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

# Start the client
client.start(phone_number)

# Run the client's event loop
client.run_until_disconnected()
