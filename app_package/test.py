from os import path

basedir = path.abspath(path.dirname(__file__))
print(basedir)

basedir += '/models/database.db'
print(basedir)
