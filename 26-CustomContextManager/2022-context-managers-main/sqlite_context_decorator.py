import logging
import sqlite3
from contextlib import contextmanager


@contextmanager
def open_db(file_name: str):
    conn = sqlite3.connect(file_name)
    try:
        logging.info("Creating connection")
        yield conn.cursor() # open db acts like generator -> open database, use cursor, get exception then go back in fn , catch exception and finally clean up the mess 
    finally:
        logging.info("Closing connection")
        conn.commit()
        conn.close()


def main():
    logging.basicConfig(level=logging.INFO)
    with open_db(file_name="application.db") as cursor: #yield cursor from fn 
        cursor.execute("SELECT * FROM blogs")
        logging.info(cursor.fetchall())


if __name__ == "__main__":
    main()
