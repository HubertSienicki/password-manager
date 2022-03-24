import psycopg2
from config import config

def test_connection():
    """Test connection to postgresql server"""

    conn = None
    try:
        params = config()

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