import psycopg2


conn = psycopg2.connect(
        database="postgres", 
        user='postgres', 
        password='postgres', 
        host='localhost', 
        port= '5432'
    )
    
cursor = conn.cursor()

def connect_to_db():

    cursor.execute("DROP TABLE IF EXISTS history_table")
    
    sql ='''CREATE TABLE history_table(
        date CHAR(16),
        first_currency VARCHAR(3) ,
        second_currency VARCHAR(3),
        rate FLOAT,
        higher_now BOOLEAN
    )'''

    cursor.execute(sql)
    print("nehe")
  

def add_to_table(date, firstCurrency, secondCurrency, rate, higherNow):
    sql = 'INSERT INTO history_table(date, first_currency, second_currency, rate, higher_now) VALUES (%s, %s, %s, %s, %s)'
    cursor.execute(sql,(date, firstCurrency, secondCurrency, rate, higherNow))
    

def quit_db():
    conn.commit()
    conn.close()

def show_history():
    cursor.execute('''SELECT * from history_table''')
    #Fetching 1st row from the table
    result = cursor.fetchall();
    return result