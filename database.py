import sqlite3

# connection
connection = sqlite3.connect('larrys_store.db')

cursor = connection.cursor()


# Creates Customers Table
create_customers_table = """CREATE TABLE IF NOT EXISTS
Customers(CID INTEGER PRIMARY KEY, CFname TEXT, CLname TEXT)"""

cursor.execute(create_customers_table)

# Creates Employees Table
create_employees_table = """CREATE TABLE IF NOT EXISTS
Employees(EID INTEGER PRIMARY KEY, EFname TEXT, ELname TEXT)"""

cursor.execute(create_employees_table)

# Creates Inventory Table
create_inventory_table = """CREATE TABLE IF NOT EXISTS
Inventory(IID INTEGER PRIMARY KEY, IDesc TEXT, IPrice FLOAT)"""

cursor.execute(create_inventory_table)

# Creates Sales Table
create_sales_table = """CREATE TABLE IF NOT EXISTS
Sales(SID INTEGER PRIMARY KEY, SQty INTEGER, STotal FLOAT, 
CID INT NOT NULL,
IID INT NOT NULL,
EID INT NOT NULL,
FOREIGN KEY (CID) REFERENCES Customers(CID),
FOREIGN KEY (EID) REFERENCES Employees(EID),
FOREIGN KEY (IID) REFERENCES Inventory(IID))"""

cursor.execute(create_sales_table)

# add 10 rows to customers
cursor.execute("INSERT OR IGNORE INTO Customers VALUES (1, 'Lola', 'Blair')")
cursor.execute("INSERT OR IGNORE INTO Customers VALUES (2, 'Brendan', 'Bush')")
cursor.execute("INSERT OR IGNORE INTO Customers VALUES (3, 'Simon', 'McKinney')")
cursor.execute("INSERT OR IGNORE INTO Customers VALUES (4, 'Herald', 'Beck')")
cursor.execute("INSERT OR IGNORE INTO Customers VALUES (5, 'Lucas', 'Ballot')")
cursor.execute("INSERT OR IGNORE INTO Customers VALUES (6, 'Mario', 'Regan')")
cursor.execute("INSERT OR IGNORE INTO Customers VALUES (7, 'Gordon', 'Bell')")
cursor.execute("INSERT OR IGNORE INTO Customers VALUES (8, 'Vincent', 'Rowling')")
cursor.execute("INSERT OR IGNORE INTO Customers VALUES (9, 'Jarrad', 'Butler')")
cursor.execute("INSERT OR IGNORE INTO Customers VALUES (10, 'Codey', 'Bow')")

# adds 10 rows with values to employees
cursor.execute("INSERT OR IGNORE INTO Employees VALUES (1, 'John', 'Smith')")
cursor.execute("INSERT OR IGNORE INTO Employees VALUES (2, 'Renae', 'Burkhart')")
cursor.execute("INSERT OR IGNORE INTO Employees VALUES (3, 'Rachel', 'Heart')")
cursor.execute("INSERT OR IGNORE INTO Employees VALUES (4, 'Timothy', 'Green')")
cursor.execute("INSERT OR IGNORE INTO Employees VALUES (5, 'Jennifer', 'Lee')")
cursor.execute("INSERT OR IGNORE INTO Employees VALUES (6, 'Dylan', 'Murtz')")
cursor.execute("INSERT OR IGNORE INTO Employees VALUES (7, 'Jeremy', 'Klein')")
cursor.execute("INSERT OR IGNORE INTO Employees VALUES (8, 'Linda', 'Lopez')")
cursor.execute("INSERT OR IGNORE INTO Employees VALUES (9, 'Mary', 'Mooney')")
cursor.execute("INSERT OR IGNORE INTO Employees VALUES (10, 'Derrick', 'Wade')")

# adds 10 rows with values to inventory
cursor.execute("INSERT OR IGNORE INTO Inventory VALUES (1, 'Prada, Single breasted Wool Suit', 1990.99)")
cursor.execute("INSERT OR IGNORE INTO Inventory VALUES (2, 'Sebastian Cruz Couture, Champagne Dinner Jacket', 1185.99)")
cursor.execute("INSERT OR IGNORE INTO Inventory VALUES (3, 'Dolce And Gabbana, Single Breasted Two Piece Suit', 1915.99)")
cursor.execute("INSERT OR IGNORE INTO Inventory VALUES (4, 'Paul Smith, Brick Red Windowpane Check Suit', 1695.00)")
cursor.execute("INSERT OR IGNORE INTO Inventory VALUES (5, 'Dolce And Gabbana, Marble Print Two Piece Suit', 5695.99)")
cursor.execute("INSERT OR IGNORE INTO Inventory VALUES (6, 'Ermenegildo Zegna, Black Trofeo Wool Tuxedo', 3395.00)")
cursor.execute("INSERT OR IGNORE INTO Inventory VALUES (7, 'Zarr Mezzanotte, Dinner Jacket', 1295.00)")
cursor.execute("INSERT OR IGNORE INTO Inventory VALUES (8, 'Saint Laurent, Mens Virgin Wool Suit Noir', 2990.00)")
cursor.execute("INSERT OR IGNORE INTO Inventory VALUES (9, 'Paul Smith, Wool Suit', 720.99)")
cursor.execute("INSERT OR IGNORE INTO Inventory VALUES (10, 'Calvin Klein, Mens Peak Lapel Big And Tall Tuxedo Black', 499.99)")

# adds 10 rows with values to sales (SID, SQty, STotal, CID, EID, IID)
cursor.execute("INSERT OR IGNORE INTO Sales VALUES (1, 2, 11391.98, 5, 1, 5)")
cursor.execute("INSERT OR IGNORE INTO Sales VALUES (2, 1, 499.99, 1, 4, 10)")
cursor.execute("INSERT OR IGNORE INTO Sales VALUES (3, 1, 5695.99, 3,3, 5)")
cursor.execute("INSERT OR IGNORE INTO Sales VALUES (4, 2, 5980.00, 2,4, 7)")
cursor.execute("INSERT OR IGNORE INTO Sales VALUES (5, 1, 3395.00, 7,3, 6)")
cursor.execute("INSERT OR IGNORE INTO Sales VALUES (6, 1, 2990.00, 8,2, 8)")
cursor.execute("INSERT OR IGNORE INTO Sales VALUES (7, 2, 3981.98, 9,1, 1)")
cursor.execute("INSERT OR IGNORE INTO Sales VALUES (8, 1, 1185.99, 10,3, 2)")
cursor.execute("INSERT OR IGNORE INTO Sales VALUES (9, 1, 3395.00, 4,2, 6)")
cursor.execute("INSERT OR IGNORE INTO Sales VALUES (10, 3, 1499.97, 6, 3, 10)")

connection.commit()
connection.close()  # closes connection
