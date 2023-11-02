#LIM JIA SHENG, TP067045
#DENNIS CHONG KEE KIAN, TP065544

import datetime
adminList = [["admin1","abc1","Jason"],
            ["admin2","abc2","Dennis"]]

#admin login page
def admin_login(adminList):
    print("")
    print(" --- ADMIN LOGIN PAGE ---")
    username = input("Enter your Username: ")
    password = input("Enter your Password: ")
    allRec = []
    ind = -1
    with open("adminlog.txt", "r") as f:
       for rec in f:
          allRec.append(rec.strip().split(":"))
    for cnt in range(len(allRec)):
       if (username == allRec[cnt][0]) and (password == allRec[cnt][1]):
          ind = cnt
    if (ind != -1):
        print("**************** ADMIN SYSTEM **************** \n")
        print("Logged in Successfully!")
        print("Welcome back",username)
        print("")
        admin_menu()
    else:
        print("Login failed, credential not valid")
        main_menu()






#admin menu
def admin_menu():
    print(" --- ADMIN MENU ---")
    print("1. Add item category")
    print("2. Modify item")
    print("3. Delete item")
    print("4. View/Search customer order")
    print("5. View/Search customer payment" )
    print("6. Order Delivery Management")
    print("7. Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        add_item_category()
    elif ch == 2:
        modify_item()
    elif ch == 3:
        remove_item()
    elif ch == 4:
        view_search_cust_order()
    elif ch == 5:
        view_search_cust_payment()
    elif ch == 6:
        odm()
    elif ch == 7:
        print("End of program \n")
        main_menu()
    else:
        print("Wrong input!")
        print("Wrong choice! \n")
        main_menu()
            
    

    


#register page   
def register():    
     print("")
     print("--- REGISTER PAGE ---")
     username = input("Enter Username: ")
     password = input("Enter password: ")
     password1 = input("Confirm password: ")

     if password == password1:
        
         with open("credentials.txt", "a") as f:
             rec = username +":"+password
             f.write(rec +"\n")
             print("You have registered successfully!")
         login()
     else:
         print("Password is not same as above! \n")
         register()






#login page and access to view all item details and place order function
def login():
     print("")
     print("--- LOGIN PAGE ---")
     username = input("Enter your Username: ")
     password = input("Enter your Password: ")
     allRec = []
     ind = -1
     with open("credentials.txt", "r") as f:
        for rec in f:            
           allRec.append(rec.strip().split(":"))
     for cnt in range(len(allRec)):
        if (username == allRec[cnt][0]) and (password == allRec[cnt][1]):            
           ind = cnt
     if (ind != -1):                                 
         print("")
         print("Logged in Successfully!")
         print("Welcome Back," + username)
         print("Happy Shopping!")
         print("")   
         print(" --- Welcome to Jason and Dennis ALL IT APU Online Shopping Mall ---")
         print("1. View all item details")
         print("2. Place order")
         print("3. Exit")
         ch = int(input("Enter your choice: "))
         if ch == 1:         
             with open("item_Details.txt", "r")as f:
                 print(f.read())
                 placeorder = input("Do you want to place an order? (yes/no): ")
                 if placeorder == "yes":
                     place_order()
                 elif placeorder == "no":
                    print("Back to main menu!")
                    main_menu()
                 else:
                     print("Wrong Input!")
                     main_menu()
                 
         elif ch == 2:                    
             place_order()
         elif ch == 3:
             print("End of program \n")
             main_menu()
         else:
             print("Wrong input!")
             main_menu()
     else:
         print("Login failed \n")
         main_menu()
     






#view all items page and access to register page    
def view_all_items():    
    print("")
    print(" --- VIEW ALL ITEM PAGE ---")
    print("")
    f=open("Category_Details.txt", "r")
    print(f.read())
    f.close()
    print("")
    f=open("All_items.txt", "r")
    print(f.read())
    f.close()
    print("")
    print("1.Registered")
    print("2.Unregistered")
    print("3.Back")
    print("")
    ch = int(input("Please enter your choice:"))
    if ch == 1:
        login()
    elif ch == 2:
        print("")
        print("1. Register to access more details")
        print("2. Exit")
        ch = int(input("Please enter your choice:"))
        if ch == 1:
            register()
        else:
            print("Exit to main menu")
            main_menu()
                
    elif ch == 3:
        print("Back to main menu")
        main_menu()
    else:
        print("Wrong Input \n")
        main_menu()








#allow registered user to place order 
def place_order():
    shoppingDict = {}

    my_file = open("All_items.txt")
    file_line = my_file.readline()
    itemsAvailable = my_file.readlines()
    my_file.close()
    
    email = input("Enter your email address:")
    phone_no = input("Enter your phone number:")
    print("")
    print("*********** Items Available in Our Store ************ \n")
    print("Item Code: Item Name: Item Type: Item Quantity: Item Price")
    for item in itemsAvailable:
        itmCode = item.split(":")[0]
        itmName = item.split(":")[1]
        itmType = item.split(":")[2]
        itmQuantity = item.split(":")[3]
        itmPrice = item.split(":")[4]

        print(f"{itmCode}: {itmName}: {itmType}: {itmQuantity}: {itmPrice}")

        
    allRec = []
    with open("All_items.txt", "r") as f:
        for rec in f:
            allRec.append(rec.strip().split(":"))
    proceedShopping = input("Do you wish to proceed (y/n): ").lower()
    while (proceedShopping == "y"):
        item_added = input("Enter item code to place order: ")
        ind = -1
        for cnt in range(len(allRec)):
            if (item_added in allRec[cnt][0]):
                ind = cnt
        if (ind != -1):
            item_qty = int(input(allRec[ind][0] +":"+ allRec[ind][1] +":"+ allRec[ind][2] +":"+ allRec[ind][3] +":"+ allRec[ind][4] +" >"+ " Enter quantity: "))
            shoppingDict.update({"Item: "+item_added:{"quantity":item_qty,"subtotal(RM)":float(allRec[ind][4])*item_qty}})
            print(shoppingDict)
            ind1 = -1
            for cnt1 in range(len(allRec)):
                if (item_qty <= int(allRec[ind][3])):
                    ind1 = cnt1
            if (ind1 != -1):
                ori_qty = allRec[ind][3]
                new_qty = int(ori_qty) - item_qty
                allRec[ind][3] = str(new_qty)
                with open("All_items.txt","w") as f:
                    for recList in allRec:
                        rec = ":".join(recList) + "\n"
                        f.write(rec)
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ADD CART SUCCESSFUL~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            else:
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~FAIL TO ADD CART~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("Item stock quantity not enough!!")
                print("Please re-enter the quantity of product needed according to our stock quantity.")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~PLEASE PLACE ORDER AGAIN~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                place_order()
        else:
            print("Item not found. Please try again.")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~GOING BACK ORDER PAGE~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            place_order()

        proceed_Shopping = input("Do you wish to add more items(y/n): ").lower()
        if (proceed_Shopping == "y"):
            continue
        else:
            print("\n\n")
            print("********************************Bill Summary********************************")
            print("***************JASON AND DENNIS ALL IT APU ONLINE SHOPPING MALL***************")
            print("Item\t\t\t\tQuantity\t\t\tSubtotal")
            total = 0
            for record in shoppingDict:
                print(f"{record}\t\t\t{shoppingDict[record]['quantity']}\t\t\t{shoppingDict[record]['subtotal(RM)']}")
                total = shoppingDict[record]['subtotal(RM)']+total
                print(f"Total: {total}")
            proceedpayment = input("Do u wish to proceed payment (y/n):")
            if proceedpayment.lower() == "y":
                payment_method = input("Enter your payment method (Debit/Credit) card:")            
                card_no = int(input("Enter your " + payment_method + " card number:"))
                cfm_payment = input("Comfirm payment? (yes/no) :")
                if cfm_payment.lower() == "yes":
                    with open("cust_order.txt", "a") as f:
                        rec = email + "/" + phone_no + "/" + str(shoppingDict) + "/"
                        f.write(rec + "\n")            
                    cfm_payment = "paid" + ", " + str(datetime.datetime.now())
                    with open("cust_payment.txt", "a") as f:
                        info = email + ", " + phone_no + ", " + str(total) + ", " + payment_method + ", " + str(card_no) + ", " + cfm_payment
                        f.write(info + "\n")

                    print("")
                    print("*********** Thank You ***********")
                    print("Hope to see you back soon!")
                    main_menu()
                else:
                    print("Exit to main menu")
                    main_menu()
            
            else:
                print("Back to main menu")
                main_menu()
            break                  











#delivery staff login page
def delivery_staff_login():
    print("")
    print(" --- LOGIN PAGE FOR DELIVERY STAFF ---")
    username = input("Enter your username:")
    password = input("Enter your password:")
    allRec = []
    ind = -1
    with open("stafflog.txt", "r") as f:
       for rec in f:
          allRec.append(rec.strip().split(":"))
    for cnt in range(len(allRec)):
       if (username == allRec[cnt][0]) and (password == allRec[cnt][1]):
          ind = cnt
    if (ind != -1):
        print("Logged in Successfully!")
        print("Welcome back", username)
        delivery_staff_system()
    else:
        print("Login failed, credential not valid")
        main_menu()









#allow admin to add items in inventory
def add_item_category():
    with open("All_items.txt", "r") as f:
        print("")
        print(" " + "--- ITEM LIST ---")
        print("")
        print("Code : Item : Type : Quantity : Price(RM) \n")
        print(f.read())
    with open("All_items.txt", "a") as f:
        print(" --- ADD ITEM CATEGORY ---")
        itmCode = input("Please enter new ITEM CODE:")
        itmName = input("Please enter new ITEM NAME:")
        itmType = input("Please enter new ITEM TYPE (Electronic Gadget/Home Appliance):")
        itmQuantity = input("Please enter new ITEM QUANTITY:")
        itmPrice = input("Please enter new ITEM PRICE:")
        rec = itmCode+":"+itmName+":"+itmType+":"+itmQuantity+":"+itmPrice
        f.write(rec + "\n")
        print(rec + " " + "has been successfully added")
    admin_menu()






#allow admin to modify items in inventory
def modify_item():
    with open("All_items.txt" ,"r") as f:
        print("")
        print(" " + "--- ITEM LIST ---")
        print("")
        print("Code : Item : Type : Quantity : Price(RM) \n")
        print(f.read())
        
    allRec = []
    with open("All_items.txt","r") as f:
        for rec in f:
            allRec.append(rec.strip().split(":"))
    print(" --- MODIFY ITEM ---")
    itmCode = input("Please enter the ITEM CODE to modify: ")
    ind = -1
    for cnt in range(len(allRec)):
        if (itmCode == allRec[cnt][0]):
            ind = cnt
    if (ind != -1):
        newName = input(allRec[ind][1] + " Please enter new name: ")
        newType = input(allRec[ind][2] + "Please enter new type(Electronic Gadget/Home Appliance: ")
        newQuantity = input(allRec[ind][3] + "Please enter new quantity: ")
        newPrice = input(allRec[ind][4] + "Please enter new price: ")
        allRec[ind][1] = newName
        allRec[ind][2] = newType
        allRec[ind][3] = newQuantity
        allRec[ind][4] = newPrice
        print("Modify Successfully")
    else:
        print("Record Not Found")
        admin_menu()
        
    with open("All_items.txt","w") as f:
         for recList in allRec:
             rec = ":".join(recList) + "\n"
             f.write(rec)
    admin_menu()






#allow admin to remove items in inventory
def remove_item():
    with open("All_items.txt", "r") as f:
        print("")
        print(" " + "--- ITEM LIST ---")
        print("")
        print(f.read())
        
    allRec = []
    with open("All_items.txt","r") as f:
        for rec in f:
            allRec.append(rec.strip().split(":"))
    print(" --- REMOVE ITEM ---")
    itmCode = input("Please enter item code to delete: ")
    ind = -1
    for cnt in range(len(allRec)):
        if (itmCode == allRec[cnt][0]):
            ind = cnt
    if (ind != -1):
        print("Item Code: "+ allRec[ind][0])
        print("Item Name: "+ allRec[ind][1])
        print("Item Type: "+ allRec[ind][2])
        print("Item Quantity: "+ allRec[ind][3])
        print("Item Price: "+ allRec[ind][4])
        ch = input("Are you sure to delete this item? (y/n): ")
        if (ch == "y"):
            print(rec + "has been removed successfully")
            with open("All_items.txt","w") as f:
                for cnt in range(len(allRec)):
                    if (cnt != ind):
                        rec = ":".join(allRec[cnt]) + "\n"
                        f.write(rec)
            admin_menu()
        else:
            print("Back to admin menu")
            admin_menu()
              
    else:
        print("Record Not Found")
        admin_menu()

   





#allow admin to view and search customer order
def view_search_cust_order():
    print("")
    print("1. View customer order history")
    print("2. Search customer order history")
    print("3. Back")
    ch = int(input("Enter your choice:"))
    if ch == 1:
        with open("cust_order.txt", "r") as f:
            print("")
            print(f.read())
            print("1. Back to admin menu")
            print("2. Exit to main menu")
            ch = int(input("Enter your choice: "))
            if ch == 1:
                admin_menu()
            elif ch == 2:
                main_menu()
            else:
                print("Wrong input")
                main_menu()                       
                       
    elif ch == 2:
        search_cust_order()
    elif ch == 3:
        print("")
        print("Back to admin menu")
        admin_menu()
    else:
        print("Wrong choice!")
        admin_menu()
        
 
def search_cust_order():
    with open("cust_order.txt" , "r") as f:
        print("")
        print(f.read())
        
    allRec = []
    with open("cust_order.txt" , "r") as f:
        for rec in f:
            allRec.append(rec.strip().split("/"))
    search = input("Enter email to search customer order: ")
    ind = -1
    for cnt in range(len(allRec)):
        if (search == allRec[cnt][0]):
            ind = cnt                              
    if (ind != -1):
        print("Email: " + allRec[ind][0])
        print("Phone No: " + allRec[ind][1])
        print("Order: " + allRec[ind][2])
        admin_menu()
    else:
        print("Record not found!")
        admin_menu()
    






#allow admin to view and search customer payment
def view_search_cust_payment():
    print("")
    print("1. View customer payment history")
    print("2. Search customer payment history")
    print("3. Back")
    ch = int(input("Enter your choice:"))
    if ch == 1:
        with open("cust_payment.txt", "r") as f:
            print("")
            print(f.read())
            view_search_cust_payment()
    elif ch == 2:
        with open("cust_payment.txt" , "r") as f:
            print("")
            print(f.read())
        
        allRec = []
        with open ("cust_payment.txt" , "r") as f:
            for rec in f:
                allRec.append(rec.strip().split(","))
        search = input("Enter email to search customer payment: ")
        ind = -1
        for cnt in range(len(allRec)):
            if (search == allRec[cnt][0]):
                ind = cnt                              
        if (ind != -1):
            print("Email: " + allRec[ind][0])
            print("Phone No: " + allRec[ind][1])
            print("Total Amount(RM): " + allRec[ind][2])
            print("Payment Method: " + allRec[ind][3])
            print("Card No: " + allRec[ind][4])
            print("Payment Status: " + allRec[ind][5])
            print("Payment Record Date and Time: " + allRec[ind][6])
        else:
            print("Record not found!")
            view_search_cust_payment()
    elif ch == 3:
        print("Back to admin menu")
        admin_menu()
    else:
        print("Wrong choice!")
        admin_menu()
    view_search_cust_payment()





    
#allow delivery staff to select customer order and update the delivery status 
def delivery_staff_system():
    print("")
    print(" --- DELIVERY STAFF SYSTEM ---")
    with open("cust_order.txt" ,"r") as f:
        print("")
        print(f.read())
            
    allRec = []
    with open("cust_order.txt","r") as f:
        for rec in f:
            allRec.append(rec.strip().split("/"))
    print(" --- SELECT CUSTOMER ORDER TO UPDATE DELIVERY STATUS ---")
    cust_email = input("Enter customer email to select: ")
    ind = -1
    for cnt in range(len(allRec)):
        if (cust_email == allRec[cnt][0]):
            ind = cnt
    if (ind != -1):
        delivery_status = input("Do you sure you want to update the delivery status? (yes/no): ")
        if delivery_status.lower() == "yes":
            ch = int(input(allRec[ind][3] + "Enter number to update the following status (1.Shipped, 2.Delivered 3.Cancelled): "))
            if ch == 1:
                ch = "Shipped"
                allRec[ind][3] = ch
                print("Updated Successfully")
            elif ch == 2:
                ch = "Delivered"
                allRec[ind][3] = ch
                print("Updated Successfully")
            elif ch == 3:
                ch = "Cancelled"
                allRec[ind][3] = ch
                print("Updated successfully")
            else:
                print("Wrong Input! Please enter number 1 up to 3 to update following status")
                delivery_staff_system()

        elif delivery_status.lower() == "no":
            main_menu()
        else:
            print("Wrong Input!")
            main_menu()
            

    else:
        print("Record Not Found")
        delivery_staff_system()
            
    with open("cust_order.txt","w") as f:
            for recList in allRec:
                rec = "/".join(recList) + "\n"
                f.write(rec)








#allow admin to access the function of order delivery management system       
def odm():
    print("")
    print(" --- ORDER DELIVERY MANAGEMENT SYSTEM --- \n")
    print("1. Add delivery staff")
    print("2. Modify delivery staff")
    print("3. Delete delivery staff")
    print("4. Assign orders to delivery staff")
    print("5. Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        with open("stafflog.txt", "r") as f:
            print("")
            print(" --- DELIVERY STAFF LIST ---")
            print("")
            print("ID-PASSWORD-NAME \n")
            print(f.read())
        with open("stafflog.txt", "a") as f:
            print(" --- ADD DELIVERY STAFF ---")
            staffid = input("Please enter new delivery staff ID:")
            staffpass = input("Please enter new delivery staff PASSWORD:")
            staffname = input("Please enter new delivery staff NAME:")
            rec = staffid + ":" + staffpass + ":" + staffname 
            f.write(rec + "\n")
            print(rec + " " + "has been successfully added")
        odm()
        
    elif ch == 2:
        with open("stafflog.txt" ,"r") as f:
            print("")
            print(" --- DELIVERY STAFF LIST ---")
            print("")
            print("ID-PASSWORD-NAME \n")
            print(f.read())
        
        allRec = []
        with open("stafflog.txt","r") as f:
            for rec in f:
                allRec.append(rec.strip().split(":"))
        print(" --- MODIFY DELIVERY STAFF ---")
        staffid = input("Please enter the staff ID to modify: ")
        ind = -1
        for cnt in range(len(allRec)):
            if (staffid == allRec[cnt][0]):
                ind = cnt
        if (ind != -1):
            newId = input(allRec[ind][0] + " Please enter new ID: ")
            newPass = input(allRec[ind][1] + "Please enter new PASSWORD: ")
            newName = input(allRec[ind][2] + "Please enter new NAME: ")
            allRec[ind][0] = newId
            allRec[ind][1] = newPass
            allRec[ind][2] = newName + ":"
            print("Modify Successfully")
        else:
            print("Record Not Found")
            odm()

            
        with open("stafflog.txt","w") as f:
            for recList in allRec:
                rec = ":".join(recList) + "\n"
                f.write(rec)
        odm()

                 
    elif ch == 3:
        with open("stafflog.txt", "r") as f:
            print("")
            print(" --- DELIVERY STAFF LIST ---")
            print("")
            print("ID-PASSWORD-NAME \n")
            print(f.read())
        
        allRec = []
        with open("stafflog.txt","r") as f:
            for rec in f:
                allRec.append(rec.strip().split(":"))
        print(" --- REMOVE DELIVERY STAFF ---")
        staffid = input("Please enter staff ID to delete: ")
        ind = -1
        for cnt in range(len(allRec)):
            if (staffid == allRec[cnt][0]):
                ind = cnt
        if (ind != -1):
            print("Staff ID: "+ allRec[ind][0])
            print("Staff Password: "+ allRec[ind][1])
            print("Staff Name: "+ allRec[ind][2])
            ch = input("Are you sure to delete this item? (y/n): ")
            if (ch == "y"):
                print(rec + "has been removed successfully")
                with open("stafflog.txt","w") as f:
                    for cnt in range(len(allRec)):
                        if (cnt != ind):
                            rec = ":".join(allRec[cnt]) + "\n"
                            f.write(rec)
                  
        else:
            print("Record Not Found")
            odm()
        odm()

    elif ch == 4:        
        print("")
        print(" ********** ASSIGN ORDER TO DELIVERY STAFF SYSTEM **********")
        with open("stafflog.txt" ,"r") as f:
            print("")
            print(" --- DELIVERY STAFF LIST ---")
            print("ID-PASSWORD-NAME-CUSTOMER EMAIL")
            print(f.read())
                
        allRec = []
        with open("stafflog.txt","r") as f:
            for rec in f:
                allRec.append(rec.strip().split(":"))
        print(" --- SELECT STAFF ID TO ASSIGN ORDER FOR DELIVER ---")
        staffid = input("Enter staff ID to select: ")
        ind = -1
        for cnt in range(len(allRec)):
            if (staffid == allRec[cnt][0]):
                ind = cnt
        if (ind != -1):
            with open("cust_order.txt", "r") as f:
                print("")
                print(" --- CUSTOMER ORDER LIST ---")
                print(f.read())
                cust_email = input(allRec[ind][3] + "Enter customer email to assign deliver order: ")
                allRec[ind][3] = cust_email
                print("Updated Successfully")
        else:
            print("Record Not Found")
            odm()
                
        with open("stafflog.txt","w") as f:
                for recList in allRec:
                    rec = ":".join(recList) + "\n"
                    f.write(rec)
        odm()
            
    elif ch == 5:
        print("Back to admin menu")
        admin_menu()
    else:
        print("Wrong Input!")
        admin_menu()
        


    
#main menu page
def main_menu():
    print("")
    print("********** MAIN MENU **********")
    print("1. Admin Login")
    print("2. Register")
    print("3. Login")
    print("4. View all items")
    print("5. Delivery Staff Login")
    print("6. Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        admin_login(adminList)
    elif ch == 2:
        register()
    elif ch == 3:
        login()
    elif ch == 4:
        view_all_items()
    elif ch == 5:
        delivery_staff_login()
    elif ch == 6:
        print("end of program")
   
    else:
        print("Wrong Choice! Please enter option 1-6!")
        main_menu()

    


while 1:
    main_menu()
    break




