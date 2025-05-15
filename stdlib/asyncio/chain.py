# asyncio_coroutine_chain.py
# https://pymotw.com/3/asyncio/coroutines.html
import asyncio


async def make_chicken_soup():
    print("make chicken soup")
    veggetable = await chop_veggetable()
    soup = await prepare_soup(veggetable)
    soup += ", and chicken"
    return soup


async def chop_veggetable():
    print("chop veggetable")
    return "carrot, potatoes, celery"


async def prepare_soup(ingredients):
    print("prepare soup")
    return "soup made from {}".format(ingredients)


event_loop = asyncio.get_event_loop()
try:
    return_value = event_loop.run_until_complete(make_chicken_soup())
    print(return_value)
finally:
    event_loop.close()
