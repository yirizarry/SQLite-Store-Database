#######################################################################
######################## ReadMe #######################################
#######################################################################


1)
########################## database.py ##################################
1. Connects & creates new database							#
2. Creates multiple Tables (Customer, Employee, Inventory and Sales)	#
3. Insert Statements to populate data for each table				#
#########################################################################


2)
####################### connectAndModify.py #############################
1. At the Top we have multiple Sqlite statements:				#
	- insert new records for all tables						#
	- reading records of tables							#
	- deleting records by ID							#
	- Updating records								#
#########################################################################


3)
############################ tester.py ##################################
1. Menu function that prompts user to select a choice from menu		#
2. connect to connectAndModify so we can use the func to modify the DB	#
3. calls menu for prompt 								#
4. prompts user for choice								#
4. while loop will execute until we choose exit					#
5. checks which choice was made, executes the selection (1-24)		#
6. if number is not between 1-24, main() prompt user again			#
7. program will end by the statement sys.exit					#
#########################################################################