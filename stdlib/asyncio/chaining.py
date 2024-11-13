#!/usr/bin/env python3
# whatis: We can chain async coroutines together using the await keyword
import asyncio


async def make_soup():
    print("Making soup")
    veggie1 = await harvest("potatoes")
    veggie2 = await harvest("onion")
    print("Done")
    return f"soup with {veggie1} and {veggie2}"


async def harvest(veggie):
    print(f"Harvesting {veggie}")
    return veggie


loop = asyncio.get_event_loop()
try:
    soup_maker = make_soup()
    soup = loop.run_until_complete(soup_maker)
    print(f"Serving {soup}")
finally:
    loop.close()
