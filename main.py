from random import randint
import discord
import os
from dotenv import load_dotenv

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    if message.content == "$test":
        await message.channel.send(pingMessage())


def greetings():
    greetings = ["Hello", "Howdy", "Bonjour", "Heya", "Wassup"]
    return greetings[randint(0, 4)]

def pingMessage():
    return greetings() + " coders, remember to do you commits today!"

load_dotenv()
client.run(os.getenv('TOKEN'))