import discord
import os
import random
from datetime import datetime

def read_token():
    with open('token', 'r') as f:
        lines = f.readlines()
        return lines[0].strip()

token = read_token()

client = discord.Client()

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
    elif 'raise-exception' in message.content :
        raise discord.DiscordException



client.run(token)