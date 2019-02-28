users = {}
status = ""

def displayMenu():
    status = input("Are you a registered user? Y/N? Press q to Quit: ")
    if status == "Y":
        oldUser()
    elif status == "N":
        newUser()

def newUser():
    createLogin = input("Create Login Name: ")

    if createLogin in users:
        print("\nLogin name already exists!\n")
    else:
        createPassw = input("Create Password: ")
        users[createLogin] = createPassw
        print("\nUser created")


def oldUser():
    login = input("Enter Login name: ")
    passw = input("Enter Password: ")

    if login in users and users[login] == passw:
        print("\nLogin Successful!\n")
    else:
        print("\nUser doesn't exist or wrong password!\n")


while status != "q":
    displayMenu()

