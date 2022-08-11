import sqlite3

class Database():
    def __init__(self,name):
        self.db = sqlite3.connect(name)
        self.cursor = self.db.cursor()
        self.name = name

    def create_table_customers(self,shape):
        query= """
        create table if not exists customers(
        first_name datatype,
        last_name datatype,
        email datatype
        )
        """
        self.cursor.execute(query)

    def insert_customers(self,first_name,last_name,email):
        query =f"""
        insert into customers
        values ('{first_name}','{last_name}','{email}')
        """
        self.cursor.execute(query)
        self.db.commit()

    def select_all_customers(self):
        query = f"""
            select *
            from customers
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()




