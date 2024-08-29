import time
import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнование')
    for i in range(5):
        await asyncio.sleep(30 / power)
        print(f'Силач {name} поднял {i + 1} шар')
    print(f'Силач {name} закончил соревнование')


async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Nic', 3))
    task2 = asyncio.create_task(start_strongman('Pol', 4))
    task3 = asyncio.create_task(start_strongman('Mike', 5))
    await task1
    await task2
    await task3


asyncio.run(start_tournament())
