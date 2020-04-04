import os

import discord
import random
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    chui_string = [
        'you dump, Vu cko',
        'Vu cko, suot ngay choi game',
        (
            'Vu dot lam, dung choi game voi no!!'
        ),
    ]

    now = datetime.now()

    current_time = now.strftime("%H:%M")
    
    if '@nntien' in message.content:
        response = random.choice(chui_string)
        await message.channel.send(response)
    elif current_time == '23:30':
        await message.channel.send("khuya roi, giai tan, di ngu thoi!!!")


client.run(TOKEN)