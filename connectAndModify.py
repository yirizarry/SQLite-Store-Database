import sqlite3
import database

# SQL Statements

# Insert Additional records
INSERT_CUSTOMER = "INSERT INTO Customers (CID, CFname, CLname) VALUES (?, ?, ?);"
INSERT_EMPLOYEE = "INSERT INTO Employees (EID, EFname, ELname) VALUES (?, ?, ?);"
INSERT_SALES = "INSERT INTO Sales (SID, SQty, STotal, CID, EID, IID) VALUES (?, ?, ?, ?, ?, ?);"
INSERT_INVENTORY = "INSERT INTO Inventory (IID, IDesc, IPrice) VALUES (?, ?, ?);"

# Read Records from customers Table
SELECT_ALL_CUSTOMERS = "SELECT * FROM Customers;"
SELECT_CUSTOMER = "SELECT CFname, CLname FROM Customers;"

# Read Records from Employees Table
SELECT_ALL_EMPLOYEES = "SELECT * FROM Employees;"
SELECT_EMPLOYEE = "SELECT EID, ELname FROM Employees;"

# Read Records from Sales Table
SELECT_ALL_SALES = "SELECT * FROM Sales;"
SELECT_SALE = "SELECT * FROM Sales WHERE SID = ?;"

# Read Records from Inventory Table
SELECT_ALL_INVENTORY = "SELECT * FROM Inventory;"
SELECT_INVENTORY = "SELECT IDesc FROM Inventory;"

# Delete Records by ID
DELETE_CUSTOMER = "DELETE FROM Customers WHERE CID = ?;"
DELETE_EMPLOYEE = "DELETE FROM Employees WHERE EID = ?;"
DELETE_SALES = "DELETE FROM Sales WHERE SID = ?;"
DELETE_INVENTORY = "DELETE FROM Inventory WHERE IID = ?;"

# Update Records
CHANGE_CUSTOMER_FNAME = "UPDATE Customers SET CFname = ? WHERE CID = ?;"
CHANGE_CUSTOMER_LNAME = "UPDATE Customers SET CLname = ? WHERE CID = ?;"

CHANGE_EMPLOYEE_FNAME = "UPDATE Employees SET EFname = ? WHERE EID = ?;"
CHANGE_EMPLOYEE_LNAME = "UPDATE Employees SET ELname = ? WHERE EID = ?;"

CHANGE_SALES_QTY = "UPDATE Sales SET SQty = ? WHERE SID = ?;"
CHANGE_SALES_TOTAL = "UPDATE Sales SET STotal = ? WHERE SID = ?;"

CHANGE_INVENTORY_DESC = "UPDATE Inventory SET IDesc = ? WHERE IID = ?;"
CHANGE_INVENTORY_PRICE = "UPDATE Inventory SET IPrice = ? WHERE IID = ?;"

# Show results of sales records
SHOW_SALES_INVENTORY = "SELECT IDesc, IPrice FROM Inventory, Sales WHERE SQty >= 2;"

###########################################################
# connection to database ##################################
###########################################################
def connect():
	return sqlite3.connect('larrys_store.db')
	#cursor = connection.cursor()

###########################################################
############ This section is for adding Records ###########
###########################################################
# function to add customer records
def add_customer(connection, CID, CFname, CLname):
	with connection:
		connection.execute(INSERT_CUSTOMER, (CID, CFname, CLname))

# function to add employee records
def add_employee(connection, EID, EFname, ELname):
	with connection:
		connection.execute(INSERT_EMPLOYEE, (EID, EFname, ELname))

# function to add Sales records
def add_sales(connection, SID, SQty, STotal, CID, IID, EID):
	with connection:
		connection.execute(INSERT_SALES, (SID, SQty, STotal, CID, IID, EID))

# function to add inventory records
def add_inventory(connection, IID, IDesc, IPrice):
	with connection:
		connection.execute(INSERT_INVENTORY, (IID, IDesc, IPrice))

###########################################################
############ This section is for reading Records ##########
###########################################################
# Reads all data in table
def get_all_customers(connection):
	with connection:
		return connection.execute(SELECT_ALL_CUSTOMERS).fetchall()

# reads data first & lastname of customer
def get_customer_by_last_name(connection):
	with connection:
		return connection.execute(SELECT_CUSTOMER).fetchall()

# Employee Data
# Reads all data in table		
def get_all_employees(connection):
	with connection:
		return connection.execute(SELECT_ALL_EMPLOYEES).fetchall()

# reads data id and lastname 
def get_employee_ID_last_name(connection):
	with connection:
		return connection.execute(SELECT_EMPLOYEE).fetchall()

# Sales Data
# Reads all data in table
def get_all_sales(connection):
	with connection:
		return connection.execute(SELECT_ALL_SALES).fetchall()

# reads data by SID
def get_sale(connection, SID):
	with connection:
		return connection.execute(SELECT_SALE, (SID,)).fetchall()

# Inventory Data
# Reads all data in table
def get_all_inventory(connection):
	with connection:
		return connection.execute(SELECT_ALL_INVENTORY).fetchall()

# reads IDesc data only 
def get_inventory(connection):
	with connection:
		return connection.execute(SELECT_INVENTORY).fetchall()

# reads data by Sales Quantity >= 2
def show_sales_inventory(connection):
        with connection:
                return connection.execute(SHOW_SALES_INVENTORY).fetchall()

###########################################################
############ This section is for deleting Records #########
###########################################################

def delete_customer(connection, CID):
	with connection:
		connection.execute(DELETE_CUSTOMER, (CID,))

def delete_employee(connection, EID):
	with connection:
		connection.execute(DELETE_EMPLOYEE, (EID,))

def delete_sale(connection, SID):
	with connection:
		connection.execute(DELETE_SALES, (SID,))

def delete_inventory(connection, IID):
	with connection:
		connection.execute(DELETE_INVENTORY, (IID,))

###########################################################
############ This section is for updating Records #########
###########################################################
# Update to customer data	
def update_customer_fname(connection, CFname, CID):
	with connection:
		connection.execute(CHANGE_CUSTOMER_FNAME, (CFname, CID))

def update_customer_lname(connection, CLname, CID):
	with connection:
		connection.execute(CHANGE_CUSTOMER_LNAME, (CLname, CID))

# Update to employee data
def update_employee_fname(connection, EFname, EID):
	with connection:
		connection.execute(CHANGE_EMPLOYEE_FNAME, (EFname, EID))

def update_employee_lname(connection, ELname, EID):
	with connection:
		connection.execute(CHANGE_EMPLOYEE_LNAME, (ELname, EID))

# Update Sales Data
def update_sales_qty(connection, SQty, SID):
	with connection:
		connection.execute(CHANGE_SALES_QTY, (SQty, SID))

def updates_sales_total(connection, STotal, SID):
	with connection:
		connection.execute(CHANGE_SALES_TOTAL, (STotal, SID))

def update_inventory_desc(connection, IDesc, IID):
	with connection:
		connection.execute(CHANGE_INVENTORY_DESC, (IDesc, IID))

def update_intentory_price(connection, IPrice, IID):
	with connection:
		connection.execute(CHANGE_INVENTORY_PRICE, (IPrice, IID))
