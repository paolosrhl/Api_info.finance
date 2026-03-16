from abc import ABC, abstractmethod
import mysql.connector

class ORM(ABC):
    def __init__(self, host, user, password, database):
        self.__host = host
        self.__user = user
        self.__password = password
        self.__database = database

    def _get_connection(self):
        return mysql.connector.connect(
            host=self.__host,
            user=self.__user,
            password=self.__password,
            database=self.__database
        )

    @property
    @abstractmethod
    def table_name(self):
        pass

    # --- GET (Read all) ---
    def get_all(self):
        db = self._get_connection()
        cursor = db.cursor(dictionary=True)
        cursor.execute(f"SELECT * FROM {self.table_name}")
        result = cursor.fetchall()
        db.close()
        return result

    # --- GET (Read one by ID) ---
    def get_one(self, record_id):
        db = self._get_connection()
        cursor = db.cursor(dictionary=True)
        sql = f"SELECT * FROM {self.table_name} WHERE id = %s"
        cursor.execute(sql, (record_id,))
        result = cursor.fetchone()
        db.close()
        return result
    #I'm here 

    # --- POST (Create) ---
    def post(self, data_dict):
        db = self._get_connection()
        cursor = db.cursor()
        columns = ", ".join(data_dict.keys())
        placeholders = ", ".join(["%s"] * len(data_dict))
        sql = f"INSERT INTO {self.table_name} ({columns}) VALUES ({placeholders})"
        cursor.execute(sql, list(data_dict.values()))
        db.commit()
        new_id = cursor.lastrowid
        db.close()
        return {"id": new_id, "status": "created"}

    # --- PUT (Update) ---
    def put(self, record_id, data_dict):
        db = self._get_connection()
        cursor = db.cursor()
        settings = ", ".join([f"{key} = %s" for key in data_dict.keys()])
        sql = f"UPDATE {self.table_name} SET {settings} WHERE id = %s"
        params = list(data_dict.values()) + [record_id]
        cursor.execute(sql, params)
        db.commit()
        db.close()
        return {"id": record_id, "status": "updated"}

    # --- DELETE ---
    def delete(self, record_id):
        db = self._get_connection()
        cursor = db.cursor()
        sql = f"DELETE FROM {self.table_name} WHERE id = %s"
        cursor.execute(sql, (record_id,))
        db.commit()
        db.close()
        return {"id": record_id, "status": "deleted"}