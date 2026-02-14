from sqlalchemy import create_engine

# Engine is used to talk to the database or connect to it
# Also if the database does not exist it will create it

engine = create_engine("sqllite:///mydatabase.db", echo=True)

# The conn object is used to execute commands this makes a connection to the DB
conn = engine.connect()

conn.execute("CREATE TABLE IF NOT EXISTS")