import happybase as hb

# DON'T CHANGE THE PRINT FORMAT, WHICH IS THE OUTPUT
# OR YOU WON'T RECEIVE POINTS FROM THE GRADER

connection = hb.Connection()
connection.open()
t = connection.table('powers')
row = t.row('row1')
# print(row['professional:name'])

hero = row['personal:hero']
power = row['personal:power']
name = row['professional:name']
xp = row['professional:xp']
color = row['custom:color']
print('hero: {}, power: {}, name: {}, xp: {}, color: {}'.format(hero, power, name, xp, color))

row = t.row('row19')
hero = row['personal:hero']
color = row['custom:color']
print('hero: {}, color: {}'.format(hero, color))

row = t.row('row1')
hero = row['personal:hero']
name = row['professional:name']
color = row['custom:color']
print('hero: {}, name: {}, color: {}'.format(hero, name, color))

connection.close()