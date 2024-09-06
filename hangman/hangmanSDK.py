import sqlite3
import datetime
from .model import *

def cursor():
    return sqlite3.connect("hangman.db").cursor();

c = cursor()

c.execute('CREATE TABLE IF NOT EXISTS state ( id int NOT NULL,state varchar(255),PRIMARY KEY (id))')
c.execute('CREATE TABLE IF NOT EXISTS game ( game_id int NOT NULL,allocated_word varchar(255),cretaed_date DATE,updated_date DATE,state_id int,'
          + 'PRIMARY KEY (id), FOREIGN KEY (state_id) REFERENCES state(id))')

#save Game with Game ID
def add_game(word,stateid):
   c = cursor()
   with c.connection:
       c.execute('INSERT INTO game VALUES(?,?,?,?)', (word,datetime.datetime.now(),'',stateid))
   return c.lastrowid

#update the Game status
def update_game(gameid , status ):
    c = cursor()
    with c.connection:
       c.execute('UPDATE game set updated_date'+datetime.datetime.now()+', state_id='+status+' where game_id='+gameid)
    return c.fetchone()

#add States
def add_state(id , state):
   c = cursor()
   with c.connection:
       c.execute('INSERT INTO state VALUES(?,?)', (id,state))
   return c.lastrowid


def get_all_states():
    with c.connection:
        c.execute('SELECT * FROM state')
    
    return c.fetchall()