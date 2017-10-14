'''
Created on Sep 9, 2014

@author: lada
https://docs.python.org/2/library/sqlite3.html
'''
import sqlite3

def create_db(dbname):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    # Create table
    c.execute('''CREATE TABLE stocks (date text, trans text,
                 symbol text, qty real, price real)''')
    
    # Insert a row of data
    c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
    
    # Save (commit) the changes
    conn.commit()
    
    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()
    
def transaction():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    try:
        c.execute("INSERT INTO stocks VALUES ('2016-02-02','SELL','Ubuntu',200,35.14)")
        c.execute("INSERT INTO stocks VALUES ('BUY',32,200,35.14)")
    except:
        conn.rollback()
        print "Rollback done."
    else:
        conn.commit()
        print "Transaction successful."
    finally:
        conn.close()
        print "Finally connection closed"
def print_db(dbname):
    print "###Printing DB###"
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    for rows in c.execute('SELECT * from stocks'):
        print rows    
    conn.close()
            

def main():
    #create_db('example.db')        
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('SELECT trans from stocks')    
    print c.fetchone()    
    c.execute('SELECT date from stocks WHERE symbol = "RHAT"')
    print c.fetchone()
    for rows in c.execute('SELECT * from stocks'):
        print rows    
    conn.close()
    
    transaction()
    print_db('example.db')

if __name__ == '__main__':
    main()