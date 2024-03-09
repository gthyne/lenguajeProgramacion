
import mysql.connector
import os

class MYSQLDB:
   def __int__(self, host, user, password, database):
    self.host= host
    self.user= user
    self.password= password
    self.database= database
    self.connection = None

   def connector(self):
     try:
       if(self.connection == None):
         self.connection = mysql.connector.connect(
           host=self.host,
           user=self.User,
           password = self.password,
           database=self.database
        )
         os.system("color a3")
         print("wow, me connecte")
     except mysql.connector.error as Error:
          print("error mientras se estaba conectando")
          db =MYSQLDB("localhost","root","","dbtestlp")
          print("connectado")
def disconnect(self):
   try:
      if self.connection:
         self.connection.close
         self.connection = None
   except mysql.connector.error as error:
    print("error")
    
    def execute_query(self, query, params=None):
        try:
                cursos = self.connection.cursos()
                cursos = execute(query, params)
                result = cursos.fetchall()
    return result
   except mysql.connector.error as error:
         print(f"error: {error}")

         db =MYSQLDB("localhost", "root", "", "testtl")
         print("conectado")

         db.connect()
         categorias = db.execute_query("select * from categorias")

for reg in categorias
    print(reg)
