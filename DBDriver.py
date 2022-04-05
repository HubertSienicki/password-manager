import psycopg2
from config import configParser


SELECT_QUERY = """SELECT password FROM accounts WHERE app_name = '%s'"""
SELECT_ALL_QUERY = "SELECT * FROM accounts"
INSERT_QUERY = """INSERT INTO accounts (password, username, email, app_name, url) VALUES(%s, %s, %s, %s, %s)"""
remove_query = """DELETE FROM accounts WHERE password = %s and username = %s and email = %s and app_name = %s and url = %s"""

#Function used to connect to the database
def connect():
    try:
        params = configParser()
        print('-'*30)
        print('Connecting to postgresql server...')
        connection = psycopg2.connect(**params)
        
        print('...connection successful!')
        print('-'*30)
        print('')
        
        return connection
    
    except (Exception, psycopg2.Error) as error:
        print(error)

def remove_password():
    result = find_all()
    data = []

    try:
        print('Please, select the id to remove from the database')
        to_removeID = int(input(': '))
    
        for row in result:
            data = row
            
            
        print('Removing password from database...')
        connection = connect()
        cursor = connection.cursor()
        cursor.execute(remove_query, data)
        connection.commit()

        print('...Password was removed successfully!')


    except(Exception, psycopg2.Error) as error:
        print(error)




def store_password(password, username, email, app_name, url):
    try:
        connection = connect()
        cursor = connection.cursor()

        to_insert = (password, username, email, app_name, url)

        cursor.execute(INSERT_QUERY, to_insert)
        connection.commit()
    
    except(Exception, psycopg2.Error) as error:
        print(error)



def find_password(app_name):
    try:
        connection = connect()
        cursor = connection.cursor()
        
        sql = SELECT_QUERY % (app_name)
        cursor.execute(sql)

        connection.commit()
        result = cursor.fetchone()
        
        print('-'*30)
        print('Password: ')
        print(result[0])
        print('')

    except(Exception, psycopg2.Error) as error:
        print(error)

def find_users(user_email):

    data = ('Password: ', 'Username: ', 'Email: ', 'url: ', 'App/Site name: ')
    
    try:
        connection = connect()
        cursor = connection.cursor()
        
        select_query = """ SELECT * FROM accounts WHERE email = '""" + user_email + "'"
        cursor.execute(select_query, user_email)
        connection.commit()

        result = cursor.fetchall()

        print('-'*30)
        print('RESULT')
        print('')

        for row in result:
            for i in range(0, len(row) - 1):
                print(data[i] + row[i])

            print('')
            print('-'*30)
    
    except(Exception, psycopg2.Error) as error:
        print(error)


def find_all():
    passID = 1
    data = ('ID: ', 'Password: ', 'Username: ', 'Email: ', 'url: ', 'App/Site name: ')

    try:
        connection = connect()
        cursor = connection.cursor()
        cursor.execute(SELECT_ALL_QUERY)
        connection.commit()
        
        result = cursor.fetchall()

        print('-'*30)
        print('RESULT')
        print('')

        for row in result:
            for i in range(0, len(row) - 1):
                if(i == 0):
                    print(data[i], passID)
                    passID += 1
                    print(data[i + 1] + row[i])
                else:     
                    print(data[i + 1] + row[i])

            print('')
            print('-'*30)

        return result

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
        