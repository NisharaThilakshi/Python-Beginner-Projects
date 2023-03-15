import time

username = "nishara"
password = "darkhorse"

username_input = input("Please enter your Username: ")
password_input = input("Please enter your Password: ")


if username_input == username and password_input == password:
    print("Access Granted")
    print("Please wait")
    time.sleep(5)
    print("Ok...Loading...")
    time.sleep(1)
    print("..............")
    time.sleep(1)
    print("..............")
    print("Alright you have the security clearance. Pulling up the secret mainframe.")

elif username_input == username and password_input != password:
    print("Invalid password")

elif username_input != username and password_input == password:
    print("Invaild Username")

else:
    print("You might wanna check both fields...")
