import asyncio
import logging

import aiosqlite


async def main():
    logging.basicConfig(level=logging.INFO)
    # async with aiosqlite.connect("application.db") as db:   # database is context manager so can write this way as well
    #     async with db.execute("SELECT * FROM blogs") as cursor: #cursoe can be context manager as well
    #         logging.info(await cursor.fetchall())
    
    #alternate 
    # async with (
        # aiosqlite.connect("application.db") as db,   # database is context manager so can write this way as well
        # db.execute("SELECT * FROM blogs") as cursor: #cursoe can be context manager as well
        #  ):       
        #       logging.info(await cursor.fetchall())
    db = await aiosqlite.connect("application.db")
    cursor = await db.execute("SELECT * FROM blogs")
    logging.info(await cursor.fetchall())


if __name__ == "__main__":
    asyncio.run(main())
