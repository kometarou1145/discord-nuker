import tls_client
from utils import TlsClientUtils
from fake_useragent import UserAgent

def send(message: str, token: str, channel_id: int, bot: bool):
    session = TlsClientUtils.get_new_session("chrome120", True)
    da_token = token

    if bot:
        da_token = f"Bot {token}"

    header = {
        "authorization": da_token
    }

    payload = {
        "content": message
    }

    res = session.post(
        f"https://discord.com/api/v9/channels/{channel_id}/messages",
        headers=header,
        json=payload
    )

    return res

def delete_channel(token: str, channel_id: int, bot: bool):
    session = TlsClientUtils.get_new_session("chrome120", True)
    da_token = token

    if bot:
        da_token = f"Bot {token}"

    header = {
        "authorization": da_token
    }

    res = session.delete(
        f"https://discord.com/api/v9/channels/{channel_id}",
        headers=header
    )

    return res

def create_channel(token: str, channel_name: str, guild_id: int, bot: bool):
    session = TlsClientUtils.get_new_session("chrome120", True)
    da_token = token

    if bot:
        da_token = f"Bot {token}"

    header = {
        "authorization": da_token
    }

    payload = {
        "name": channel_name,
        "type": 0
    }

    res = session.post(
        f"https://discord.com/api/v9/guilds/{guild_id}/channels",
        headers=header,
        json=payload
    )

    return res

def get_all_channels(token: str, guild_id: int, bot: bool):
    session = TlsClientUtils.get_new_session("chrome120", True)
    da_token = token

    if bot:
        da_token = f"Bot {token}"
    
    header = {
        'authorization': da_token
    }

    res = session.get(
        f'https://discord.com/api/v9/guilds/{guild_id}/channels',
        headers=header
    )

    channel_id_list = []

    if res.status_code == 200:
        channels = res.json()
        for data in channels:
            channel_id = data['id']
            channel_id_list.append(channel_id)
    
    return channel_id_list