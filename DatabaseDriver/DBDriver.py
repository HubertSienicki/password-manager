import psycopg2 as psg

class Driver():

    def __init__(self):
        self.conn = psg.connect(
            host="127.0.0.", 
            database="password_manager",
            user="postgres",
            password="Bo27erer#"
        )
    
    def test_connect()