import happybase as hb
import csv 

connection = hb.Connection()
connection.open()

t = connection.table('powers')
csv_input = open('input.csv', 'r')
rreader = csv.reader(csv_input)


counter = '3'
for row in rreader:
    t.put(
        row[0],
        {
            'personal:hero': row[1],
            'personal:power': row[2],
            'professional:name': row[3],
            'professional:xp': row[4],
            'custom:color': row[5]
        }
    )


connection.close()