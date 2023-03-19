import asyncio

async def uradi():
    for i in range(20):
        print(f" ja nesto radim {i}")
        await asyncio.sleep(1)

async def main():
    task1 = asyncio.create_task(uradi())
    task2 = asyncio.create_task(uradi())
    await asyncio.sleep(20)

asyncio.run(main())