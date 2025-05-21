import asyncio


async def cancel_me():
    print("Enter cancel_me()")
    await asyncio.sleep(3600)


async def main():
    task = asyncio.create_task(cancel_me())
    await asyncio.sleep(1)

    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("main(): cancel_me is cancelled now")


if __name__ == "__main__":
    asyncio.run(main())
