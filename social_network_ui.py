# You can implement user interface functions here.

def mainMenu():
    print("")
    print("1. Create a new account")
    print("2. Manage my account")
    print("3. Save and quit")
    print("********************************************************")
    return input("Please Choose a number: ")

def manageAccountMenu():
    print("")
    print("1. Edit my details")
    print("2. Add a friend")
    print("3. View all my friends")
    print("4. View all my messages")
    print("5. Send message")
    print("6. Block a friend")
    print("7. <- Go back ")
    return input("Please Choose a number: ")

def editDetailsMenu():
    print("")
    print("1. Change username")
    print("2. Change age")
    print("3. Password")
    print("4. <- Go back ")
    return input("Please Choose a number: ")