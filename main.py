#author github.com/kometarou1145
import discord
import threading
from utils import AppUtils

client = discord.Client()
bot=True

token = 'Your bot token'

@client.event
async def on_ready():
    print("ready")

@client.event
async def on_message(message):
    args = message.content.split()[1:]

    if message.content.lower().startswith(".setup"):
        if len(args) != 7: return

        channel_name = str(args[0])
        send_message = str(args[1])
        channel_amount = int(args[2])
        send_amount = int(args[3])
        delete_delay = float(args[4])
        create_delay = float(args[5])
        send_delay = float(args[6])

        channel_ids = [channel.id for channel in client.get_all_channels()]
        guild_id = message.guild.id

        delete = threading.Thread(
            target=AppUtils.delete_channels,
            args=(
                channel_ids,
                token,
                delete_delay,
                bot
            )
        )

        delete.start()

        create = threading.Thread(
            target=AppUtils.create_channels,
            args=(
                guild_id,
                token,
                channel_name,
                create_delay,
                channel_amount,
                bot
            )
        )

        create.start()

        send = threading.Thread(
            target=AppUtils.send_messages,
            args=(
                token,
                guild_id,
                send_message.replace('\\n', '\n'),
                send_delay,
                send_amount,
                bot
            )
        )

        send.start()

client.run(token, bot=bot)
