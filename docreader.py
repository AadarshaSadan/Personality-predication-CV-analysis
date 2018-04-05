import sqlite3
from nltk.tokenize import sent_tokenize 
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
conn=sqlite3.connect('details.db')
c=conn.cursor()
def create_table():
    #c.execute('''CREATE TABLE IF NOT EXISTS details(first)''')
    c.execute('''CREATE TABLE IF NOT EXISTS CvScore(name,regno,designation,salary,school,highscool,experience)''')
    c.execute('CREATE TABLE IF NOT EXISTS Score(regno,app_Score,cv_score)')
    c.execute('''CREATE TABLE IF NOT EXISTS final(name,regno,cv_score,remarks)''')
    conn.commit()
  