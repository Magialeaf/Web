import requests
import asyncio
import time
import aiohttp

start = time.time()

async def run(url:str):
    print("Downloading... ")
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            page_text = response.text
            print(page_text)
    print("Finished")

urls = ["http://127.0.0.1:5000","http://127.0.0.1:5000/bobo","http://127.0.0.1:5000/jay","http://127.0.0.1:5000/tom"]
loop = asyncio.new_event_loop()
tasks = []
for url in urls:
    c = run(url)
    task = asyncio.ensure_future(c,loop=loop)
    tasks.append(task)
loop.run_until_complete(asyncio.wait(tasks))

end = time.time()
print("time:",end - start)