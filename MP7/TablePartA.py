#git clone https://github.com/UIUC-CS498-Cloud/MP8_python_template.git
import happybase as hb

connection = hb.Connection()

connection.open()
print(connection.tables())

connection.create_table(
    'powers',
    {
        'row key' :dict(),
        'personal' : dict(),
        'professional' : dict(),
        'custom' : dict()
    })

connection.create_table(
    'food',
    {
        'row key': dict(),
        'nutrition' : dict(),
        'taste' : dict()
    }

)

print(connection.tables())

connection.close()