import asyncio
import time

# async def re(url:str):
#     print("Doing url",url)
#     print("end")
#     return url
#
# c = re("www.baidu.com")

# loop = asyncio.new_event_loop()
# asyncio.set_event_loop(loop)
# loop.run_until_complete(c)
# asyncio.run(c)

# loop = asyncio.new_event_loop()
# asyncio.set_event_loop(loop)
# task = loop.create_task(c)
# print(task)

# loop = asyncio.new_event_loop()
# asyncio.set_event_loop(loop)
# task = asyncio.ensure_future(c,loop=loop)
# loop.run_until_complete(task)

# def callback_func(task):
#     print(task.result())
#
# loop = asyncio.new_event_loop()
# asyncio.set_event_loop(loop)
# task = asyncio.ensure_future(c,loop=loop)
# task.add_done_callback(callback_func)
# loop.run_until_complete(task)

async def request(url:str):
    print("Downloading",url,"...")
    await asyncio.sleep(2)
    print("OK for",url)

start = time.time()
urls = ["www.baidu.com","www.sogou.com","www.google.com"]

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
stasks = []
for url in urls:
    c = request(url)
    task = asyncio.ensure_future(c,loop=loop)
    stasks.append(task)
loop.run_until_complete(asyncio.wait(stasks))
print(time.time()-start)