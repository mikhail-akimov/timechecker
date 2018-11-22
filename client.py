import aiohttp
import asyncio


async def get_time(client, pid):
    while True:
        async with client.get('http://127.0.0.1:5000') as resp:
            await resp.text()


async def run_checker():
    async with aiohttp.ClientSession(loop=loop) as client:
        tasks = [asyncio.ensure_future(
            get_time(client, pid)) for pid in range(1000)]
        await asyncio.gather(*tasks)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run_checker())
