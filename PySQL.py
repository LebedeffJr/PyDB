import psycopg2

conn = psycopg2.connect(database="person_info", user="postgres", password="___")

def create_tables():
    with conn.cursor() as cur:
        cur.execute("""
        DROP TABLE Phone;
        DROP TABLE Person;
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS Person(
            id SERIAL PRIMARY KEY,
            name VARCHAR(40) NOT NULL,
            last_name VARCHAR(40) NOT NULL,
            email VARCHAR(50)
            );
            """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS Phone(
            id SERIAL PRIMARY KEY,
            Person_id INT NOT NULL REFERENCES Person(id),
            number VARCHAR (20)
            );
            """)
        conn.commit()

def addPerson():
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO Person (name, last_name, email)
            VALUES (%s, %s, %s);
            """,
            (input('Введите имя: '),
            input('Введите Фамилию: '),
            input('Введите email: '))
        )
        conn.commit()

def addPhone():
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO Phone (person_id, number)
            VALUES (%s, %s)
            """,
            (input('Введите id Пользователя: '),
             input('Введите телефон для добавления: '))
        );
        conn.commit()

def updatePerson():
    change = input('Что хотите поменять? (имя, фамилию, email) ')
    if change == 'имя':
        with conn.cursor() as cur:
            cur.execute("""
                UPDATE Person
                SET name=%s WHERE id=%s
                """, (input('Введите новое имя: '),
                     input('Введите id пользователя: '))
                )
    elif change == 'фамилию':
        with conn.cursor() as cur:
            cur.execute("""
                UPDATE Person
                SET last_name=%s WHERE id=%s
                """, (input('Введите новую фамилию: '),
                     input('Введите id пользователя: '))
                )
    elif change == 'email':
        with conn.cursor() as cur:
            cur.execute("""
                UPDATE Person
                SET email=%s WHERE id=%s
                """, (input('Введите новый email: '),
                      input('Введите id пользователя: '))
                )
    else:
        print('Нет такой информации, попробуйте снова.')

    conn.commit()

def delete_phone():
    with conn.cursor() as cur:
        cur.execute("""
            DELETE FROM Phone WHERE number=%s;
            """, (input('Введите телефон который хотите удалить: '),)
        )
    conn.commit()

def delete_person(id_person):
    with conn.cursor() as cur:
        cur.execute("""
            DELETE FROM Phone WHERE person_id=%s;
            """, (id_person,)
            )
        cur.execute("""
            DELETE FROM Person WHERE id=%s;
            """, (id_person,)
            )
    conn.commit()

def find_person():
    param = input('По какому параметру хотите искать? ')
    if param == 'имя':
        with conn.cursor() as cur:
            cur.execute("""
            SELECT * FROM Person WHERE name=%s;
            """, (input('Введите имя: '),)
            )
            print(cur.fetchall())
    elif param == 'фамилия':
        with conn.cursor() as cur:
            cur.execute("""
            SELECT * FROM Person WHERE last_name=%s;
            """, (input('Введите фамилию: '),)
            )
            print(cur.fetchall())
    elif param == 'email':
        with conn.cursor() as cur:
            cur.execute("""
            SELECT * FROM Person WHERE email=%s;
            """, (input('Введите email: '),)
            )
            print(cur.fetchall())
    elif param == 'телефон':
        with conn.cursor() as cur:
            cur.execute("""
            SELECT * FROM Person JOIN Phone
            ON Phone.person_id = Person.id
            WHERE Phone.number=%s;
            """, (input('Введите телефон: '),)
            )
            print(cur.fetchall())
    else:
        print('Нет такого параметра. Попробуйте снова.')

if __name__ == "__main__":
    # create_tables()
    # addPerson()
    # addPhone()
    # updatePerson()
    # delete_phone()
    # delete_person()
    # find_person()
    conn.close()
