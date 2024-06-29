#IMPORTED LIBRARYS  
from sched import scheduler
import discord
import requests
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import os
import random

#IMPORTANT VARIABLES
NEWS_API_KEY = 'My news api key here'
DISCORD_TOKEN = 'My discord bot token here'
CHANNEL_ID = 123456789012345678 #My channel ID of my discord server

#Password Shuffler handler function
def Shuffle(String):
    templist = list(String)
    random.shuffle(templist)
    return "".join(templist)

#Character And Integer Randomizer section
upperCaseLetter1 = chr(random.randint(65,90))  # Generate a random uppercase letter in ASCII
upperCaseLetter2 = chr(random.randint(65,90)) 
lowerCaseLetter1 = chr(random.randint(97,122))
lowerCaseLetter2 = chr(random.randint(97,122))

password = upperCaseLetter1 + upperCaseLetter2 + lowerCaseLetter1 + lowerCaseLetter2
password = Shuffle(password)


intents = discord.Intents.default()
intents.message_contend = True #Enables the bot to process message contend

client = discord.Client(intents=intents) #The Client class represents a connection to Discord.
intents = AsyncIOScheduler()

#Make sure to replace this with the actuall url and api key
def get_tech_news():
    url = (
        ' es?'
           'category=technology&'
           f'apiKey={NEWS_API_KEY}'
    )
    Web_Response = requests.get(url)
    news_data = Web_Response.json()

    if news_data['status'] == 'ok':
        articles = news_data['articles'][:5] #Gets the top 5 articles
        news_message = 'Latest Tech News:\n'
        for article in articles:
            news_message += f"{article['title']}\n{article['url']}\n\n"
            return news_message
        return "Failed to fetch news today: Sorry!"

@client.event
async def on_ready(): # bot has successfully connected to Discord and is ready. 
    print(f'We have logged in in as {client.user}')
    
@client.event
async def on_message(message):
    if message.author == client.user: #checks if the message was sent by the bot itself. If it was, the function returns early and does nothing.
        return
    
    if message.contend.startswith("!hello"):
        await message.channel.send("Hello you!")

#This automatically sends the news message in a specific channel every 1 hour
@scheduler.scheduled_job('interval', hour=1 )
async def send_news():
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        news_message = get_tech_news()
        await channel.send(news_message)

async def on_request_password():
    channel = client.get_channel(CHANNEL_ID)
    if channel.message.startswith("!Password"):
        channel.send("This is your requested password /n")
        channel.send(password)
        
        
client.run(DISCORD_TOKEN) #connects it to Discord using the provided token
print("DISCORD BOT IS RUNNING~!")