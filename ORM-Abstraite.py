from abc import ABC, abstractmethod
import mysql.connector

class ORM(ABC):
    
    #Abstract Base Class for a simple Object-Relational Mapping (ORM).
    
    #This class provides a blueprint for database interactions (CRUD). 
    #It cannot be instantiated directly and must be inherited by table-specific classes.

    def __init__(self, host, user, password, database):
        #Initialize the ORM with database credentials.
        
        #Args:
        #host (str): The database server address (e.g., AlwaysData host).
        #user (str): Database username.
        #password (str): Database password.
        #database (str): Name of the specific database to use.
            
        #Note:
        #Uses double underscores (e.g., self.__host) for ENCAPSULATION, 
        #making these attributes private to the ORM class.

        self.__host = host
        self.__user = user
        self.__password = password
        self.__database = database

    def _get_connection(self):
        #Creates and returns a new MySQL connection.
        
        #This is a protected method (indicated by the single underscore),
        #intended to be used internally by CRUD methods.
        return mysql.connector.connect(
            host=self.__host,
            user=self.__user,
            password=self.__password,
            database=self.__database
        )

    @property
    @abstractmethod
    def table_name(self):
        #Abstract Property: Must be implemented by subclasses to define 
        #which SQL table the class interacts with.
        pass

    #--- GET (Read all) ---
    def get_all(self):
        #Fetches all records from the table.
        
        #Returns:
        #list: A list of dictionaries representing the table rows.

        db = self._get_connection()
        cursor = db.cursor(dictionary=True)
        cursor.execute(f"SELECT * FROM {self.table_name}")
        result = cursor.fetchall()
        db.close()
        return result

    #--- GET (Read one by ID) ---
    def get_one(self, record_id):
        #Fetches a single record by its primary key (ID).
        
        #Args:
        #record_id (int/str): The unique identifier of the row.
        #Returns:
        #dict: The row data or None if not found.
       
        db = self._get_connection()
        cursor = db.cursor(dictionary=True)
        sql = f"SELECT * FROM {self.table_name} WHERE id = %s"
        cursor.execute(sql, (record_id,))
        result = cursor.fetchone()
        db.close()
        return result

    #--- POST (Create) ---
    def post(self, data_dict):
        #Inserts a new record into the database.
        
        #Args:
        #data_dict (dict): Keys should match table columns, values are data to insert.
        #Returns:
        #dict: Confirmation of the new record ID and status.
        
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

    #--- PUT (Update) ---
    def put(self, record_id, data_dict):
        
        #Updates an existing record.
        
        #Args:
        #record_id (int/str): The ID of the record to update.
        #data_dict (dict): Dictionary of columns and new values.
        #Returns:
        #dict: Confirmation of the update.
        
        db = self._get_connection()
        cursor = db.cursor()
        settings = ", ".join([f"{key} = %s" for key in data_dict.keys()])
        sql = f"UPDATE {self.table_name} SET {settings} WHERE id = %s"
        params = list(data_dict.values()) + [record_id]
        cursor.execute(sql, params)
        db.commit()
        db.close()
        return {"id": record_id, "status": "updated"}

    #--- DELETE ---
    def delete(self, record_id):
        
        #Removes a record from the database.
        
        #Args:
        #record_id (int/str): The ID of the record to delete.
        #Returns:
        #dict: Confirmation of the deletion.
        db = self._get_connection()
        cursor = db.cursor()
        sql = f"DELETE FROM {self.table_name} WHERE id = %s"
        cursor.execute(sql, (record_id,))
        db.commit()
        db.close()
        return {"id": record_id, "status": "deleted"}
