import sqlite3

connection = sqlite3.connect('cars.db')
sql = connection.cursor()
sql.execute('CREATE TABLE cars '
            '(mdel TEXT, color TEXT, year INTEGER, mileage REAL);')
connection.commit()
