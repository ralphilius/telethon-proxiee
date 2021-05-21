import os
from http.server import BaseHTTPRequestHandler
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from dotenv import load_dotenv

load_dotenv()

try:
    client = TelegramClient(StringSession(os.getenv("STRING_TOKEN")), os.getenv("API_ID"), os.getenv("API_HASH"))
    client.start()
except Exception as e:
    print(f"Exception while starting the client - {e}")
else:
    print("Client started")

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
        dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        if "name" in dic:
            message = "Hello, " + dic["id"] + "!"
        else:
            message = "Hello, stranger!"
        self.wfile.write(message.encode())
        return
