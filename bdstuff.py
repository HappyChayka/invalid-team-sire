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
    return True


def search_tags(disabs="", type="",
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
    connection.close()
    return cursor.fetchall()


def view_all():
    connection = s3.connect("buildings.db")
    cursor = connection.cursor()
    cursor.execute("""
    SELECT * FROM buildings""")
    connection.commit()
    connection.close()
    return cursor.fetchall()


def insert_data(disabs="", type="", dis_feats="",
                name="", district="", 
                b_num="", gm=""):
    connection = s3.connect("buildings.db")
    cursor = connection.cursor()
    cursor.execute("""
    INSERT INTO buildings VALUES(
                   NULL, ?, ?, ?, ?, ?, ?, ?
    )""", [disabs, type, dis_feats, name, district, b_num, gm])
    connection.commit()
    connection.close()


create_table()
insert_data(disabs="Нарушения умственного развития", type="Культура", dis_feats="".join(["Туалет для людей с инвалидностью", "Кнопка вызова персонала", "Пандус"]),
            name="Школа-интернат 'Надежда'", district="Пр. Строителей",
            b_num="58", gm="")


# disabs:
# Нарушения слуха
# Нарушения зрения
# Нарушения ОДС
# Нарушения умственного развития

# type:
# Культура
# Спорт
# Образование
# Социальная сфера