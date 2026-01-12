import asyncio
import logging

import aiosqlite


async def main():
    logging.basicConfig(level=logging.INFO)
    # Using 2 context managers for both database and cursor
    async with aiosqlite.connect("application.db") as db:   # database is context manager so can write this way as well
        async with db.execute("SELECT * FROM blogs") as cursor: #cursoe can be context manager as well
            logging.info(await cursor.fetchall())
    
    #alternate 
    # async with (
        # aiosqlite.connect("application.db") as db,   # database is context manager so can write this way as well
        # db.execute("SELECT * FROM blogs") as cursor: #cursoe can be context manager as well
        #  ):       
        #       logging.info(await cursor.fetchall())

    # another alternate with one context manager for db only
    # async with aiosqlite.connect("application.db") as db:   # database is context manager so can write this way as well
    #     cursor = await db.execute("SELECT * FROM blogs") #cursoe can be context manager as well
    #     await cursor.close()
    #     logging.info(await cursor.fetchall())

    # Without context manager call (less preferred)
    # db = await aiosqlite.connect("application.db")
    # cursor = await db.execute("SELECT * FROM blogs")
    # logging.info(await cursor.fetchall())
    # await cursor.close()
    # await db.close()
    


if __name__ == "__main__":
    asyncio.run(main())
