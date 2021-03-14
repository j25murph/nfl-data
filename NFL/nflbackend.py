import pandas as pd
import psycopg2
import scrape
from scrape import df

def create_table():
    conn = psycopg2.connect("dbname='database1' user='postgres' password = 'hockey' host='localhost'port='5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS nflrush (id INTEGER, name TEXT, yards INTEGER, attempts INTEGER, touchdowns INTEGER, twenty_plus INTEGER, forty_plus INTEGER, lng INTEGER, first_downs INTEGER, first_down_percentage REAL, rush_fum INTEGER)")
    conn.commit()
    conn.close()

df.to_csv("rushing2019.csv")

def upload():
    conn=psycopg2.connect("dbname='database1' user='postgres' password = 'hockey' host='localhost'port='5432'")
    cur = conn.cursor()
    with open('rushing2019.csv', 'r') as f:
        next(f)
        cur.copy_from(f, 'nflrush', sep=',')
    conn.commit()

def view():
    conn=psycopg2.connect("dbname='database1' user='postgres' password = 'hockey' host='localhost'port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM nflrush")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(name="", yards)












#table_name = "nfl_rushing_2019"
#df.to_sql(table_name, con, if_exists = 'append', index = False)
#con.close()
