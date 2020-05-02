import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()
#if exists delete table
cur.execute('DROP TABLE IF EXISTS Counts')
#create table
cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')
#open file
fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
#go thought the file and search "From "
for line in fh:
    if not line.startswith('From '): continue
    #if it in split for words take second
    pieces = line.split()
    email = pieces[1]
    #take only domen name
    email = email[email.find('@')+1:]
    #choose only with current domain
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (email,))
    #take row from table with domain filter
    row = cur.fetchone()
    #if it exist update or create row
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (email,))

    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 100'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
