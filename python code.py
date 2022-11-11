def register():
    db = open("database.txt","r")
    Username = input("Create username: ")
    Password = input("Create password: ")
    Password1 =      input("Comfirm password: ")
  
    if Password != Password1:
        print("Password don't match, restart")
        register()
    else:
        if len(Password)<1:
            print("Password too short, restart")
            register()
        elif Username in db:
            print("Username exists")
            register()
        else:
            db = open("database.txt", "a")
            db.write(Username+","+Password+"\n")
            print("Registered Success!")
register()
            
def login():
    db = open("database.txt", "r")
    Username = input("Enter your Username: ")
    Password = input("Enter your Password: ")

    if Password == data[Username]:
              print("Login Successfully")
              print("Welcome ",Username)
    else:
        print("Password or Username incorrect")
    
while 1:
    print("********** Login System **********")
    print("1.Register")
    print("2.Login")
    print("3.View all items")
    print("4.Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        register()
    elif ch == 2:
        login()
    elif ch == 3:
        view_all_items()
    elif ch == 4:
        print("end of program")
        break
    else:
        print("Wrong Choice!")
        print("Wrong input.")
