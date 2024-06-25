import connectAndModify
import sqlite3
import sys

# menu function, this enables us to call this again if needed instead of having repetitive code
def menu():
    print("------------- Larry's Database -------------\n\
    Choose any of the following operations:\n\
    1. Add Customer\n\
    2. Add Employee\n\
    3. Add Sale\n\
    4. Add Inventory\n\
    5. Show all Customer Data\n\
    6. Show all Employee Data\n\
    7. Show all Sales Data\n\
    8. Show all Inventory Data\n\
    9. Show customer with first- and lastname\n\
    10. Show employee ID and last name\n\
    11. Show sale by Description and Price for more than 2 sales per item\n\
    12. Show inventory descriptions.. \n\
    13. Delete customer\n\
    14. Delete employee\n\
    15. Delete sale record\n\
    16. Delete inventory record\n\
    17. Update customer first name\n\
    18. Update customer last name\n\
    19. Update employee first name\n\
    20. Update employee last name\n\
    21. Update sales total\n\
    22. Update sales quantity\n\
    23. Update item price in inventory\n\
    24. Update item description in inventory\n\
    25. Exit Program\n\
    ")

def main():
    connection = connectAndModify.connect()
    menu()
    choice = int(input("Enter your choice: "))
    # as long as we do not select exit, check for choices not equal to 25
    while (choice != 25):
        # The following conditionals evaluate which choice was chosen and execute the following menu commands
        if choice == 1:
            CID = int(input("Enter a Customer ID: \n"))
            CFname = input("Enter a first name: \n")
            CLname = input("Enter a last name: \n")
            connectAndModify.add_customer(connection, CID, CFname, CLname)
            break # break statements are necessary to break out of the loop
        elif choice == 2:
            EID = int(input("Enter an Employee ID: \n"))
            EFname = input("Enter a first name: \n")
            ELname = input("Enter a last name: \n")
            connectAndModify.add_employee(connection, EID, EFname, ELname)
            break # break statements are necessary to break out of the loop
        elif choice == 3:
            SID = int(input("Enter a Sale ID: \n"))
            SQty = int(input("Enter sales quantity: \n"))
            STotal = input("Enter a sales total: \n")
            CID = int(input("Enter a Customer ID: \n"))
            IID = int(input("Enter an Inventory ID: \n"))
            EID = int(input("Enter an Employee ID: \n"))
            connectAndModify.add_sales(connection, SID, SQty, STotal, CID, IID, EID)
            break # break statements are necessary to break out of the loop
        elif choice == 4:
            IID = int(input("Enter an Inventory ID: \n"))
            IDesc = input("Enter a description: \n")
            IPrice = input("Enter a price: \n")
            connectAndModify.add_inventory(connection, IID, IDesc, IPrice)
            break # break statements are necessary to break out of the loop
        elif choice == 5:
            print("Showing data from all customers.... \n")
            print(connectAndModify.get_all_customers(connection))
            break # break statements are necessary to break out of the loop
        elif choice == 6:
            print("Showing data from all employees... \n")
            print(connectAndModify.get_all_employees(connection))
            break # break statements are necessary to break out of the loop
        elif choice == 7:
            print("Showing data from all sales... \n")
            print(connectAndModify.get_all_sales(connection))
            break # break statements are necessary to break out of the loop
        elif choice == 8:
            print("Showing data from the whole inventory... \n")
            print(connectAndModify.get_all_inventory(connection))
            break # break statements are necessary to break out of the loop
        elif choice == 9:
            print("Customer first- and lastname \n")
            print(connectAndModify.get_customer_by_last_name(connection))
            break # break statements are necessary to break out of the loop
        elif choice == 10:
            print("Employee ID and lastname")
            print(connectAndModify.get_employee_ID_last_name(connection))
            break # break statements are necessary to break out of the loop
        elif choice == 11:
            print("Sales records with at least 2 items sold: \n")
            print(connectAndModify.show_sales_inventory(connection))
            break # break statements are necessary to break out of the loop
        elif choice == 12:
            print("Inventory Descriptions... \n")
            print(connectAndModify.get_inventory(connection))
            break # break statements are necessary to break out of the loop
        elif choice == 13:
            CID = int(input("Enter customer's ID to delete record: "))
            connectAndModify.delete_customer(connection, CID)
            break # break statements are necessary to break out of the loop
        elif choice == 14:
            EID = int(input("Enter employee's ID to delete record: "))
            connectAndModify.delete_employee(connection, EID)
            break # break statements are necessary to break out of the loop
        elif choice == 15:
            SID = int(input("Enter sales's ID to delete record: "))
            connectAndModify.delete_sale(connection, SID)
            break # break statements are necessary to break out of the loop
        elif choice == 16:
            IID = int(input("Enter inventory's ID to delete record: "))
            connectAndModify.delete_inventory(connection, IID)
            break # break statements are necessary to break out of the loop
        elif choice == 17:
            CID = int(input("Enter customer's ID to change record: \n"))
            CFname = input("Enter a new first name: \n")
            connectAndModify.update_customer_fname(connection, CFname, CID)
            break # break statements are necessary to break out of the loop
        elif choice == 18:
            CID = int(input("Enter customer's ID to change record: \n"))
            CLname = input("Enter a new last name: \n")
            connectAndModify.update_customer_lname(connection, CLname, CID)
            break # break statements are necessary to break out of the loop
        elif choice == 19:
            EID = int(input("Enter employee's ID to change record: \n"))
            EFname = input("Enter a new first name: \n")
            connectAndModify.update_employee_fname(connection, EFname, EID)
            break # break statements are necessary to break out of the loop
        elif choice == 20:
            EID = int(input("Enter employee's ID to change record: \n"))
            ELname = input("Enter a new last name: \n")
            connectAndModify.update_employee_lname(connection, ELname, EID)
            break # break statements are necessary to break out of the loop
        elif choice == 21:
            SID = int(input("Enter sales ID to change record: \n"))
            STotal = input("Enter a new total amount: \n")
            connectAndModify.updates_sales_total(connection, STotal, SID)
            break # break statements are necessary to break out of the loop
        elif choice == 22:
            SID = int(input("Enter sales ID to change record: \n"))
            SQty = int(input("Enter a new sales quantity: \n"))
            connectAndModify.update_sales_qty(connection, SQty, SID)
            break # break statements are necessary to break out of the loop
        elif choice == 23:
            IID = int(input("Enter an Inventory ID to change record: \n"))
            IPrice = input("Enter a new Price for item: \n")
            connectAndModify.update_intentory_price(connection, IPrice, IID)
            break # break statements are necessary to break out of the loop
        elif choice == 24:
            IID = int(input("Enter an Inventory ID to change record: \n"))
            IDesc = input("Enter a new description for item: \n")
            connectAndModify.update_inventory_desc(connection, IDesc, IID)           
            break # break statements are necessary to break out of the loop
        # Will prompt the user to enter choice again if entry is below 0, 0 or greater than 25
        else:
            print('Wrong Entry, try again.')
            main()
    # forces to exit program when choice is 25
    if (choice == 25):
        sys.exit("Ending Program...")
    main()
main()
