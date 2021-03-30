import happybase as hb

# DON'T CHANGE THE PRINT FORMAT, WHICH IS THE OUTPUT
# OR YOU WON'T RECEIVE POINTS FROM THE GRADER


connection = hb.Connection()
connection.open()
t = connection.table('powers')
for key, data in t.scan():

    # print(data, "<<DATA")
    color = data['custom:color']
    name = data['professional:name']
    power = data['personal:power']

    for key1, i in t.scan():
        # print(i, "<<I")
        color1 = i['custom:color']
        name1 = i['professional:name']
        power1 = i['personal:power']

        if i['professional:name'] != data['professional:name'] and i['custom:color'] == data['custom:color']:
            print('{}, {}, {}, {}, {}'.format(name, power, name1, power1, color))

connection.close()



# color = ???
# name = ???
# power = ???

# color1 = ???
# name1 = ???
# power1 = ???

# print('{}, {}, {}, {}, {}'.format(name, power, name1, power1, color))


