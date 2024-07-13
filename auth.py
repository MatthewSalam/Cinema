import mysql.connector
import operations

user_id = 0
con  = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "cinema_db")
cursor = con.cursor()


def insert_details(user_name, email, password):

    sql = (f"INSERT INTO `users`(`user_name`, `email`, `password`) VALUES ('{user_name}','{email}','{password}')")
    cursor.execute(sql)
    con.commit()
    print("User details inputted")
    return

def validate_user_details(username,password):
    sql = (f"SELECT user_name,password FROM `users` WHERE `user_name` = '{username}'")
    cursor.execute(sql)
    # con.commit()
    result = cursor.fetchone()
    # return True

    if username != result[0] or password != result[1] :
       print("Invalid username or password")
       login()
    return

def login():
    username = input("Enter your username:  ")
    password = input("Enter your password:  ")
    validate_user_details(username,password)
    operations.tikOperation()
    return

def create_account():
    global user_id
    
    user_id = user_id + 1
    user_name = input("Enter your username:  ")  
    email = input("Enter your email:   ")
    password = input("Enter your password:  ")
    insert_details(user_name, email, password)
    print("Account created successfully")
    operations.tikOperation()
