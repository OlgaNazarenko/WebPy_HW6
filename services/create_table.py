import sqlite3
from sqlite3 import Error
from services.settings import DATABASE


class DataConn:
    def __init__(self, database_name):
        self.database_name = database_name

    def __enter__(self):
        self.conn = sqlite3.connect(self.database_name)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
        if exc_val:
            raise


def create_table() -> tuple():


    sgl_create_student_table = """
    DROP TABLE IF EXISTS students;
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        first_name VARCHAR(30) NOT NULL,
        last_name VARCHAR(30) NOT NULL,
        group_id INTEGER,
        FOREIGN KEY (group_id) REFERENCES groups (id)
            ON DELETE CASCADE
            ON UPDATE CASCADE
    );
    """

    sql_create_group_table = """
    DROP TABLE IF EXISTS groups;
    CREATE TABLE IF NOT EXISTS groups (
        id INTEGER PRIMARY KEY,
        title VARCHAR(50) NOT NULL
    );
    """

    sql_create_professor_table = """
    DROP TABLE IF EXISTS professors;
    CREATE TABLE IF NOT EXISTS professors (
        id INTEGER PRIMARY KEY,
        first_name VARCHAR(30) NOT NULL,
        last_name VARCHAR(30) NOT NULL
    );
    """

    sgl_create_disciplines_table = """
    DROP TABLE IF EXISTS discipline;
    CREATE TABLE IF NOT EXISTS discipline (
        id INTEGER PRIMARY KEY,
        discipline VARCHAR(50) NOT NULL,
        groups_id INTEGER,
        professors_id INTEGER,
        FOREIGN KEY (groups_id) REFERENCES groups (id)
          ON DELETE CASCADE
          ON UPDATE CASCADE,
        FOREIGN KEY (groups_id) REFERENCES professors (id)
          ON DELETE CASCADE
          ON UPDATE CASCADE
    );
    """

    sql_create_marks_table = """
    DROP TABLE IF EXISTS marks;
    CREATE TABLE IF NOT EXISTS marks (
        id INTEGER PRIMARY KEY,
        mark INTEGER,
        lesson_date DATE,
        students_id INTEGER NOT NULL,
        discipline_id INTEGER NOT NULL,
        professors_id INTEGER NOT NULL,
        FOREIGN KEY (students_id) REFERENCES students (id)
          ON DELETE CASCADE
          ON UPDATE CASCADE,
        FOREIGN KEY (discipline_id) REFERENCES discipline (id)
          ON DELETE CASCADE
          ON UPDATE CASCADE,
        FOREIGN KEY (professors_id) REFERENCES professors (id)
          ON DELETE CASCADE
          ON UPDATE CASCADE
    );
    """

    Tables: list = [sql_create_group_table, sgl_create_student_table, sql_create_professor_table,
                    sgl_create_disciplines_table, sql_create_marks_table]

    with DataConn(DATABASE) as conn:
        cursor = conn.cursor()
        print("Connection to SQLite DB was successful")
       
        if conn is not None:
            for table in Tables:
                cursor.executescript(table)
        cursor.close()
        print('DB is created\n')
