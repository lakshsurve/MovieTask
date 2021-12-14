import sqlite3

conn = sqlite3.connect("moviee.db")

c = conn.cursor()


c.execute("""CREATE TABLE movies (
            movie text,
            actor text,
            actress text,
            director text,
            year integer
            )""")
def ins():
    print("Enter Details of Movie in sequence of Name of Movie, Actor, Actress, Diector & Year of Release")
    movie = input()
    act = input()
    actress = input()
    director = input()
    year = int(input())
    c.execute("INSERT INTO movies VALUES (?,?,?,?,?)",
              (movie.lower(), act.lower(), actress.lower(), director.lower(), year))
    conn.commit()


while True:
    print("Choose the option \n 1.Insert Details \n 2.Fetch Details \n 3.Find Movie using actor name \n 4.Quit")
    n = int(input())
    if n == 1:
        ins()
    elif n == 2:
        c.execute("SELECT * FROM movies")
        conn.commit()
        print(c.fetchall())
    elif n == 3:
        actr = input("Enter the name of actor to search movie \n")
        c.execute("SELECT movie FROM movies WHERE actor=:act", {'act': actr.lower()})
        print(c.fetchall())
        conn.commit()
    elif n == 4:
        break

conn.close()