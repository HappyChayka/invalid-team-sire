import sqlite3 as s3


def create_table():
    connection = s3.connect("buildings.db")
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS buildings (
                id INTEGER PRIMARY KEY,
                disabs TEXT,
                disab_feats TEXT,
                type TEXT,
                name TEXT,
                district TEXT,
                b_num TEXT,
                geomark TEXT
    );
    """)
    connection.commit()
    connection.close()


def search_tags(disabs="", ty="",
                name="", district="",
                b_num=""):
    connection = s3.connect("buildings.db")
    cursor = connection.cursor()
    cursor.execute("""
    SELECT * FROM buildings WHERE 
                disabs LIKE ? OR
                type LIKE ? OR
                name LIKE ? OR
                district LIKE ? OR
                b_num LIKE ?
    ;
    """)
    connection.commit()
    rows = cursor.fetchall()
    connection.close()
    return rows


def view_all():
    connection = s3.connect("buildings.db")
    cursor = connection.cursor()
    cursor.execute("""
    SELECT * FROM buildings""")
    connection.commit()
    rows = cursor.fetchall()
    connection.close()
    return rows


def insert_data(disabs="", ty="", dis_feats="",
                name="", district="", 
                b_num="", gm=""):
    connection = s3.connect("buildings.db")
    cursor = connection.cursor()
    cursor.execute("""
    INSERT INTO buildings VALUES(
                   NULL, ?, ?, ?, ?, ?, ?, ?
    )""", [disabs, dis_feats, ty, name, district, b_num, gm])
    connection.commit()
    connection.close()


create_table()
# insert_data(disabs="ОДС", ty="Социальная сфера",
#             dis_feats=", ".join(["Пандус"]),
#             name="Молодёжная библиотека № 45", district="Пр. Шинников",
#             b_num="44", gm="")
for i in open("ergerggr.txt", encoding="UTF8"):
    k = i.split(";")
    insert_data(disabs=k[0], ty=k[1], dis_feats=k[2], name=k[3], district=k[4], b_num=k[5])

# disabs:
# Нарушения слуха
# Нарушения зрения
# Нарушения ОДС
# Нарушения умственного развития

# ty:
# Культура
# Спорт
# Образование
# Социальная сфера
