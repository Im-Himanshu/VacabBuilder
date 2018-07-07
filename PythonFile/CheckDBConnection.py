import mysql.connector
from mysql.connector import Error
from python_mysql_dbconfig import read_db_config
#import python_mysql_dbconfig as caller;

def connect():
    """ Connect to MySQL database """
    try:

        db_config = read_db_config()
        print(db_config)
        conn = mysql.connector.connect(**db_config)
        if conn.is_connected():
            print('Connected to MySQL database')

    except Error as e:
        print(e)

    finally:
        conn.close()


if __name__ == '__main__':
    connect()