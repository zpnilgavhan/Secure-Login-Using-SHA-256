import os
import otp_generator as ms
import hashlib

def secure_login():
    entered_username = input("Enter USERNAME : ")
    entered_password = input("Enter PASSWORD : ")
    hashed_password = hashlib.sha256(entered_password.encode()).hexdigest()
    import mysql.connector as mysql

    db = mysql.connect(
        host = "localhost",
        user = "root",
        passwd = "Khemraj@1"
    )
    print("DB status : Available")
    cursor = db.cursor()
    cursor.execute("USE db1")
    ## executing the statement using 'execute()' method
    cursor.execute("SELECT * FROM login_info")

    ## 'fetchall()' method fetches all the rows from the last executed statement
    databases = cursor.fetchall() ## it returns a list of all databases present
    logged_in = 0;
    ## showing one by one database
    for database in databases:
        if(database[1]== entered_username):
            print("User Found ")
            if(database[2] == hashed_password):
                print("Password Matched ")
                #update last login info
                sql_select_query = """select * from last_login where login_id = %s"""
                cursor.execute(sql_select_query, (str(database[1]),))
                record = cursor.fetchall()
                print("SELECTED")
                ##print(record[0][1])
                #query = "UPDATE login_info SET pswd = %s WHERE login_id = %s"
                #cursor.execute(query, (str(hashed_password.hexdigest()),database[1]))
                #db.commit()
                return True
            else :
                print("Password Unmatched")
                choice = 2
                choice = int(input("1 to reset password \n2 to leave"))
                if(choice == 2):
                    return False
                else : 
                    otp1 = ms.otp_generator(database[0])
                    otp2 = input("Enter OTP : ")
                    if(otp1 == otp2):
                        print("matched")
                        password = input("Enter NEW PASSWORD : ")
                        hashed_password = hashlib.sha256(password.encode())
                        ## defining the Query
                        query = "UPDATE login_info SET pswd = %s WHERE login_id = %s"
                        ## executing the query with values
                        cursor.execute(query, (str(hashed_password.hexdigest()),database[1]))

                        ## to make final output we have to run the 'commit()' method of the database object
                        db.commit()

                        print(cursor.rowcount, "Password Changed Successfully")
                        print("Redirected to login")
                        return secure_login()
    while logged_in == 0 : 
            choice = int(input("1 to sign Up \n2 to leave :"))
            if(choice == 2):
                return False
            else :
                    email = input("Enter your mail id")
                    print("SENDING OTP ")
                    otp1 = ms.otp_generator(email)
                    otp2 = input("Enter OTP : ")
                    if(otp1 == otp2):
                            user_name_is_unique = False
                            print("oTP matched")
                            while(user_name_is_unique == False):
                                username = input("Enter New Username : ")
                                new_cursor = db.cursor()
                                new_cursor.execute("SELECT * FROM login_info")

                                ## 'fetchall()' method fetches all the rows from the last executed statement
                                databases = new_cursor.fetchall() ## it returns a list of all databases present
                                ## showing one by one database
                                found = False
                                for database in databases:
                                    if(database[1] ==  username):
                                        print("Username Unavailable")
                                        found = True
                                        break
                                if(found == False):
                                    print("Username Available")
                                    user_name_is_unique = True
                            password = input("Enter NEW PASSWORD : ")
                            hashed_password = hashlib.sha256(password.encode()) 
                            ## defining the Query
                            query = "INSERT INTO login_info (email,login_id, pswd) VALUES (%s,%s , %s)"
                            ## storing values in a variable
                            values = (email,username, str(hashed_password.hexdigest()))

                            ## executing the query with values
                            cursor.execute(query, values)

                            ## to make final output we have to run the 'commit()' method of the database object
                            db.commit()

                            print(cursor.rowcount, "Signed Up Successfully")
                            print("Redirected to login")
                            return secure_login()
                    else :
                        print("OTP Unmatched")
                        otp2 = input("Try again: ")
                        if(otp1 == otp2):
                            user_name_is_unique = False
                            print("oTP matched")
                            while(user_name_is_unique == False):
                                username = input("Enter New Username : ")
                                new_cursor = db.cursor()
                                new_cursor.execute("SELECT * FROM login_info")

                                ## 'fetchall()' method fetches all the rows from the last executed statement
                                databases = new_cursor.fetchall() ## it returns a list of all databases present
                                ## showing one by one database
                                found = False
                                for database in databases:
                                    if(database[1] ==  username):
                                        print("Username Unavailable")
                                        found = True
                                        break
                                if(found == False):
                                    print("Username Available")
                                    user_name_is_unique = True
                            password = input("Enter NEW PASSWORD : ")
                            hashed_password = hashlib.sha256(password.encode()) 
                            ## defining the Query
                            query = "INSERT INTO login_info (email,login_id, pswd) VALUES (%s,%s , %s)"
                            ## storing values in a variable
                            values = (email,username, str(hashed_password.hexdigest()))

                            ## executing the query with values
                            cursor.execute(query, values)

                            ## to make final output we have to run the 'commit()' method of the database object
                            db.commit()

                            print(cursor.rowcount, "Signed Up Successfully")
                            print("Redirected to login")
                            return secure_login()
                        else :
                            print("OTP unmatched,you exhausted chances,plaese come back again after same time")
                            return False
    return False
        

