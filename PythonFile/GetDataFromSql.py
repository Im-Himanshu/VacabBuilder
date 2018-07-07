from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

def query_with_fetchone(query):
    #if (query is  ):

    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute(query)

        row = cursor.fetchone()

        while row is not None:
            print(row)
            row = cursor.fetchone()

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    query = "SELECT * FROM words";
    query_with_fetchone(query)