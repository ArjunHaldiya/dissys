import pymysql

conn = pymysql.connect(host="localhost", port=3307, user="root", password="rootpass", database="demo")


def setup():
    with conn.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT PRIMARY KEY,
                name varchar(50),
                email varchar(50)
            )
        """)
        conn.commit()



def create(id, name, email):
    with conn.cursor() as  cursor:
        cursor.execute("INSERT INTO users (id, name, email) VALUES (%s, %s, %s)", (id, name, email))
    conn.commit()

def update(id, new_email):
    with conn.cursor() as cursor:
        cursor.execute("UPDATE users SET email = %s WHERE id = %s", (new_email, id))
    conn.commit()

def read(id):
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM users WHERE id = %s", (id,))
        return cursor.fetchone()

def delete(id):
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM users WHERE id=%s", (id,))
    conn.commit()


if __name__ == "__main__":
    setup()
    create(1, "Arjun Haldiya","arjunhaldiya@gmail.com")
    print(read(1))