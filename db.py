import psycopg2
import os


class Database:
    def __init__(self):
        self.db = psycopg2.connect(
            dbname=os.getenv("DATABASENAME"),
            password=os.getenv("POSTGRESS_PASSWORD"),
            user=os.getenv("POSTGRESS_USER")
        )
        self.db.autocommit = True

    async def insert_user_id(self, user_id):
        with self.db.cursor() as cursor:
            insert_sql_query = """
            insert into users (user_id) values (%s);
            """
            cursor.execute(insert_sql_query, (user_id,))

    async def select_user_id(self, user_id):
        with self.db.cursor() as cursor:
            select_sql_query = """
            select user_id from users where user_id = %s;
            """
            cursor.execute(select_sql_query, (user_id,))
            result = cursor.fetchone()
            if result:
                return False
            else:
                return True
