#!/usr/bin/python3

# made by Pure luck, compatible with teeworlds 0.7

# configure it:
channel_id=0 # an integer value
bot_api_key="" # a string

# don't change anything below unless you know what you're doing

import discord, asyncio, sys, re, os, time
from discord.ext import commands

last_msg = {}

# try to switch buffering to text mode per line
inin = os.fdopen(sys.stdin.fileno(), 'r', buffering=1)

client = commands.Bot(";")
@client.event

async def on_ready():
  print("Logged in as " + str(client.user))
  channel = client.get_channel(channel_id)
  await channel.send("> Bot restarted")
  time.sleep(1) # we don't want to streess discord servers
  for line in inin:
    print("< " + line) # for debug purposes
    if "chat" in line:
      m = p.match(line)
      if m:
        username = m.group(1)
        text = m.group(2)
        s = "**" + m.group(1) + "**: " + m.group(2)
        print(">> " + s) # for debug purposes
        if (last_msg.get(username) and last_msg[username] == text):
          print("duplicated") # simple anti-flood
          continue
        await channel.send(s)
        last_msg[username] = text

p = re.compile('^\[\d*-\d*-\d* \d*:\d*:\d*\]\[chat\]: \d*:\d*:([^:]+): ([^/?].*)$')

client.run(bot_api_key)

print('Bot exited')
