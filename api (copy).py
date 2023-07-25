from googleapiclient.discovery import build
from urllib.parse import urlparse, parse_qs
import os
from datetime import datetime
import time
from twitch import TwitchClient
import asyncio
from twitchio.ext import commands
import aiomysql

# Set up the API client
api_key = '' #Youtube api key
youtube = build('youtube', 'v3', developerKey=api_key)

# Input the URL of the specific live stream
live_stream_url = input("Enter the URL of the yt live stream: ")
latest_chatmessagetime = 0

# Extract the video ID from the URL
parsed_url = urlparse(live_stream_url)
video_id = parse_qs(parsed_url.query)['v'][0]

# Get live broadcasts for the video ID
request = youtube.videos().list(
    part='snippet,liveStreamingDetails',
    id=video_id
)
response = request.execute()

# Extract broadcast information
video = response['items'][0]
broadcast_id = video['liveStreamingDetails']['activeLiveChatId']
datetie = 0

async def send_twitch_message(message):
    server = "irc.chat.twitch.tv"
    port = 6667
    nick = "" #your twitch username
    token = "" # Generate this oauth token from Twitch developer dashboard
    reader, writer = await asyncio.open_connection(server, port)

    # Authenticate with the Twitch server
    writer.write(f"PASS {token}\r\n".encode())
    writer.write(f"NICK {nick}\r\n".encode())
    await writer.drain()
    channel = "#" #the name of the streamer whos chat you wish to send to, preceded by a #
    
    # Join the channel
    writer.write(f"JOIN {channel}\r\n".encode())
    await writer.drain()

    # Send the message
    writer.write(f"PRIVMSG {channel} :{message}\r\n".encode())
    await writer.drain()

    # Leave the channel
    writer.write(f"PART {channel}\r\n".encode())
    await writer.drain()
    
    # Close the connection
    writer.write(b"QUIT\r\n")
    await writer.drain()
    writer.close()
    await writer.wait_closed()

while True:
    print(f"waiting (dont spam youtube api)")
    time.sleep(10)
    request = youtube.liveChatMessages().list(
        part='snippet',
        liveChatId=broadcast_id,
        maxResults=10000,
    )
    response = request.execute()

    #Extract chat messages
    messages = response['items']
    print(f"")
    print(f"attempting to identify commands")

    time.sleep(1)
    for message in messages:
        # Extract relevant information from the message
        message_text = message['snippet']['displayMessage']
        published_at = message['snippet']['publishedAt']

        if message_text.startswith("!"):
            datetie = datetime.strptime(published_at, '%Y-%m-%dT%H:%M:%S.%f%z')
            formatted = datetie.strftime("%d%H%M%S")
            if latest_chatmessagetime == 0:
                print(message_text, formatted)
                latest_chatmessagetime = formatted
                message = 'Your message here'
                asyncio.run(send_twitch_message(message_text))
                       
            elif formatted > latest_chatmessagetime:
                print(message_text, formatted)
                latest_chatmessagetime = formatted
                message = 'Your message here'
                asyncio.run(send_twitch_message(message_text))
            

