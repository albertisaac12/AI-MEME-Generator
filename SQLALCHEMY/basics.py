from sqlalchemy import create_engine, text

# Engine is used to talk to the database or connect to it
# Also if the database does not exist it will create it

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)

# The conn object is used to execute commands this makes a connection to the DB
# conn = engine.connect()

# conn.execute("CREATE TABLE IF NOT EXISTS")

with engine.connect() as conn:
    result = conn.execute(text("select 'hello world'"))
    print(result.all())


with engine.connect() as conn:
    conn.execute(text("create table if not exists meow(x integer primary key autoincrement,y integer)"))
    conn.execute(
        text("insert into meow (y) values(:y)"),
        [{"y":1},{"y":5}]
    )
    conn.commit()
    res = conn.execute(text("select * from meow"))
    print(res.all())