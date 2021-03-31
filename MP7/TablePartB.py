import happybase as hb

connection = hb.Connection(autoconnect=False)

connection.open()
print(connection.tables())

connection.close()