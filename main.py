import discord
from discord.ext import commands
from discord.ext import tasks
import asyncio
import os


app = commands.Bot("!")



TOKEN = os.getenv("TOKEN")
VOICEID = int("901037840698331146")


@app.event
async def ready():
	channel = app.get_channel(id=VOICEID)
	await channel.connect()




loop = asyncio.get_event_loop()
loop.create_task(app.start(TOKEN, bot=False))
loop.run_forever()
