import sqlite3

#Create Database Manager using CRUD Structure
class Database():
    def __init__(self,entity):
        self.db = sqlite3.connect('data.db',check_same_thread=False)
        self.cursor = self.db.cursor()
        self.entity = entity
    
    def create_table(self):
        entity = self.entity
        name= entity['NAME']
        schema = entity['SCHEMA']
        query= f"""create table if not exists {name}({schema})"""
        self.cursor.execute(query)

    #CREATE
    def create(self,values):
        self.create_many([values])

    def create_many(self,values,custom_shape=None):
        entity = self.entity
        name= entity['NAME']
        shape = custom_shape or entity['SHAPE']
        
        query =f"""
        insert into {name}
        (link,is_download)
        values {shape}
        """
        print(query)
        self.cursor.executemany(query,values)
        self.db.commit()
    #READ
    def read(self,query):
        self.cursor.execute(query)
        return self.cursor.fetchall()
    def read_all(self):
        entity = self.entity
        name= entity['NAME']
        self.cursor.execute(f'select * from {name}')
        return self.cursor.fetchall()
    
    #UPDATE
    def update(self,query):
        self.cursor.execute(query)
        return self.db.commit()

    #DELETE
    def delete(self):
        pass





