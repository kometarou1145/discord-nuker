#author github.com/kometarou1145
import time
from utils import DiscordUtils

channel_id_list = []
is_creating = None

def delete_channels(channel_ids: list, token: str, delete_delay: float, bot: bool):
    for i in range(len(channel_ids)):
        res = DiscordUtils.delete_channel(
            token=token,
            channel_id=int(channel_ids[i]),
            bot=bot
        )

        time.sleep(delete_delay)

def create_channels(guild_id: int, token: str, channel_name: str, create_delay: float, amount: int, bot: bool):
    for i in range(amount):
        res = DiscordUtils.create_channel(
            token=token,
            channel_name=channel_name,
            guild_id=guild_id,
            bot=bot
        )

        time.sleep(create_delay)

def send_messages(token: str, guild_id: int, message: str, send_delay: float, amount: int, bot: bool):
    count = 0

    while count <= amount:
        channel_ids = DiscordUtils.get_all_channels(
            token=token,
            guild_id=guild_id,
            bot=True
        )

        for i in range(len(channel_ids)):
            res = DiscordUtils.send(
                message=message,
                token=token,
                channel_id=int(channel_ids[i]),
                bot=bot
            )
            
            count+=1
            time.sleep(send_delay)
