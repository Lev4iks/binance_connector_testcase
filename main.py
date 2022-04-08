from binance_connector import listen
from telegram_bot import run_bot
from settings import BINANCE_API

import asyncio


async def main():
    run_bot()
    await asyncio.create_task(listen(BINANCE_API))


if __name__ == '__main__':
    asyncio.run(main())
