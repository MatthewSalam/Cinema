import mysql.connector
import operations

#Allowing the initial userid to be zero
user_id = 0
con  = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "cinema_db")
cursor = con.cursor()


def insert_details(user_name, email, password):
    #Appending thhe details into the database
    sql = (f"INSERT INTO `users`(`user_name`, `email`, `password`) VALUES ('{user_name}','{email}','{password}')")
    cursor.execute(sql)
    con.commit()
    print("User details inputted")
    return

def validate_user_details(username,password):
    #Making sure the user details inputted match the ones in the DB
    sql = (f"SELECT user_name,password FROM `users` WHERE `user_name` = '{username}'")
    cursor.execute(sql)
    # con.commit()
    result = cursor.fetchone()
    # return True

    if username != result[0] or password != result[1] :
        #Making sure the user inputs correct username or password
       print("Invalid username or password")
       login()
    return

def login():
    #Allowing the user attempt to login and validating if they are in the database 
    username = input("Enter your username:  ")
    password = input("Enter your password:  ")
    validate_user_details(username,password)
    operations.tikOperation()
    return

def create_account():
    #Allowing user create his accont in the database if He/She is new
    global user_id
    user_id = user_id + 1
    user_name = input("Enter your username:  ")  
    email = input("Enter your email:   ")
    password = input("Enter your password:  ")
    insert_details(user_name, email, password)
    print("Account created successfully")
    operations.tikOperation()

def movie_status():
    movies_available = ["Black Panther", "Infinity War", "Endgame", "The Eternals", "Homecoming", "Far from Home", "No way Home", "Guardians of the Galaxy", "Deadpool and Wolverine", "Antman and the Wasp: Quantumania"]
    print(f"Movies: ", movies_available)
    movie = str(input("What movie do you want to watch:  "))
    if movie in movies_available:
      print("Movie ticket is available")
    else:
      print("Sorry, movie is not available")
    user_recognition = input("Are you a registered user:  ")
    if user_recognition == "yes":
      print("Login")
      login()
    elif user_recognition == "no":
      print("Account creation")
      create_account()
    else:
     print("Input yes or no")

