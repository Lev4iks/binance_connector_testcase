from helpers import check_pair
import aiohttp as aio
import json


async def listen(url):
    async with aio.ClientSession().ws_connect(url, ssl=True) as ws:

        async for msg in ws:

            if msg.type == aio.WSMsgType.close:
                await ws.close()
                return 1

            if msg.type == aio.WSMsgType.error:
                print(f'Error: {msg.data}')

            if msg.type == aio.WSMsgType.ping:
                await msg.pong()
                print('Pong message sent')

            if msg.type == aio.WSMsgType.TEXT:
                last_ticker_info = json.loads(msg.data)
                pair = {last_ticker_info['data']['s']: last_ticker_info['data']['c']}
                check_pair(pair)
