import csv
import sqlite3

f = open('lotto.csv', 'r', encoding='utf-8')
fr = csv.reader(f)

con = sqlite3.connect("../db.sqlite3")
cur = con.cursor()
# cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
# print(cur.execute('SELECT sql FROM sqlite_master WHERE type=\'table\' AND name=\'table_name\'').fetchall())
# print(cur.execute("SELECT * FROM lotto_lotto").fetchall())

for nth, date, no1, no2, no3, no4, no5, no6, nob, winmoney, winco in fr:
    row = (nth, date, no1, no2, no3, no4, no5, no6, nob, winmoney, winco)
    # print(row)
    # print(cur.execute("SELECT * FROM lotto_lotto WHERE nth="+nth).fetchone())
    if cur.execute("SELECT * FROM lotto_lotto WHERE nth="+nth).fetchone() is None:
        new_num = len(cur.execute("SELECT * FROM lotto_lotto").fetchall()) + 1
        row = (new_num, nth, date, no1, no2, no3, no4, no5, no6, nob, winmoney, winco)
        cur.execute('INSERT INTO lotto_lotto VALUES (?,?,?,?,?,?,?,?,?,?,?,?);', row)
    else:
        print("??")

cur.execute("SELECT * FROM lotto_lotto")
for row in cur:
    print(row)

cur.close()
con.commit()
con.close()
f.close()
