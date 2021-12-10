# creating mysql connection
import mysql.connector
from mysql.connector import cursor

# Setting the database class 
class RacingDao:
    db = ""
    def __init__(self):
        self.db = mysql.connector.connect(
            host = 'localhost',
            user= 'root',
            password = '',
            database ='datarepresentation'
        )
        
# Defining the creation process
    def create(self, horse):
        cursor = self.db.cursor()
        sql = "insert into horses (Horse, Jockey, Trainer, Age) values (%s,%s,%s,%s)"
        values = [
            horse['Horse'],
            horse['Jockey'],
            horse['Trainer'],
            horse['Age']    
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

# Defining the retreive all process
    def getAll(self):
        cursor = self.db.cursor()
        sql = 'select * from horses'
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        #print(results)
        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)

        return returnArray
# retrieving by id 
    def findById(self, Racenumber):
        cursor = self.db.cursor()
        sql = 'select * from Horses where Racenumber = %s'
        values = [ Racenumber ]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDict(result)
        
# updating the table
    def update(self, horse):
       cursor = self.db.cursor()
       sql = "update horses set Horse = %s, Jockey = %s, Trainer = %s, Age = %s where Racenumber = %s"
       values = [
            horse['Racenumber'],
            horse['Horse'],
            horse['Jockey'],
            horse['Trainer'],
            horse['Age']
       
       ]
       cursor.execute(sql, values)
       self.db.commit()
       return horse
# deleting the row
    def delete(self, Racenumber):
       cursor = self.db.cursor()
       sql = 'delete from horses where Racenumber = %s'
       values = [Racenumber]
       cursor.execute(sql, values)
       
       return {}



    def convertToDict(self, result):
        colnames = ['Racenumber','Horse', 'Jockey', 'Trainer','Age']
        horse = {}

        if result:
            for i , colName in enumerate(colnames):
                value = result[i]
                horse[colName] = value
        return horse

racingDAO = RacingDao()