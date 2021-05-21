import os
from http.server import BaseHTTPRequestHandler
from urllib import parse
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from dotenv import load_dotenv

load_dotenv()



# async def main():
#     try:
#         # Replace the xxxxx in the following line with the full international mobile number of the contact
#         # In place of mobile number you can use the telegram user id of the contact if you know
#         ret_value = await client.send_message("xxxxxxxxxxx", 'Hi')
#     except Exception as e:
#         print(f"Exception while sending the message - {e}")
#     else:
#         print(f"Message sent. Return Value {ret_value}")

# with client:
#     client.loop.run_until_complete(main())
    
class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        s = self.path
        
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        try:
            client = TelegramClient(StringSession(os.getenv("STRING_TOKEN")), os.getenv("API_ID"), os.getenv("API_HASH"))
            client.start()
            messages = []
            dic = dict(parse.parse_qsl(parse.urlsplit(s).query));
            if "id" in dic:
                message = "Hello, " + dic["id"] + "!"
                channel_username = dic["id"]
                for msg in client.get_messages(channel_username, limit=10):
                    print(msg.message)
                    messages.append(msg.message)
                message = messages
            else:
                message = "Hello, stranger!"
            self.wfile.write(message.encode())
        except Exception as e:
            message = "Exception while starting the client"
            print(f"Exception while starting the client - {e}")
        else:
            print("Client started")
        return
