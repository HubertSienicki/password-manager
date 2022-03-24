import psycopg2
from config import configParser


SELECT_QUERY = """SELECT password FROM accounts WHERE app_name = '%s'"""

#Function used to connect to the database
def connect():
    try:
        params = configParser()
        print('Connecting to postgresql server...')
        connection = psycopg2.connect(**params)
        
        print('...connection successful!')
        return connection
    
    except (Exception, psycopg2.Error) as error:
        print(error)


def find_password(app_name):
    try:
        connection = connection()
        cursor = connection.cursor()
    
    except(Exception, psycopg2.Error) as error:
        print(error)





###########################TEST METHODS#####################################
def test_connection():
    """Test connection to postgresql server"""

    conn = None
    try:
        params = configParser()

        #Connect to postgresql server
        print("Connecting to postgresql server...")
        conn = psycopg2.connect(**params)
        
        # Create a cursor 
        cur = conn.cursor()

        #Execute test statement
        print("PostgreSQL database version: ")
        cur.execute('SELECT version()')

        #display postgresql version
        db_version = cur.fetchone()
        print(db_version)


        #Close connection
        cur.close()


    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()
            print("Connection closed.")

def test_add():
    try:

        params = configParser()
        print("Connecting to postgresql server...")
        conn = psycopg2.connect(**params)
        
        cursor = conn.cursor()

        #Using s string format a query
        insert_query = """INSERT INTO accounts (password, username, email, app_name, url) VALUES(%s, %s, %s, %s, %s)"""
        record = ('123', 'test', 'test@email.com', 'testAppName', "https://test.com")
        
        #Execute a query
        cursor.execute(insert_query, record)
        conn.commit()
        
        #Debug print
        print('...record inserted!')

    except(Exception, psycopg2.Error) as error:
        print(error)
        
def test_delete():
    try:

        params = configParser()
        print('Connection to postgresql server...')
        conn = psycopg2.connect(**params)

        cursor = conn.cursor()

        delete_query = "Delete from accounts"

        cursor.execute(delete_query)
        conn.commit()

        print('...record deleted!')
    except(Exception, psycopg2.Error) as error:
        print(error)
        