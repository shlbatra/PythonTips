import logging
import sqlite3


#used try final block to make sure connection is always closed
def main():
    logging.basicConfig(level=logging.INFO)
    connection = sqlite3.connect("application.db")
    try:
        cursor = connection.cursor() # retreive cursor from db connection
        cursor.execute("SELECT * FROM blogs")
        logging.info(cursor.fetchall())
    finally:
        logging.info("Closing Connection")
        connection.close()


if __name__ == "__main__":
    main()
