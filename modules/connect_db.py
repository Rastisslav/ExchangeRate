import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')

conn = psycopg2.connect(
    database="postgres",
    user=POSTGRES_USER,
    password=POSTGRES_PASSWORD,
    host='db',
    port='5432'
)

cursor = conn.cursor()

# vytvori tabulku history_table
def connect_to_db():

    cursor.execute("DROP TABLE IF EXISTS history_table")

    sql = '''CREATE TABLE history_table(
        date CHAR(16),
        first_currency VARCHAR(3) ,
        second_currency VARCHAR(3),
        rate FLOAT,
        higher_now BOOLEAN
    )'''
   
    cursor.execute(sql)
    
    

# funkcia ktora zadava hodnoty do databazy
def add_to_table(date, firstCurrency, secondCurrency, rate, higherNow):
    
    sql = 'INSERT INTO history_table(date, first_currency, second_currency,'\
        ' rate, higher_now) VALUES (%s, %s, %s, %s, %s)'
    
    cursor.execute(sql,(date, firstCurrency, secondCurrency, rate, higherNow))
    

# ukoncenie pirpojenia na db
def quit_db():
    conn.commit()
    conn.close()

# query vsetkych poloziek v db
def show_history():
    cursor.execute('''SELECT * from history_table''')
    result = cursor.fetchall()
    return result
