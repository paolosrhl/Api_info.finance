import mysql.connector


class ORM:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        return mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )

    def use_database(self, mydb):
        mycursor = mydb.cursor()
        mycursor.execute(f"USE {self.database}")

    def select_all(self, Article):
        mydb = self.connect()
        self.use_database(mydb)
        mycursor = mydb.cursor()
        mycursor.execute(f"SELECT * FROM {Article}")
        return mycursor.fetchall()

my_orm = ORM(host="mysql-serhal.alwaysdata.net", user="serhal", password="968-AJK-0101/", database="serhal_projct")
my_orm.connect()
my_orm.select_all("Article")