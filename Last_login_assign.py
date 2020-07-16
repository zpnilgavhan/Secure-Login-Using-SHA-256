import mysql.connector as mysql
from datetime import date

password = input("Admin function,Enter master password")

db = mysql.connect(
        host = "localhost",
        user = "root",
        passwd = str(password)
    )
print("DB status : Available")
cursor = db.cursor()
cursor.execute("USE db1")
cursor.execute("TRUNCATE last_login")
cursor.execute("SELECT * FROM login_info")
databases = cursor.fetchall()
    ## it returns a list of all databases present
for database in databases:
        login_id = database[1]
        last_login_date = date.today()
        chances = 5
        #query = "INSERT INTO last_login(email,login_id, pswd) values(%s,%s,%s)" 
        query = "INSERT INTO last_login(login_id,last_login_date,chances) VALUES (%s,%s ,%s)"
        ## storing values in a variable
        values = (login_id,last_login_date,chances)
                            ## executing the query with values
        cursor.execute(query, values)
        #cursor.execute(query, (login_id,last_login_date,chances))\
        db.commit()
        print(cursor.rowcount, "Updated")
