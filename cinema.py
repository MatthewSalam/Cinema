import auth 

print("Welcome to Filmhouse Cinemas")
movies_available = ["Black Panther", "Infinity War", "Endgame", "The Eternals", "Homecoming", "Far from Home", "No way Home", "Guardians of the Galaxy", "Deadpool and Wolverine", "Antman and the Wasp: Quantumania"]
movie = str(input("What movie do you want to watch:  "))
if movie in movies_available:
  print("Movie ticket is available")
else:
  print("Sorry, movie is not available")
user_recognition = input("Are you a registered user:  ")
print(user_recognition)
if user_recognition == "yes":
    print("Login")
    auth.login()
elif user_recognition == "no":
    print("Account creation")
    auth.create_account()
else:
     print("Input yes or no")

