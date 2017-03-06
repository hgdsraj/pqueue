import sqlite3
conn = sqlite3.connect('queue.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS queue
             (priority int, message text)''')
