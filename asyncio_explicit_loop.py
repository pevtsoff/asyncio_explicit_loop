import asyncio
import aiohttp

# Timeout to test the pending tasks display
timeout = 0.2

async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def main():
    urls = ['http://www.rbc.ru', 'http://www.mail.ru', 'http://www.rambler.ru']
    tasks = []
    
    for url in urls:
        task = asyncio.create_task(fetch_url(url))
        task.set_name(url)
        tasks.append(task)
                                           
    done, pending = await asyncio.wait(
        tasks, timeout=timeout, return_when=asyncio.ALL_COMPLETED
    )
    print(f'{done=}')
    print(f'------------------------------------------')
    print(f'{pending=}')
   


try:
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()
finally:
    loop.close()