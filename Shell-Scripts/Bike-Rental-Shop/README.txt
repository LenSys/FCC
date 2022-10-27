============================
Build a Bike Rental Shop
============================

In this 210-lesson course, you will build an interactive Bash program that stores 
rental information for your bike rental shop using PostgreSQL.

The first thing you need to do is start the terminal. Do that by clicking the "hamburger" 
menu at the top left of the screen, going to the "terminal" section, and clicking 
"new terminal". Once you open a new one, type echo hello terminal into the terminal and 
press enter.

You are going to build a bike rental shop. It will have a database, and a bash script to 
interact with the database. Use the terminal to connect to PostgreSQL by entering 
psql --username=freecodecamp --dbname=postgres.

------------------------------------------------------------------------------------------

List the databases with \l to see what databases are here.

postgres=> \l
postgres=>                                List of databases
+-----------+----------+----------+---------+---------+-----------------------+
|   Name    |  Owner   | Encoding | Collate |  Ctype  |   Access privileges   |
+-----------+----------+----------+---------+---------+-----------------------+
| postgres  | postgres | UTF8     | C.UTF-8 | C.UTF-8 |                       |
| template0 | postgres | UTF8     | C.UTF-8 | C.UTF-8 | =c/postgres          +|
|           |          |          |         |         | postgres=CTc/postgres |
| template1 | postgres | UTF8     | C.UTF-8 | C.UTF-8 | =c/postgres          +|
|           |          |          |         |         | postgres=CTc/postgres |
+-----------+----------+----------+---------+---------+-----------------------+
(3 rows)

------------------------------------------------------------------------------------------

You need your own database for the bike shop. Create a new database named bikes.

postgres=> CREATE DATABASE bikes;

------------------------------------------------------------------------------------------

List databases again to make sure your database got created.

postgres=> \l
                                 List of databases
+-----------+--------------+----------+---------+---------+-----------------------+
|   Name    |    Owner     | Encoding | Collate |  Ctype  |   Access privileges   |
+-----------+--------------+----------+---------+---------+-----------------------+
| bikes     | freecodecamp | UTF8     | C.UTF-8 | C.UTF-8 |                       |
| postgres  | postgres     | UTF8     | C.UTF-8 | C.UTF-8 |                       |
| template0 | postgres     | UTF8     | C.UTF-8 | C.UTF-8 | =c/postgres          +|
|           |              |          |         |         | postgres=CTc/postgres |
| template1 | postgres     | UTF8     | C.UTF-8 | C.UTF-8 | =c/postgres          +|
|           |              |          |         |         | postgres=CTc/postgres |
+-----------+--------------+----------+---------+---------+-----------------------+
(4 rows)

------------------------------------------------------------------------------------------

postgres=> \c bikes;
You are now connected to database "bikes" as user "freecodecamp".

------------------------------------------------------------------------------------------

Your database needs three tables. One for your bike inventory, one for your customers, 
and one for the bikes that are rented out. Create a table named bikes in your database 
for the inventory.

bikes=> CREATE TABLE bikes();

------------------------------------------------------------------------------------------

Display the tables to make sure your table got created.

bikes=> \d
bikes=>             List of relations
+--------+-------+-------+--------------+
| Schema | Name  | Type  |    Owner     |
+--------+-------+-------+--------------+
| public | bikes | table | freecodecamp |
+--------+-------+-------+--------------+
(1 row)

------------------------------------------------------------------------------------------

The table will have a few columns for bike information. First, is a unique ID column. 
Add a column to the bikes table named bike_id. Give it a type of SERIAL and make it a 
PRIMARY KEY.

bikes=> ALTER TABLE bikes ADD COLUMN bike_id SERIAL PRIMARY KEY;

------------------------------------------------------------------------------------------

Use the display command to view the details of the bikes table.

bikes=> \d bikes;
bikes=>                                 Table "public.bikes"
+---------+---------+-----------+----------+----------------------------------------+
| Column  |  Type   | Collation | Nullable |                Default                 |
+---------+---------+-----------+----------+----------------------------------------+
| bike_id | integer |           | not null | nextval('bikes_bike_id_seq'::regclass) |
+---------+---------+-----------+----------+----------------------------------------+
Indexes:
    "bikes_pkey" PRIMARY KEY, btree (bike_id)

------------------------------------------------------------------------------------------

The first column is set. Add a column named type for the type of bike.
Make it a VARCHAR(50) and give it a constraint of NOT NULL.

bikes=> ALTER TABLE bikes ADD COLUMN type VARCHAR(50) NOT NULL;

------------------------------------------------------------------------------------------

Display the details of the bikes table again.

bikes=> \d bikes;
                                       Table "public.bikes"
+---------+-----------------------+-----------+----------+----------------------------------------+
| Column  |         Type          | Collation | Nullable |                Default                 |
+---------+-----------------------+-----------+----------+----------------------------------------+
| bike_id | integer               |           | not null | nextval('bikes_bike_id_seq'::regclass) |
| type    | character varying(50) |           | not null |                                        |
+---------+-----------------------+-----------+----------+----------------------------------------+
Indexes:
    "bikes_pkey" PRIMARY KEY, btree (bike_id)

------------------------------------------------------------------------------------------

The first two columns look good. Add a column named size to the bikes table that is an INT 
and has the NOT NULL constraint. This will be for the size of each bike.

bikes=> ALTER TABLE bikes ADD COLUMN size INT NOT NULL;

------------------------------------------------------------------------------------------

Add another column to the table named available. Make it a boolean and has a constraint of 
NOT NULL. Also give it a default value of TRUE. This will be set to false when someone 
rents out a bike.

bikes=> ALTER TABLE bikes ADD COLUMN available BOOLEAN NOT NULL DEFAULT TRUE;

------------------------------------------------------------------------------------------

Display the details of the bikes table again so you can make sure it's how you want it.

bikes=> \d bikes;
                                        Table "public.bikes"
+-----------+-----------------------+-----------+----------+----------------------------------------+
|  Column   |         Type          | Collation | Nullable |                Default                 |
+-----------+-----------------------+-----------+----------+----------------------------------------+
| bike_id   | integer               |           | not null | nextval('bikes_bike_id_seq'::regclass) |
| type      | character varying(50) |           | not null |                                        |
| size      | integer               |           | not null |                                        |
| available | boolean               |           | not null | true                                   |
+-----------+-----------------------+-----------+----------+----------------------------------------+
Indexes:
    "bikes_pkey" PRIMARY KEY, btree (bike_id)

------------------------------------------------------------------------------------------

That table is done for now. Create another table named customers. It will store a name and 
phone number for each customer that rents a bike.

bikes=> CREATE TABLE customers();

------------------------------------------------------------------------------------------

Add a customer_id column to your new table that is a type of SERIAL and make it a PRIMARY KEY.

bikes=> ALTER TABLE customers ADD COLUMN customer_id SERIAL PRIMARY KEY;

------------------------------------------------------------------------------------------

Display the details of the customers table so you can make sure your new column is there.

bikes=> \d customers;
                                    Table "public.customers"
+-------------+---------+-----------+----------+------------------------------------------------+
|   Column    |  Type   | Collation | Nullable |                    Default                     |
+-------------+---------+-----------+----------+------------------------------------------------+
| customer_id | integer |           | not null | nextval('customers_customer_id_seq'::regclass) |
+-------------+---------+-----------+----------+------------------------------------------------+
Indexes:
    "customers_pkey" PRIMARY KEY, btree (customer_id)

------------------------------------------------------------------------------------------

There it is. Add a column named phone for customers phone numbers. Make it a varying 
character that has a maximum length of 15 characters. Also make sure it can't be null, 
and that it has to be unique.

bikes=> ALTER TABLE customers ADD COLUMN phone VARCHAR(15) NOT NULL UNIQUE;

------------------------------------------------------------------------------------------

Add the last column. Call it name and make it a VARCHAR(40) that can't be null.

bikes=> ALTER TABLE customers ADD COLUMN name VARCHAR(40) NOT NULL;

------------------------------------------------------------------------------------------

Display the details of the customers table.

bikes=> \d customers;
                                           Table "public.customers"
+-------------+-----------------------+-----------+----------+------------------------------------------------+
|   Column    |         Type          | Collation | Nullable |                    Default                     |
+-------------+-----------------------+-----------+----------+------------------------------------------------+
| customer_id | integer               |           | not null | nextval('customers_customer_id_seq'::regclass) |
| phone       | character varying(15) |           | not null |                                                |
| name        | character varying(40) |           | not null |                                                |
+-------------+-----------------------+-----------+----------+------------------------------------------------+
Indexes:
    "customers_pkey" PRIMARY KEY, btree (customer_id)
    "customers_phone_key" UNIQUE CONSTRAINT, btree (phone)

------------------------------------------------------------------------------------------

That table is finished. Lastly, you need a table to store which bikes are rented and who 
has rented them. Create a new table named rentals.

bikes=> CREATE TABLE rentals();

------------------------------------------------------------------------------------------

Add a rental_id column to your new table. Make it automatically increment with SERIAL 
and make it the primary key for this table.

bikes=> ALTER TABLE rentals ADD COLUMN rental_id SERIAL PRIMARY KEY;

------------------------------------------------------------------------------------------

Display the details of the rentals table.

bikes=> \d rentals;
bikes=>                                   Table "public.rentals"
+-----------+---------+-----------+----------+--------------------------------------------+
|  Column   |  Type   | Collation | Nullable |                  Default                   |
+-----------+---------+-----------+----------+--------------------------------------------+
| rental_id | integer |           | not null | nextval('rentals_rental_id_seq'::regclass) |
+-----------+---------+-----------+----------+--------------------------------------------+
Indexes:
    "rentals_pkey" PRIMARY KEY, btree (rental_id)


------------------------------------------------------------------------------------------

Next, you need a column for the customer who is renting a bike. Add column named customer_id. 
This will have an id of a customer from the customers table. Make the column an INT and 
NOT NULL to start.

bikes=> ALTER TABLE rentals ADD COLUMN customer_id INT NOT NULL;

------------------------------------------------------------------------------------------

Make the column you just added a foreign key that references the customer_id column from the 
customers table. Here's an example of how you can do that:
ALTER TABLE table_name ADD FOREIGN KEY(column_name) REFERENCES 
referenced_table(referenced_column);

bikes=> ALTER TABLE rentals ADD FOREIGN KEY(customer_id) REFERENCES customers(customer_id);

------------------------------------------------------------------------------------------

Display the details of the rentals table to make sure your key is set.

bikes=> \d rentals;
                                   Table "public.rentals"
+-------------+---------+-----------+----------+--------------------------------------------+
|   Column    |  Type   | Collation | Nullable |                  Default                   |
+-------------+---------+-----------+----------+--------------------------------------------+
| rental_id   | integer |           | not null | nextval('rentals_rental_id_seq'::regclass) |
| customer_id | integer |           | not null |                                            |
+-------------+---------+-----------+----------+--------------------------------------------+
Indexes:
    "rentals_pkey" PRIMARY KEY, btree (rental_id)
Foreign-key constraints:
    "rentals_customer_id_fkey" FOREIGN KEY (customer_id) REFERENCES customers(customer_id)


------------------------------------------------------------------------------------------

That foreign key is set. You need another column so you know what bike a customer is renting. 
Add a column named bike_id and make it an INT and NOT NULL.

bikes=> ALTER TABLE rentals ADD COLUMN bike_id INT NOT NULL;

------------------------------------------------------------------------------------------

Make that column a foreign key that references the bike_id column from the bikes table so 
you know what bike the id is for.

bikes=> ALTER TABLE rentals ADD FOREIGN KEY(bike_id) REFERENCES bikes(bike_id);

------------------------------------------------------------------------------------------

Display the details of the rentals table so you can make sure the key is correct.

bikes=> \d rentals;
                                   Table "public.rentals"
+-------------+---------+-----------+----------+--------------------------------------------+
|   Column    |  Type   | Collation | Nullable |                  Default                   |
+-------------+---------+-----------+----------+--------------------------------------------+
| rental_id   | integer |           | not null | nextval('rentals_rental_id_seq'::regclass) |
| customer_id | integer |           | not null |                                            |
| bike_id     | integer |           | not null |                                            |
+-------------+---------+-----------+----------+--------------------------------------------+
Indexes:
    "rentals_pkey" PRIMARY KEY, btree (rental_id)
Foreign-key constraints:
    "rentals_bike_id_fkey" FOREIGN KEY (bike_id) REFERENCES bikes(bike_id)
    "rentals_customer_id_fkey" FOREIGN KEY (customer_id) REFERENCES customers(customer_id)

------------------------------------------------------------------------------------------

Moving along. You want to know when a customer rents a bike, and when it gets returned. 
Add a column to your rentals table named date_rented that's a type of DATE. 
Make sure the entry can't be null, and give it a default value of NOW().

bikes=> ALTER TABLE rentals ADD COLUMN date_rented DATE NOT NULL DEFAULT NOW();

------------------------------------------------------------------------------------------

Display the details of the rentals table again.

bikes=> \d rentals;
                                   Table "public.rentals"
+-------------+---------+-----------+----------+--------------------------------------------+
|   Column    |  Type   | Collation | Nullable |                  Default                   |
+-------------+---------+-----------+----------+--------------------------------------------+
| rental_id   | integer |           | not null | nextval('rentals_rental_id_seq'::regclass) |
| customer_id | integer |           | not null |                                            |
| bike_id     | integer |           | not null |                                            |
| date_rented | date    |           | not null | now()                                      |
+-------------+---------+-----------+----------+--------------------------------------------+
Indexes:
    "rentals_pkey" PRIMARY KEY, btree (rental_id)
Foreign-key constraints:
    "rentals_bike_id_fkey" FOREIGN KEY (bike_id) REFERENCES bikes(bike_id)
    "rentals_customer_id_fkey" FOREIGN KEY (customer_id) REFERENCES customers(customer_id)


------------------------------------------------------------------------------------------

It looks good. Lastly, you need column for when a customer returns a bike. Add a column 
named date_returned that's a type of DATE.

bikes=> ALTER TABLE rentals ADD COLUMN date_returned DATE;

------------------------------------------------------------------------------------------

View the details of the table again.

bikes=> \d rentals;
                                    Table "public.rentals"
+---------------+---------+-----------+----------+--------------------------------------------+
|    Column     |  Type   | Collation | Nullable |                  Default                   |
+---------------+---------+-----------+----------+--------------------------------------------+
| rental_id     | integer |           | not null | nextval('rentals_rental_id_seq'::regclass) |
| customer_id   | integer |           | not null |                                            |
| bike_id       | integer |           | not null |                                            |
| date_rented   | date    |           | not null | now()                                      |
| date_returned | date    |           |          |                                            |
+---------------+---------+-----------+----------+--------------------------------------------+
Indexes:
    "rentals_pkey" PRIMARY KEY, btree (rental_id)
Foreign-key constraints:
    "rentals_bike_id_fkey" FOREIGN KEY (bike_id) REFERENCES bikes(bike_id)
    "rentals_customer_id_fkey" FOREIGN KEY (customer_id) REFERENCES customers(customer_id)


------------------------------------------------------------------------------------------

The tables are all finished. Display all the tables so you can see what you ended up with.

bikes=> \d
bikes=>                        List of relations
+--------+---------------------------+----------+--------------+
| Schema |           Name            |   Type   |    Owner     |
+--------+---------------------------+----------+--------------+
| public | bikes                     | table    | freecodecamp |
| public | bikes_bike_id_seq         | sequence | freecodecamp |
| public | customers                 | table    | freecodecamp |
| public | customers_customer_id_seq | sequence | freecodecamp |
| public | rentals                   | table    | freecodecamp |
| public | rentals_rental_id_seq     | sequence | freecodecamp |
+--------+---------------------------+----------+--------------+
(6 rows)

------------------------------------------------------------------------------------------

You have nine bikes in your inventory. Add the first one to your bikes table. It has a 
type of Mountain and a size of 27. Make sure to put your VARCHAR values in single quotes. 
The bike_id and available columns should be filled in automatically, so you don't need to 
worry about those.

bikes=> INSERT INTO bikes(type,size) VALUES ('Mountain', 27);

------------------------------------------------------------------------------------------

View all the columns in your bikes table with SELECT.

bikes=> SELECT * FROM bikes;
                     
+---------+----------+------+-----------+
| bike_id |   type   | size | available |
+---------+----------+------+-----------+
|       1 | Mountain |   27 | t         |
+---------+----------+------+-----------+
(1 row)

------------------------------------------------------------------------------------------

Looks like it's all working, the bike_id and available columns were filled in automatically. 
Insert another bike. Give it a type of Mountain and a size of 28.

bikes=> INSERT INTO bikes(type,size) VALUES ('Mountain', 28);

------------------------------------------------------------------------------------------

Add another Mountain bike to your inventory. Make it a 29 inch bike.

bikes=> INSERT INTO bikes(type,size) VALUES ('Mountain', 29);

------------------------------------------------------------------------------------------

Add a 27 inch Road bike to the table.

bikes=> INSERT INTO bikes(type,size) VALUES ('Road', 27);

------------------------------------------------------------------------------------------

Use SELECT to view all the data in the bikes table again.

bikes=> SELECT * FROM bikes;
                     
+---------+----------+------+-----------+
| bike_id |   type   | size | available |
+---------+----------+------+-----------+
|       1 | Mountain |   27 | t         |
|       2 | Mountain |   28 | t         |
|       3 | Mountain |   29 | t         |
|       4 | Road     |   27 | t         |
+---------+----------+------+-----------+
(4 rows)

------------------------------------------------------------------------------------------

Add the two bikes to your inventory, they are 28 and 29 inch Road bikes. Try to add them 
both with one command.

bikes=> INSERT INTO bikes(type,size) VALUES ('Road', 28), ('Road', 29);

------------------------------------------------------------------------------------------

There's three more bikes. Add 19, 20, and 21 inch BMX bikes to your table. Try to add 
them with one command.

bikes=> INSERT INTO bikes(type,size) VALUES ('BMX', 19), ('BMX', 20), ('BMX', 21);

------------------------------------------------------------------------------------------

View all the data in your bikes table.

bikes=> SELECT * FROM bikes;
                     
+---------+----------+------+-----------+
| bike_id |   type   | size | available |
+---------+----------+------+-----------+
|       1 | Mountain |   27 | t         |
|       2 | Mountain |   28 | t         |
|       3 | Mountain |   29 | t         |
|       4 | Road     |   27 | t         |
|       5 | Road     |   28 | t         |
|       6 | Road     |   29 | t         |
|       7 | BMX      |   19 | t         |
|       8 | BMX      |   20 | t         |
|       9 | BMX      |   21 | t         |
+---------+----------+------+-----------+
(9 rows)

------------------------------------------------------------------------------------------

Your current inventory is all added. For the rest of the project, I recommend leaving 
that terminal open and connected, and that you should "split" the terminal so you have a 
second one to use for bash commands. Do that by clicking the "hamburger" menu at the top 
left of the window, going to the "terminal" section, and clicking "split terminal". 
After you have opened it, use the touch command to create a file named bike-shop.sh in 
the project folder.

codeally@17c15ec401c5:~/project$ touch bike-shop.sh

------------------------------------------------------------------------------------------

This file will be the program for your bike rental shop. Open the file and add a 
"shebang" at the top so it uses bash when it's executed. If you don't remember, it looks 
like this: #!/bin/bash.

(see bike-shop.sh)

------------------------------------------------------------------------------------------

In the file, use echo with the -e flag to print 
"~~~~~ Bike Rental Shop ~~~~~" with a new line at the beginning and end.

(see bike-shop.sh)

------------------------------------------------------------------------------------------

Use the terminal (not the psql one) and the chmod command to make your file executable. 
Add the +x flag and bike-shop.sh to the command to do that.

codeally@17c15ec401c5:~/project$ chmod +x bike-shop.sh 

------------------------------------------------------------------------------------------

Type ./bike-shop.sh in the terminal to run your script.

codeally@17c15ec401c5:~/project$ ./bike-shop.sh 

------------------------------------------------------------------------------------------

In the script, create an empty function named MAIN_MENU. This will have a few options to 
enter when the script runs to rent or return a bike.

1. Here's an example:

FUNCTION_NAME() {

}

(see bike-shop.sh)

------------------------------------------------------------------------------------------

In your function, echo the text "How may I help you?" so that there's a greeting when 
you go to the menu.

(see bike-shop.sh)

------------------------------------------------------------------------------------------

Call your MAIN_MENU at the bottom of the file so the function runs when you start the 
script.

(see bike-shop.sh)

------------------------------------------------------------------------------------------

Run the file in the terminal again so you can see what it is outputting.

codeally@17c15ec401c5:~/project$ ./bike-shop.sh 

------------------------------------------------------------------------------------------

It's coming along. Add another echo command in the function below the other one. 
Make it output text that looks like this:

1. Rent a bike
2. Return a bike
3. Exit
Note that there's an empty line at the start.

(see bike-shop.sh)

------------------------------------------------------------------------------------------

Run the file to make sure it worked.

codeally@17c15ec401c5:~/project$ ./bike-shop.sh 

------------------------------------------------------------------------------------------

You have some options displaying. Next, you need to get input from whoever is using the 
program. Use the read command to read input into a variable called MAIN_MENU_SELECTION 
below the options.

(see bike-shop.sh)

------------------------------------------------------------------------------------------

When an option gets entered, you need to take a user to one of those other menus. Add an 
empty RENT_MENU function below the MAIN_MENU function.

(see bike-shop.sh)

------------------------------------------------------------------------------------------

For the time being, just echo Rent Menu in the function so you can see if it's working.

(see bike-shop.sh)

------------------------------------------------------------------------------------------

Add an empty RETURN_MENU function below the RENT_MENU function for when a user enters 
the option to return a bike.

(see bike-shop.sh)

------------------------------------------------------------------------------------------

Use echo to print Return Menu in the function you just added. You will change these later.

(see bike-shop.sh)

------------------------------------------------------------------------------------------

Add an empty EXIT function below the RETURN_MENU function for when a user wants to 
exit the program.

(see bike-shop.sh)

------------------------------------------------------------------------------------------

This one probably doesn't need a placeholder message. In the EXIT function, use echo to 
print "Thank you for stopping in." with a new line at the beginning and end of the message.

(see bike-shop.sh)

------------------------------------------------------------------------------------------

When a user enters an option at the main menu, you want to take them to the appropriate 
sub-menu. You can use a case statement for this. Here's an example:

case EXPRESSION in
  PATTERN) STATEMENTS ;;
  PATTERN) STATEMENTS ;;
  PATTERN) STATEMENTS ;;
  *) STATEMENTS ;;
esac
The expression you want is the $MAIN_MENU_SELECTION variable. You are expecting it to be 
a 1, 2, or 3 for your various menus. Add a case statement that takes users to their 
corresponding menus. The * is for when anything else is entered. Take users to the 
MAIN_MENU when the variable isn't a 1, 2, or 3.

(see bike-shop.sh)

------------------------------------------------------------------------------------------

Run the script a few times and try out the different menus. Be sure to enter something 
other than one of the options to go to the main menu.

codeally@17c15ec401c5:~/project$ ./bike-shop.sh 

------------------------------------------------------------------------------------------

Add an argument to where you call MAIN_MENU in the case statement. It should be 
"Please enter a valid option.". The next step will adjust the function so the message is 
printed when a user enters an invalid option.

(see bike-shop.sh)

------------------------------------------------------------------------------------------

At the top of the MAIN_MENU function, add an if condition that checks if there's an 
argument ($1) passed to the function. If there is, print the message with a new line in 
front of it.

(see bike-shop.sh)

------------------------------------------------------------------------------------------

Run the script and enter an invalid option to see the message. Exit the program when you 
are done.

codeally@17c15ec401c5:~/project$ ./bike-shop.sh 

------------------------------------------------------------------------------------------

Looks good. Delete the echo "Rent Menu" from the RENT_MENU function so you can start 
adding the ability to rent a bike from the database.

(see bike-shop.sh)

------------------------------------------------------------------------------------------

In the RENT_MENU function, add three single line comments; "get available bikes", "if no 
bikes available", and "send to main menu", in that order.

(see bike-shop.sh)

------------------------------------------------------------------------------------------

To get the bikes available, you need to query the database from your script. Below the 
"shebang", add a PSQL variable that looks like this: 
PSQL="psql -X --username=freecodecamp --dbname=bikes --tuples-only -c". 

You will then be able to use it to query the database like this: $($PSQL "<query_here>").

(see bike-shop.sh)

------------------------------------------------------------------------------------------

Below the get available bikes comment. Create an AVAILABLE_BIKES variable that gets the 
bike_id, type, and size columns from the bikes table for the bikes that are available. 
Order the results by their bike_id column. Here's an example: 
AVAILABLE_BIKES=$($PSQL "<query_here>")

AVAILABLE_BIKES=$($PSQL "SELECT bike_id, type, size FROM bikes WHERE 
available = true ORDER BY bike_id");
(see bike-shop.sh)
------------------------------------------------------------------------------------------

Below the new variable, use echo to print it. Place it in double quotes so it prints 
any new lines.

echo "$AVAILABLE_BIKES"
(see bike-shop.sh)

------------------------------------------------------------------------------------------

Run your script and go to the rent menu to see if the available bikes are being printed.

codeally@17c15ec401c5:~/project$ ./bike-shop.sh 

~~~~~ Bike Rental Shop ~~~~~

How may I help you?


1. Rent a bike
2. Return a bike
3. Exit
1
       1 | Mountain |   27
       2 | Mountain |   28
       3 | Mountain |   29
       4 | Road     |   27
       5 | Road     |   28
       6 | Road     |   29
       7 | BMX      |   19
       8 | BMX      |   20
       9 | BMX      |   21

------------------------------------------------------------------------------------------

Awesome. In the psql prompt, set the available column to false for all the bikes so you 
can see what it prints when there's no bikes available.

bikes=> UPDATE bikes SET available = false;

------------------------------------------------------------------------------------------

Run your script and go to the rent menu to see the output.

codeally@17c15ec401c5:~/project$ ./bike-shop.sh 

~~~~~ Bike Rental Shop ~~~~~

How may I help you?


1. Rent a bike
2. Return a bike
3. Exit
1

------------------------------------------------------------------------------------------

So if there's no bike available, the variable will be empty. In the script, below the 
if no bikes available comment, add an if condition that checks if the variable is empty. 
Use -z to check if it's empty. Place the send to main menu comment in its STATEMENTS area.

RENT_MENU() {
  # get available bikes
  AVAILABLE_BIKES=$($PSQL "SELECT bike_id, type, size FROM bikes WHERE available = true ORDER BY bike_id")
  echo "$AVAILABLE_BIKES"

  # if no bikes available
  if [[ -z $AVAILABLE_BIKES ]]
  then
    # send to main menu
  fi
}
(see bike-shop.sh)

------------------------------------------------------------------------------------------

Below the comment in the if you just added. Send users to the main menu and give them 
the message, "Sorry, we don't have any bikes available right now."

RENT_MENU() {
  # get available bikes
  AVAILABLE_BIKES=$($PSQL "SELECT bike_id, type, size FROM bikes WHERE available = true ORDER BY bike_id")
  echo "$AVAILABLE_BIKES"

  # if no bikes available
  if [[ -z $AVAILABLE_BIKES ]]
  then
    # send to main menu
    MAIN_MENU "Sorry, we don't have any bikes available right now."
  fi
}
(see bike-shop.sh)

------------------------------------------------------------------------------------------

Run the script and go to the rent menu to see the message. When you are done, exit the 
program.

codeally@17c15ec401c5:~/project$ ./bike-shop.sh 

~~~~~ Bike Rental Shop ~~~~~

How may I help you?


1. Rent a bike
2. Return a bike
3. Exit
1


Sorry, we don't have any bikes available right now.
How may I help you?


1. Rent a bike
2. Return a bike
3. Exit
3

Thank you for stopping in.

------------------------------------------------------------------------------------------

If no bikes are available, you will get that message. Add an else to the if condition 
for when there is bikes available. In it, add four single line comments; 
"display available bikes", "ask for bike to rent", "if input is not a number", and 
"send to main menu".

RENT_MENU() {
  # get available bikes
  AVAILABLE_BIKES=$($PSQL "SELECT bike_id, type, size FROM bikes WHERE available = true ORDER BY bike_id")
  echo "$AVAILABLE_BIKES"

  # if no bikes available
  if [[ -z $AVAILABLE_BIKES ]]
  then
    # send to main menu
    MAIN_MENU "Sorry, we don't have any bikes available right now."
  else
    # display available bikes

    # ask for bike to rent

    # if input is not a number

    # send to main menu
  fi
}
(see bike-shop.sh)

------------------------------------------------------------------------------------------

Below the "display available bikes" comment you just added, use echo to print 
"Here are the bikes we have available:" with a new line in front of the message.

# display available bikes
    echo -e "\nHere are the bikes we have available:"

(see bike-shop.sh)

------------------------------------------------------------------------------------------

Move the echo command that prints all the available bikes below the message you just added.

else
    # display available bikes
    echo -e "\nHere are the bikes we have available:"
    echo "$AVAILABLE_BIKES"

(see bike-shop.sh)

------------------------------------------------------------------------------------------

In the psql prompt, set all the bikes, except for the BMX bikes, back to true so you can 
see a list of bikes to rent.

bikes=> UPDATE bikes SET available = true WHERE type != 'BMX';

------------------------------------------------------------------------------------------

Run the script and go to the rent menu to see the list of bikes available.

codeally@17c15ec401c5:~/project$ ./bike-shop.sh 

~~~~~ Bike Rental Shop ~~~~~

How may I help you?


1. Rent a bike
2. Return a bike
3. Exit
1

Here are the bikes we have available:
       1 | Mountain |   27
       2 | Mountain |   28
       3 | Mountain |   29
       4 | Road     |   27
       5 | Road     |   28
       6 | Road     |   29

------------------------------------------------------------------------------------------

nstead of directly printing the list, pipe the output into a while loop that reads each 
line. Here's how that looks:

echo "$AVAILABLE_BIKES" | while read <VAR_1> <VAR_2> <VAR_3> <VAR_4> <VAR_5>
do
  <STATEMENTS>
done
It will read the first line of your AVAILABLE_BIKES variable into the five variables. 
Each variable being the next word in the line. Read each line into variables, 
BIKE_ID BAR TYPE BAR SIZE. In the <STATEMENTS> area, use echo to print the BIKE_ID, TYPE, 
and SIZE variables, in that order.

else
    # display available bikes
    echo -e "\nHere are the bikes we have available:"
    echo "$AVAILABLE_BIKES" | while read BIKE_ID BAR TYPE BAR SIZE
    do
        echo "$BIKE_ID $TYPE $SIZE"
    done

(see bike-shop.sh)

------------------------------------------------------------------------------------------

Run the script and go to the rent menu again to see if it's working.

codeally@17c15ec401c5:~/project$ ./bike-shop.sh 

~~~~~ Bike Rental Shop ~~~~~

How may I help you?


1. Rent a bike
2. Return a bike
3. Exit
1

Here are the bikes we have available:
1 Mountain 27
2 Mountain 28
3 Mountain 29
4 Road 27
5 Road 28
6 Road 29

------------------------------------------------------------------------------------------

It's working. Adjust the echo command that prints the bike info so that the first line 
printed would look like this: '1) 27" Mountain Bike'. The rest would look the same, 
but with their bike info. Make sure to escape any characters you need to.

echo "$BIKE_ID) $SIZE\" $TYPE Bike"

(see bike-shop.sh)

------------------------------------------------------------------------------------------

Run the script and go to the rent menu again to see what it looks like now.

codeally@17c15ec401c5:~/project$ ./bike-shop.sh 

~~~~~ Bike Rental Shop ~~~~~

How may I help you?


1. Rent a bike
2. Return a bike
3. Exit
1

Here are the bikes we have available:
1) 27" Mountain Bike
2) 28" Mountain Bike
3) 29" Mountain Bike
4) 27" Road Bike
5) 28" Road Bike
6) 29" Road Bike

------------------------------------------------------------------------------------------

That's better. Below the ask for bike to rent comment, print 
"Which one would you like to rent?" with a new line in front of it.

# ask for bike to rent
echo -e "\nWhich one would you like to rent?"

(see bike-shop.sh)

------------------------------------------------------------------------------------------

Just below that, add a command to read input into a variable named BIKE_ID_TO_RENT.

# ask for bike to rent
echo -e "\nWhich one would you like to rent?"
read BIKE_ID_TO_RENT

(see bike-shop.sh)

------------------------------------------------------------------------------------------

Next, you want to find out how to test if the user input is a number. In the terminal, 
enter [[ a =~ [0-9] ]]; echo $? to see if a is a number. The conditional expression 
will run, and echo $? will print the exit code of it (the last command).

codeally@17c15ec401c5:~/project$ [[ a =~ [0-9] ]]; echo $?
1

------------------------------------------------------------------------------------------

It printed 1 for false. Meaning that a did not match the pattern [0-9], or a did not 
contain a number from 0-9. Enter the same commands, but check if a1 matches the pattern.

codeally@17c15ec401c5:~/project$ [[ a1 =~ [0-9] ]]; echo $?
0

------------------------------------------------------------------------------------------

That printed 0 for true. a1 does contain a number from 0-9. Enter the same command, 
but change the pattern to ^[0-9]$. The ^ signifies the start of the pattern, and $ 
means the end. So the input will have to start, contain a number 0-9, and end.

codeally@17c15ec401c5:~/project$ [[ a1 =~ ^[0-9]$ ]]; echo $?
1

------------------------------------------------------------------------------------------

1 for false. a1 does not match the pattern. Using the same syntax, check if 1 matches 
the pattern.

codeally@17c15ec401c5:~/project$ [[ 1 =~ ^[0-9]$ ]]; echo $?
0

------------------------------------------------------------------------------------------

1 does match the pattern. It starts, contains a number, and ends. Check if 11 matches 
the same pattern.

codeally@17c15ec401c5:~/project$ [[ 11 =~ ^[0-9]$ ]]; echo $?
1

------------------------------------------------------------------------------------------

That did not match because the pattern only allows a single number. Add a + after the 
[0-9] to allow any strings that start, contain one or more numbers, and end.

codeally@17c15ec401c5:~/project$ [[ 11 =~ ^[0-9]+$ ]]; echo $?
0

------------------------------------------------------------------------------------------

So that pattern will match any positive integers. You want to check if the input is not 
a number. Add ! in front of the comparison of the previous command to do that.

codeally@17c15ec401c5:~/project$ [[ ! 11 =~ ^[0-9]+$ ]]; echo $?
1

------------------------------------------------------------------------------------------

Back in your script, below the "if input is not a number" comment, add an if condition 
that checks if the input is not a number using the method you just practiced. 
Add the "send to main menu comment" in the then area of the if.

# if input is not a number
if [[ ! $BIKE_ID_TO_RENT =~ ^[0-9]+$ ]]
then
    # send to main menu
fi

(see bike-shop.sh)

------------------------------------------------------------------------------------------

If the $BIKE_ID_TO_RENT variable is not a number, add the code to send users to the 
main menu with the message, "That is not a valid bike number."

# if input is not a number
if [[ ! $BIKE_ID_TO_RENT =~ ^[0-9]+$ ]]
then
    # send to main menu
    MAIN_MENU "That is not a valid bike number."
fi

------------------------------------------------------------------------------------------

Run the script, go to the rent menu, and enter something that isn't a number to make 
sure it is working. When you are done, exit the program.

codeally@17c15ec401c5:~/project$ ./bike-shop.sh 

~~~~~ Bike Rental Shop ~~~~~

How may I help you?


1. Rent a bike
2. Return a bike
3. Exit
1

Here are the bikes we have available:
1) 27" Mountain Bike
2) 28" Mountain Bike
3) 29" Mountain Bike
4) 27" Road Bike
5) 28" Road Bike
6) 29" Road Bike

Which one would you like to rent?
a

That is not a valid bike number.
How may I help you?


1. Rent a bike
2. Return a bike
3. Exit
3

Thank you for stopping in.

------------------------------------------------------------------------------------------

Add an else area for when the input is a number. Add these three single line comments 
in it; "get bike availability", "if not available", "send to main menu".

# if input is not a number
if [[ ! $BIKE_ID_TO_RENT =~ ^[0-9]+$ ]]
then
    # send to main menu
    MAIN_MENU "That is not a valid bike number."
else
    # get bike availability
    
    # if not available
    
    # send to main menu
fi

(see bike-shop.sh)

------------------------------------------------------------------------------------------

Below the get bike availability comment you just added, create a BIKE_AVAILABILITY 
variable. Set it equal to a query that gets the available column from the bikes table 
for the input. Also, make sure to only get the row if it is available.

else
    # get bike availability
    BIKE_AVAILABILITY=$($PSQL "SELECT available FROM bikes WHERE 
    bike_id = $BIKE_ID_TO_RENT AND available = true")

(see bike-shop.sh)

------------------------------------------------------------------------------------------

Right below the variable you just created, use echo to print it so you can see what it 
looks like.

# get bike availability
BIKE_AVAILABILITY=$($PSQL "SELECT available FROM bikes WHERE bike_id = $BIKE_ID_TO_RENT AND available = true")
echo $BIKE_AVAILABILITY

(see bike-shop.sh)

------------------------------------------------------------------------------------------

Run the script a few times, go to the rent menu, enter a bike that is available and one 
that isn't. You should have some BMX bikes that aren't available.

codeally@17c15ec401c5:~/project$ ./bike-shop.sh 

~~~~~ Bike Rental Shop ~~~~~

How may I help you?


1. Rent a bike
2. Return a bike
3. Exit
1

Here are the bikes we have available:
1) 27" Mountain Bike
2) 28" Mountain Bike
3) 29" Mountain Bike
4) 27" Road Bike
5) 28" Road Bike
6) 29" Road Bike

Which one would you like to rent?
1
t

------------------------------------------------------------------------------------------

The variable will be t or empty. Below the "if not available" comment, add an if condition 
that checks if it's empty. Put the "send to main menu" comment in it's statements area.

# get bike availability
BIKE_AVAILABILITY=$($PSQL "SELECT available FROM bikes WHERE bike_id = $BIKE_ID_TO_RENT AND available = true")
echo $BIKE_AVAILABILITY

# if not available
if [[ -z $BIKE_AVAILABILITY ]]
then
    # send to main menu
fi

(see bike-shop.sh)

------------------------------------------------------------------------------------------

In the if condition you just added, send users to the main menu with the message 
"That bike is not available." if they input a number that isn't available.

# if not available
if [[ -z $BIKE_AVAILABILITY ]]
then
    # send to main menu
    MAIN_MENU "That bike is not available."
fi

(see bike-shop.sh)

------------------------------------------------------------------------------------------

Remove the line where you print the BIKE_AVAILABILITY variable. You don't need it anymore.

else
    # get bike availability
    BIKE_AVAILABILITY=$($PSQL "SELECT available FROM bikes WHERE bike_id = $BIKE_ID_TO_RENT AND available = true")

    # if not available
    if [[ -z $BIKE_AVAILABILITY ]]
    then
        # send to main menu
        MAIN_MENU "That bike is not available."
    fi

(see bike-shop.sh)

------------------------------------------------------------------------------------------

Run the script and go to the rent menu, enter a bike that isn't available to make sure 
it's working. When you are done, exit the program.

codeally@17c15ec401c5:~/project$ ./bike-shop.sh 

~~~~~ Bike Rental Shop ~~~~~

How may I help you?


1. Rent a bike
2. Return a bike
3. Exit
1

Here are the bikes we have available:
1) 27" Mountain Bike
2) 28" Mountain Bike
3) 29" Mountain Bike
4) 27" Road Bike
5) 28" Road Bike
6) 29" Road Bike

Which one would you like to rent?
7

That bike is not available.
How may I help you?


1. Rent a bike
2. Return a bike
3. Exit
3

Thank you for stopping in.

------------------------------------------------------------------------------------------

In the psql prompt, set all the bikes availability back to true.

bikes=> UPDATE bikes SET available = true;

------------------------------------------------------------------------------------------

In your script, add an else for when a bike is available. Add these four comments in the 
else area "get customer info", "if customer doesn't exist", "get new customer name", and 
"insert new customer".

# if not available
if [[ -z $BIKE_AVAILABILITY ]]
then
    # send to main menu
    MAIN_MENU "That bike is not available."
else
    # get customer info

    # if customer doesn't exist 

    # get new customer name

    #insert new customer
fi

(see bike-shop.sh)

------------------------------------------------------------------------------------------

As the comments say, you need to get the customer info and find out if they are an 
existing customer. Below the "get customer info comment", print 
"What's your phone number?" with a new line in front of it.

# get customer info
echo -e "\nWhat's your phone number?"

(see bike-shop.sh)

------------------------------------------------------------------------------------------

Below the line you just printed, read input into a PHONE_NUMBER variable. Since the 
phone number is unique, you can use it to identify a customer.

# get customer info
echo -e "\nWhat's your phone number?"
read PHONE_NUMBER

(see bike-shop.sh)

------------------------------------------------------------------------------------------

With the customer's phone number, you can get their name. Below where you get the 
phone number, create a CUSTOMER_NAME variable that gets the customers name from the 
database using the phone number.

# get customer info
echo -e "\nWhat's your phone number?"
read PHONE_NUMBER
CUSTOMER_NAME=$($PSQL "SELECT name FROM customers WHERE phone = '$PHONE_NUMBER'")

(see bike-shop.sh)

------------------------------------------------------------------------------------------

If the customer is in the database with the phone number used, the variable will be 
set to the name. If not, it will be empty. Add an if condition below the 
"if customer doesn't exist" comment that checks if the variable is empty. Place the 
next two comments in the then area.

# get customer info
echo -e "\nWhat's your phone number?"
read PHONE_NUMBER
CUSTOMER_NAME=$($PSQL "SELECT name FROM customers WHERE phone = '$PHONE_NUMBER'")

# if customer doesn't exist 
if [[ -z $CUSTOMER_NAME ]]
then
    # get new customer name

    #insert new customer
fi

(see bike-shop.sh)

------------------------------------------------------------------------------------------

If the customer isn't in the database, you need to get their name so you can add them. 
Below the get new customer name comment, print "What's your name?" with a new line in front 
of the message.

# if customer doesn't exist 
if [[ -z $CUSTOMER_NAME ]]
then
    # get new customer name
    echo -e "\nWhat's your name?"

    #insert new customer
fi

(see bike-shop.sh)

------------------------------------------------------------------------------------------

Below the question you just printed, read input into a variable named CUSTOMER_NAME.

# get new customer name
echo -e "\nWhat's your name?"
read CUSTOMER_NAME

(see bike-shop.sh)

------------------------------------------------------------------------------------------

You have the two pieces of information you need. Below the "insert new customer" comment, 
create an INSERT_CUSTOMER_RESULT variable that inserts the customer into the database.

# if customer doesn't exist 
if [[ -z $CUSTOMER_NAME ]]
then
    # get new customer name
    echo -e "\nWhat's your name?"
    read CUSTOMER_NAME

    #insert new customer
    INSERT_CUSTOMER_RESULT=$($PSQL "INSERT INTO customers(phone, name) 
        VALUES('$PHONE_NUMBER', '$CUSTOMER_NAME');")
fi

(see bike-shop.sh)

------------------------------------------------------------------------------------------

Run your script and go to the rent menu. Pick a bike to rent, then enter "555-5555" when 
it asks for a phone number, and "Me" when it asks for your name.

codeally@17c15ec401c5:~/project$ ./bike-shop.sh 

~~~~~ Bike Rental Shop ~~~~~

How may I help you?


1. Rent a bike
2. Return a bike
3. Exit
1

Here are the bikes we have available:
1) 27" Mountain Bike
2) 28" Mountain Bike
3) 29" Mountain Bike
4) 27" Road Bike
5) 28" Road Bike
6) 29" Road Bike
7) 19" BMX Bike
8) 20" BMX Bike
9) 21" BMX Bike

Which one would you like to rent?
9

What's your phone number?
555-5555

What's your name?
Me

------------------------------------------------------------------------------------------

That should have added a new customer to the database. In the psql prompt, view all the 
data in the customers table to see if it's working.

bikes=> SELECT * FROM customers;
bikes=>                  
+-------------+----------+------+
| customer_id |  phone   | name |
+-------------+----------+------+
|           1 | 555-5555 | Me   |
+-------------+----------+------+
(1 row)

------------------------------------------------------------------------------------------

Excellent. View all the data in the rentals table.

bikes=> SELECT * FROM rentals;
bikes=>                                   
+-----------+-------------+---------+-------------+---------------+
| rental_id | customer_id | bike_id | date_rented | date_returned |
+-----------+-------------+---------+-------------+---------------+
+-----------+-------------+---------+-------------+---------------+
(0 rows)

------------------------------------------------------------------------------------------

So you still need to add the rental to the rentals table when a bike is picked out. 
View all the data in the bikes table.

bikes=> SELECT * FROM bikes;
                     
+---------+----------+------+-----------+
| bike_id |   type   | size | available |
+---------+----------+------+-----------+
|       7 | BMX      |   19 | t         |
|       8 | BMX      |   20 | t         |
|       9 | BMX      |   21 | t         |
|       1 | Mountain |   27 | t         |
|       2 | Mountain |   28 | t         |
|       3 | Mountain |   29 | t         |
|       4 | Road     |   27 | t         |
|       5 | Road     |   28 | t         |
|       6 | Road     |   29 | t         |
+---------+----------+------+-----------+
(9 rows)

------------------------------------------------------------------------------------------

And set the available column to false for the bike rented. Below the end of the if 
statement that inserts a new customer, add five more comments; "get customer_id", 
"insert bike rental", "set bike availability to false", "get bike info", and 
"send to main menu".

else
    # get customer info
    echo -e "\nWhat's your phone number?"
    read PHONE_NUMBER
    CUSTOMER_NAME=$($PSQL "SELECT name FROM customers WHERE phone = '$PHONE_NUMBER'")

    # if customer doesn't exist 
    if [[ -z $CUSTOMER_NAME ]]
    then
        # get new customer name
        echo -e "\nWhat's your name?"
        read CUSTOMER_NAME
    
        #insert new customer
        INSERT_CUSTOMER_RESULT=$($PSQL "INSERT INTO customers(phone, name) VALUES('$PHONE_NUMBER', '$CUSTOMER_NAME');")
    fi

    # get customer_id
    
    # insert bike rental
    
    # set bike availability to false
    
    # get bike info
    
    # send to main menu


(see bike-shop.sh)

------------------------------------------------------------------------------------------

You're getting close to done with the rent functionality. To add a rental to the database, 
you need the customer ID. Below the "get customer_id" comment, create a CUSTOMER_ID 
variable that gets the customer_id using the phone number.


# get customer_id
CUSTOMER_ID=$($PSQL "SELECT customer_id FROM customers WHERE phone = '$PHONE_NUMBER'")


(see bike-shop.sh)

------------------------------------------------------------------------------------------

Now that you have the bike ID and customer ID, you can add the rental to the database. 
Below the "insert bike rental" comment, create a INSERT_RENTAL_RESULT variable that adds 
the rental to the database.

# insert bike rental
INSERT_RENTAL_RESULT=$($PSQL "INSERT INTO rentals(customer_id, bike_id) 
    VALUES('$CUSTOMER_ID', '$BIKE_ID_TO_RENT');")
        

(see bike-shop.sh)

------------------------------------------------------------------------------------------

That should add the rental to the database. The last thing to do is set available to false 
for the bike. Below the "set bike availability to false" comment, create a 
SET_TO_FALSE_RESULT variable that does that.

# set bike availability to false
SET_TO_FALSE_RESULT=$($PSQL "UPDATE bikes SET available = false WHERE 
    bike_id = $BIKE_ID_TO_RENT")

(see bike-shop.sh)

------------------------------------------------------------------------------------------

Run the script and go to the rent menu. Pick the first bike on the list and enter 555-5555 
when it asks for a phone number again. That phone number should already be in the database, 
so it won't ask for a name or insert a customer.

codeally@17c15ec401c5:~/project$ ./bike-shop.sh 

~~~~~ Bike Rental Shop ~~~~~

How may I help you?


1. Rent a bike
2. Return a bike
3. Exit
1

Here are the bikes we have available:
1) 27" Mountain Bike
2) 28" Mountain Bike
3) 29" Mountain Bike
4) 27" Road Bike
5) 28" Road Bike
6) 29" Road Bike
7) 19" BMX Bike
8) 20" BMX Bike
9) 21" BMX Bike

Which one would you like to rent?
9

What's your phone number?
555-5555

------------------------------------------------------------------------------------------

In the psql prompt, view all the data in the rentals table. There should be a new rental.

bikes=> SELECT * FROM rentals;
                                  
+-----------+-------------+---------+-------------+---------------+
| rental_id | customer_id | bike_id | date_rented | date_returned |
+-----------+-------------+---------+-------------+---------------+
|         1 |           1 |       9 | 2022-10-26  |               |
+-----------+-------------+---------+-------------+---------------+
(1 row)

------------------------------------------------------------------------------------------

The rental was added and the date_rented was filled in automatically. Next, view all the 
data in the bikes table. Order the results by bike_id.

bikes=> SELECT * FROM bikes ORDER BY bike_id;
                     
+---------+----------+------+-----------+
| bike_id |   type   | size | available |
+---------+----------+------+-----------+
|       1 | Mountain |   27 | t         |
|       2 | Mountain |   28 | t         |
|       3 | Mountain |   29 | t         |
|       4 | Road     |   27 | t         |
|       5 | Road     |   28 | t         |
|       6 | Road     |   29 | t         |
|       7 | BMX      |   19 | t         |
|       8 | BMX      |   20 | t         |
|       9 | BMX      |   21 | f         |
+---------+----------+------+-----------+
(9 rows)

------------------------------------------------------------------------------------------

The available column was set to false for the bike you rented. The last thing to do is 
give a nice message about the rental. Below the "get bike info" comment, create a 
BIKE_INFO variable that gets the size and type, in that order, of the bike rented.

# get bike info
BIKE_INFO=$($PSQL "SELECT size, type FROM bikes WHERE bike_id = $BIKE_ID_TO_RENT")

(see bike-shop.sh)

------------------------------------------------------------------------------------------

Below the variable you just created, use echo to print it.

# get bike info
BIKE_INFO=$($PSQL "SELECT size, type FROM bikes WHERE bike_id = $BIKE_ID_TO_RENT")
echo $BIKE_INFO

------------------------------------------------------------------------------------------

Run the script again and go to the rent menu, there should now be one less bike displayed. 
Pick the next bike on the list and rent it using the customer with phone number 555-5555 
again so you can see the variable.

codeally@17c15ec401c5:~/project$ ./bike-shop.sh 

~~~~~ Bike Rental Shop ~~~~~

How may I help you?


1. Rent a bike
2. Return a bike
3. Exit
1

Here are the bikes we have available:
1) 27" Mountain Bike
2) 28" Mountain Bike
3) 29" Mountain Bike
4) 27" Road Bike
5) 28" Road Bike
6) 29" Road Bike
7) 19" BMX Bike
8) 20" BMX Bike

Which one would you like to rent?
2

What's your phone number?
555-5555
28 | Mountain

------------------------------------------------------------------------------------------

It should have printed 28 | Mountain. The message you want to print after someone rents 
a bike would have said 'I have put you down for the 28" Mountain Bike, Me.'. You need 
to format that variable for the message. The sed command can be used to replace 
characters and patterns in text. It looks like this: 
sed s/<regex_pattern_to_replace>/<characters_to_replace_with>/<regex_flags>. 

In the terminal, enter echo '28 | Mountain' | sed 's/ /=/g' to practice.

codeally@17c15ec401c5:~/project$ echo '28 | Mountain' | sed 's/ /=/g'
28=|=Mountain

------------------------------------------------------------------------------------------

The command you used, "piped" a string (28 | Mountain) to the sed command, where it 
replaced all the spaces with =. Enter the same command, but replace all the spaces with 
nothing.

codeally@17c15ec401c5:~/project$ echo '28 | Mountain' | sed 's/ //g'
28|Mountain

------------------------------------------------------------------------------------------

The g regex flag stands for "global". It will replace all instance of the pattern. In this 
case, it replaced all the spaces. Enter the same command but without that flag.

codeally@17c15ec401c5:~/project$ echo '28 | Mountain' | sed 's/ //'

codeally@17c15ec401c5:~/project$ echo '28 | Mountain' | sed 's/ //'
28| Mountain

------------------------------------------------------------------------------------------

That time, only the first instance of the pattern was replaced. The first space was removed. 
Enter the same command, but replace the first instance of " |" (<space>|) with nothing.

codeally@17c15ec401c5:~/project$ echo '28 | Mountain' | sed 's/ |//'
28 Mountain

------------------------------------------------------------------------------------------

Enter the same command, but make the output look like how you want in the message, 
'28" Mountain'.

codeally@17c15ec401c5:~/project$ echo '28 | Mountain' | sed 's/ |/"/'
28" Mountain

------------------------------------------------------------------------------------------

Back in your script, where you echo the BIKE_INFO, pipe the output into a sed command 
that replaces " |" (<space>|) with " so the text will read '<SIZE>" <TYPE>'. 
'28 | Mountain' would become '28" Mountain', for instance.

# get bike info
BIKE_INFO=$($PSQL "SELECT size, type FROM bikes WHERE bike_id = $BIKE_ID_TO_RENT")
echo $BIKE_INFO | sed 's/ |/"/'

(see bike-shop.sh)

------------------------------------------------------------------------------------------

Run the script and rent another bike using the customer with phone number 555-5555 again. 
Make sure the bike info printed looks like you want.

codeally@17c15ec401c5:~/project$ ./bike-shop.sh 

~~~~~ Bike Rental Shop ~~~~~

How may I help you?


1. Rent a bike
2. Return a bike
3. Exit
1

Here are the bikes we have available:
1) 27" Mountain Bike
3) 29" Mountain Bike
4) 27" Road Bike
5) 28" Road Bike
6) 29" Road Bike
7) 19" BMX Bike
8) 20" BMX Bike

Which one would you like to rent?
3

What's your phone number?
555-5555
29" Mountain

------------------------------------------------------------------------------------------

Now it is formatted for the message. Take that echo command and the part that formats it, 
put it in a sub shell, and set the output into a variable named BIKE_INFO_FORMATTED. 
Here's an example: BIKE_INFO_FORMATTED=$(<formatted info here>)

BIKE_INFO_FORMATTED=$(echo $BIKE_INFO | sed 's/ |/\"/')

(see bike-shop.sh)

------------------------------------------------------------------------------------------

What you put the in subshell ($(...)) will be executed, and the result of it will replace 
the subshell. In this case, the formatted bike info was printed when you ran the script 
before, so the BIKE_INFO_FORMATTED variable will be set to that. Below the 
"send to main menu" comment, send users to the main menu with a message that would print 
'I have put you down for the 28" Mountain Bike, Me.' if 'Me' rented the 
'28 inch Mountain Bike'.

# send to main menu
MAIN_MENU "I have put you down for the $BIKE_INFO_FORMATTED Bike, $CUSTOMER_NAME."

(see bike-shop.sh)

------------------------------------------------------------------------------------------

Run the script and rent the next bike on the list. Use the customer with 555-5555 as 
their phone number. When you are done, exit the program.


codeally@17c15ec401c5:~/project$ ./bike-shop.sh 

~~~~~ Bike Rental Shop ~~~~~

How may I help you?


1. Rent a bike
2. Return a bike
3. Exit
1

Here are the bikes we have available:
1) 27" Mountain Bike
4) 27" Road Bike
5) 28" Road Bike
6) 29" Road Bike
7) 19" BMX Bike
8) 20" BMX Bike

Which one would you like to rent?
1

What's your phone number?
555-5555

I have put you down for the 27" Mountain Bike Bike, Me.
How may I help you?


1. Rent a bike
2. Return a bike
3. Exit
3

Thank you for stopping in.

------------------------------------------------------------------------------------------

There's an extra space around the customer's name. You can use sed again to fix that. 
In the terminal, enter echo ' M e ' to print M e with spaces around it to see if you can 
find out how.

codeally@17c15ec401c5:~/project$ echo ' M e '
 M e 

------------------------------------------------------------------------------------------

It printed, but you can only assume there's a space at the end. Place the last command 
in a subshell with quotes around it. Put a period right after the subshell and echo the 
whole thing in the terminal. Here's how it looks: echo "$(echo ' M e ')."

codeally@17c15ec401c5:~/project$ echo "$(echo ' M e ')."
 M e .

------------------------------------------------------------------------------------------

Now you can be certain there's a space at the end. Within the subshell of the last 
command, use a pipe and the sed command to replace the first space with no space. Here's 
the sed replacement pattern you want: 's/ //'.

codeally@a9d950bc1260:~/project$ echo "$(echo ' M e ' | sed 's/ //')."
M e .

------------------------------------------------------------------------------------------

That removed only the first space it found. Change the previous command to replace all 
instances of a space instead of just the first one.

codeally@a9d950bc1260:~/project$ echo "$(echo ' M e ' | sed 's/ //g')."
Me.

------------------------------------------------------------------------------------------

That replaced all the spaces. You only had an extra space at the beginning of the customer 
name. Add a ^ in front of the space in the replacement pattern of the last command to only 
replace a space at the beginning of the text.

codeally@a9d950bc1260:~/project$ echo "$(echo ' M e ' | sed 's/^ //g')."
M e .

------------------------------------------------------------------------------------------

The caret you added means that's the start of the text. So it will replace a space only 
if it's at the beginning. Enter the last command, but add two more spaces (three total) at 
the beginning of the text.

codeally@a9d950bc1260:~/project$ echo "$(echo '   M e ' | sed 's/^ //g')."
  M e .

------------------------------------------------------------------------------------------

The ^  (^<space>) pattern only replaced the first space. Add * at the end of the matching 
pattern to replace all spaces at the beginning of text.

codeally@a9d950bc1260:~/project$ echo "$(echo '   M e ' | sed 's/^ *//g')."
M e .

------------------------------------------------------------------------------------------

The customer name only had an extra space at the beginning. Unsure as to why, but there 
may be others with extra spaces at the end as well. You can match the end of text with $. 
Change the matching pattern of the last command so it replaces a single space at the end. 
The pattern is  $ (<space>$).

codeally@7daa4e049867:~/project$ echo "$(echo '   M e ' | sed 's/ $//g')."
   M e.

------------------------------------------------------------------------------------------

Add two more spaces to the end of the text in the previous command (three spaces total).

codeally@7daa4e049867:~/project$ echo "$(echo '   M e   ' | sed 's/ $//g')."
   M e  .

------------------------------------------------------------------------------------------

The pattern only replaces a single space at the end. Change the last command so it 
replaces all spaces at the end of the text.

codeally@7daa4e049867:~/project$ echo "$(echo '   M e   ' | sed 's/ *$//g')."
   M e.

------------------------------------------------------------------------------------------

That replaced all the spaces at the end of the text. You can use | as an "or" operator 
in a matching pattern to replace one pattern or another. Use it to change the matching 
pattern so it would replace any amount of spaces at the beginning and any amount of spaces 
at the end of the text.

codeally@7daa4e049867:~/project$ echo "$(echo '   M e   ' | sed 's/^ *| *$//g')."
   M e   .

------------------------------------------------------------------------------------------

That didn't work. It doesn't like that "or" (|) operator for some reason. Check the manual 
of the sed command to see if you can find anything.

codeally@7daa4e049867:~/project$ man sed

------------------------------------------------------------------------------------------

Somewhere in there is a flag for using extended regular expressions with sed. That might 
work. Add it to the echo "$(echo '   M e   ' | sed 's/^ *| *$//g')." command that didn't 
work to find out.

codeally@7daa4e049867:~/project$ echo "$(echo '   M e   ' | sed -E 's/^ *| *$//g')."
M e.

------------------------------------------------------------------------------------------

That trimmed all spaces from the front and end of the text. Back in the last message 
of your script, place the CUSTOMER_NAME variable in a subshell, echo and pipe it into a 
sed command that removes all spaces from the front and back. Use the same method you used 
in the terminal.

# send to main menu
MAIN_MENU "I have put you down for the $BIKE_INFO_FORMATTED 
    Bike, $(echo $CUSTOMER_NAME | sed -E 's/^ *| *$//g')."

(see bike-shop.sh)

------------------------------------------------------------------------------------------

Run the script and rent another bike with the customer whose phone number is 555-5555. 
When you are done, exit the program.

codeally@7daa4e049867:~/project$ ./bike-shop.sh 

~~~~~ Bike Rental Shop ~~~~~

How may I help you?

1. Rent a bike
2. Return a bike
3. Exit
1

Here are the bikes we have available:
5) 28" Road Bike
6) 29" Road Bike
7) 19" BMX Bike
8) 20" BMX Bike
9) 21" BMX Bike

Which one would you like to rent?
5

What's your phone number?
555-5555

I have put you down for the 28" Road Bike, Me.
How may I help you?

1. Rent a bike
2. Return a bike
3. Exit
3

Thank you for stopping in.

------------------------------------------------------------------------------------------

Run the script again. Rent another bike, use 000-0000 as the phone number this time, 
and Test as the name to create a new customer. When you are done, exit the program.

codeally@7daa4e049867:~/project$ ./bike-shop.sh 

~~~~~ Bike Rental Shop ~~~~~

How may I help you?

1. Rent a bike
2. Return a bike
3. Exit
1

Here are the bikes we have available:
6) 29" Road Bike
7) 19" BMX Bike
8) 20" BMX Bike
9) 21" BMX Bike

Which one would you like to rent?
6

What's your phone number?
000-0000

What's your name?
Test

I have put you down for the 29" Road Bike, Test.
How may I help you?

1. Rent a bike
2. Return a bike
3. Exit
3

Thank you for stopping in.

------------------------------------------------------------------------------------------

Run the script again. Rent another bike with the customer you just created. When you are 
done, exit the program.

codeally@7daa4e049867:~/project$ ./bike-shop.sh 

~~~~~ Bike Rental Shop ~~~~~

How may I help you?

1. Rent a bike
2. Return a bike
3. Exit
1

Here are the bikes we have available:
7) 19" BMX Bike
8) 20" BMX Bike
9) 21" BMX Bike

Which one would you like to rent?
7

What's your phone number?
000-0000

I have put you down for the 19" BMX Bike, Test.
How may I help you?

1. Rent a bike
2. Return a bike
3. Exit
3

Thank you for stopping in.

------------------------------------------------------------------------------------------

In the psql prompt, view all the data in your bikes table in order by the bike_id.

bikes=> SELECT * FROM bikes ORDER BY bike_id;
bikes=>                      
+---------+----------+------+-----------+
| bike_id |   type   | size | available |
+---------+----------+------+-----------+
|       1 | Mountain |   27 | f         |
|       2 | Mountain |   28 | f         |
|       3 | Mountain |   29 | f         |
|       4 | Road     |   27 | f         |
|       5 | Road     |   28 | f         |
|       6 | Road     |   29 | f         |
|       7 | BMX      |   19 | f         |
|       8 | BMX      |   20 | t         |
|       9 | BMX      |   21 | t         |
+---------+----------+------+-----------+
(9 rows)

------------------------------------------------------------------------------------------

There should be two bikes left available to rent. Next, look at all the data in the 
customers table.

bikes=> SELECT * FROM customers;
                 
+-------------+----------+------+
| customer_id |  phone   | name |
+-------------+----------+------+
|           1 | 555-5555 | Me   |
|           2 | 000-0000 | Test |
+-------------+----------+------+
(2 rows)

------------------------------------------------------------------------------------------

There should two customers in that table now. Lastly, look at all the data in the 
rentals table.

bikes=> SELECT * FROM rentals;
bikes=>                                   
+-----------+-------------+---------+-------------+---------------+
| rental_id | customer_id | bike_id | date_rented | date_returned |
+-----------+-------------+---------+-------------+---------------+
|         1 |           1 |       1 | 2021-05-25  |               |
|         2 |           1 |       2 | 2021-05-25  |               |
|         3 |           1 |       3 | 2021-05-27  |               |
|         4 |           1 |       4 | 2021-05-27  |               |
|         5 |           1 |       5 | 2022-10-27  |               |
|         6 |           2 |       6 | 2022-10-27  |               |
|         7 |           2 |       7 | 2022-10-27  |               |
+-----------+-------------+---------+-------------+---------------+
(7 rows)

------------------------------------------------------------------------------------------

The rent functionality looks like it all works. Delete the echo Return Menu line in the 
RETURN_MENU function so you can get started with that.

RETURN_MENU() {
  
}

(see bike-shop.sh)

------------------------------------------------------------------------------------------

Add three single line comments to the return menu function; "get customer info", 
"if not found", and "send to main menu", in that order.

RETURN_MENU() {
  # get customer info
  
  # if not found 
  
  # send to main menu
}

(see bike-shop.sh)

------------------------------------------------------------------------------------------

Below the get customer info comment you just added, print "What's your phone number?" 
with a new line in front of the sentence.

RETURN_MENU() {
  # get customer info
  echo -e "\nWhat's your phone number?"
  
  # if not found 
  
  # send to main menu
}

(see bike-shop.sh)

------------------------------------------------------------------------------------------

Just below that, use read to get input into a PHONE_NUMBER variable.

RETURN_MENU() {
  # get customer info
  echo -e "\nWhat's your phone number?"
  read PHONE_NUMBER

  # if not found 
  
  # send to main menu
}

(see bike-shop.sh)

------------------------------------------------------------------------------------------

Just below that, set the CUSTOMER_ID variable to a query that gets the customer ID from 
the database using the phone number they gave you.

RETURN_MENU() {
  # get customer info
  echo -e "\nWhat's your phone number?"
  read PHONE_NUMBER

  CUSTOMER_ID=$($PSQL "SELECT customer_id FROM customers WHERE phone='$PHONE_NUMBER'")

  # if not found 
  
  # send to main menu
}

(see bike-shop.sh)

------------------------------------------------------------------------------------------

If they are in the database, the variable will be their customer_id. If not, it will 
be empty. Below the if not found comment, add an if statement that checks if it's empty. 
Put the send to main menu comment in the then area.

RETURN_MENU() {
  # get customer info
  echo -e "\nWhat's your phone number?"
  read PHONE_NUMBER

  CUSTOMER_ID=$($PSQL "SELECT customer_id FROM customers WHERE phone='$PHONE_NUMBER'")

  # if not found 
  if [[ -z $CUSTOMER_ID ]]
  then
    # send to main menu
  fi
}

(see bike-shop.sh)

------------------------------------------------------------------------------------------

If the customer isn't found, send them to the main menu with the message 
"I could not find a record for that phone number."

RETURN_MENU() {
  # get customer info
  echo -e "\nWhat's your phone number?"
  read PHONE_NUMBER

  CUSTOMER_ID=$($PSQL "SELECT customer_id FROM customers WHERE phone='$PHONE_NUMBER'")

  # if not found 
  if [[ -z $CUSTOMER_ID ]]
  then
    # send to main menu
    MAIN_MENU "I could not find a record for that phone number."
  fi
}

(see bike-shop.sh)

------------------------------------------------------------------------------------------

Run the script and go to the return menu. Enter a phone number that is not in the 
database. When you are done, exit the program.

codeally@7daa4e049867:~/project$ ./bike-shop.sh 

~~~~~ Bike Rental Shop ~~~~~

How may I help you?

1. Rent a bike
2. Return a bike
3. Exit
2

What's your phone number?
333-3333

I could not find a record for that phone number.
How may I help you?

1. Rent a bike
2. Return a bike
3. Exit
3

Thank you for stopping in.

------------------------------------------------------------------------------------------

Add an else to the if condition for if the phone number is found in the database. 
Place "get customer's rentals", "if no rentals", and "send to main menu" in the else 
area as single line comments.

# if not found 
if [[ -z $CUSTOMER_ID ]]
then
    # send to main menu
    MAIN_MENU "I could not find a record for that phone number."
else
    # get customer's rentals

    # if no rentals

    # send to main menu
fi

(see bike-shop.sh)

------------------------------------------------------------------------------------------

You want to find out what rentals a customer has using their phone number and display 
them. You will need to join all the tables. Start by using the psql prompt to view all 
the data in the bikes table.

bikes=> SELECT * FROM bikes;
                     
+---------+----------+------+-----------+
| bike_id |   type   | size | available |
+---------+----------+------+-----------+
|       8 | BMX      |   20 | t         |
|       9 | BMX      |   21 | t         |
|       1 | Mountain |   27 | f         |
|       2 | Mountain |   28 | f         |
|       3 | Mountain |   29 | f         |
|       4 | Road     |   27 | f         |
|       5 | Road     |   28 | f         |
|       6 | Road     |   29 | f         |
|       7 | BMX      |   19 | f         |
+---------+----------+------+-----------+
(9 rows)

------------------------------------------------------------------------------------------

Next, use a LEFT JOIN with bikes as the left table to join the bikes and rentals tables. 
Use the USING keyword to join the two tables.

1. You need the SELECT, FROM, LEFT JOIN, and USING keywords
2. Here's an example: SELECT <column> FROM <table_1> LEFT JOIN <table_2> USING(<foreign_key>)


bikes=> SELECT * FROM bikes LEFT JOIN rentals USING(bike_id);
bikes=>                                                  
+---------+----------+------+-----------+-----------+-------------+-------------+---------------+
| bike_id |   type   | size | available | rental_id | customer_id | date_rented | date_returned |
+---------+----------+------+-----------+-----------+-------------+-------------+---------------+
|       8 | BMX      |   20 | t         |           |             |             |               |
|       9 | BMX      |   21 | t         |           |             |             |               |
|       1 | Mountain |   27 | f         |         1 |           1 | 2021-05-25  |               |
|       2 | Mountain |   28 | f         |         2 |           1 | 2021-05-25  |               |
|       3 | Mountain |   29 | f         |         3 |           1 | 2021-05-27  |               |
|       4 | Road     |   27 | f         |         4 |           1 | 2021-05-27  |               |
|       5 | Road     |   28 | f         |         5 |           1 | 2022-10-27  |               |
|       6 | Road     |   29 | f         |         6 |           2 | 2022-10-27  |               |
|       7 | BMX      |   19 | f         |         7 |           2 | 2022-10-27  |               |
+---------+----------+------+-----------+-----------+-------------+-------------+---------------+
(9 rows)


------------------------------------------------------------------------------------------

You only need the bikes that are being rented. Use an inner join with the same two tables 
to only get those. Use the USING keyword again.

bikes=> SELECT * FROM bikes INNER JOIN rentals USING(bike_id);
bikes=>                                                  
+---------+----------+------+-----------+-----------+-------------+-------------+---------------+
| bike_id |   type   | size | available | rental_id | customer_id | date_rented | date_returned |
+---------+----------+------+-----------+-----------+-------------+-------------+---------------+
|       1 | Mountain |   27 | f         |         1 |           1 | 2021-05-25  |               |
|       2 | Mountain |   28 | f         |         2 |           1 | 2021-05-25  |               |
|       3 | Mountain |   29 | f         |         3 |           1 | 2021-05-27  |               |
|       4 | Road     |   27 | f         |         4 |           1 | 2021-05-27  |               |
|       5 | Road     |   28 | f         |         5 |           1 | 2022-10-27  |               |
|       6 | Road     |   29 | f         |         6 |           2 | 2022-10-27  |               |
|       7 | BMX      |   19 | f         |         7 |           2 | 2022-10-27  |               |
+---------+----------+------+-----------+-----------+-------------+-------------+---------------+
(7 rows)

------------------------------------------------------------------------------------------

Add a join to the previous command that joins the last table so you can get the 
customer information. Use an INNER JOIN and the USING keyword again.

bikes=> SELECT * FROM bikes INNER JOIN rentals USING(bike_id) INNER JOIN 
    customers USING(customer_id);
                                                          
+-------------+---------+----------+------+-----------+-----------+-------------+---------------+----------+------+
| customer_id | bike_id |   type   | size | available | rental_id | date_rented | date_returned |  phone   | name |
+-------------+---------+----------+------+-----------+-----------+-------------+---------------+----------+------+
|           1 |       1 | Mountain |   27 | f         |         1 | 2021-05-25  |               | 555-5555 | Me   |
|           1 |       2 | Mountain |   28 | f         |         2 | 2021-05-25  |               | 555-5555 | Me   |
|           1 |       3 | Mountain |   29 | f         |         3 | 2021-05-27  |               | 555-5555 | Me   |
|           1 |       4 | Road     |   27 | f         |         4 | 2021-05-27  |               | 555-5555 | Me   |
|           1 |       5 | Road     |   28 | f         |         5 | 2022-10-27  |               | 555-5555 | Me   |
|           2 |       6 | Road     |   29 | f         |         6 | 2022-10-27  |               | 000-0000 | Test |
|           2 |       7 | BMX      |   19 | f         |         7 | 2022-10-27  |               | 000-0000 | Test |
+-------------+---------+----------+------+-----------+-----------+-------------+---------------+----------+------+
(7 rows)

------------------------------------------------------------------------------------------

Add two conditions to the last query to narrow down the results to the bikes that are 
currently being rented by customer with 555-5555 as their phone number. The second 
condition should check the date_returned column.

bikes=> SELECT * FROM bikes INNER JOIN rentals USING(bike_id) INNER JOIN customers 
    USING(customer_id) WHERE phone = '555-5555' AND date_returned IS NULL;

+-------------+---------+----------+------+-----------+-----------+-------------+---------------+----------+------+
| customer_id | bike_id |   type   | size | available | rental_id | date_rented | date_returned |  phone   | name |
+-------------+---------+----------+------+-----------+-----------+-------------+---------------+----------+------+
|           1 |       1 | Mountain |   27 | f         |         1 | 2021-05-25  |               | 555-5555 | Me   |
|           1 |       2 | Mountain |   28 | f         |         2 | 2021-05-25  |               | 555-5555 | Me   |
|           1 |       3 | Mountain |   29 | f         |         3 | 2021-05-27  |               | 555-5555 | Me   |
|           1 |       4 | Road     |   27 | f         |         4 | 2021-05-27  |               | 555-5555 | Me   |
|           1 |       5 | Road     |   28 | f         |         5 | 2022-10-27  |               | 555-5555 | Me   |
+-------------+---------+----------+------+-----------+-----------+-------------+---------------+----------+------+
(5 rows)

------------------------------------------------------------------------------------------

Now you have all the rentals for one specific customer. Only get the columns you need to 
display the bike information to them. They are the same three columns you used to display 
the list of available bikes.

bikes=> SELECT bike_id, type, size FROM bikes INNER JOIN rentals USING(bike_id) INNER JOIN 
    customers USING(customer_id) WHERE phone = '555-5555' AND date_returned IS NULL;
               
+---------+----------+------+
| bike_id |   type   | size |
+---------+----------+------+
|       1 | Mountain |   27 |
|       2 | Mountain |   28 |
|       3 | Mountain |   29 |
|       4 | Road     |   27 |
|       5 | Road     |   28 |
+---------+----------+------+
(5 rows)

------------------------------------------------------------------------------------------

One more thing, order the results of the last query by their bike_id column.

bikes=> SELECT bike_id, type, size FROM bikes INNER JOIN rentals USING(bike_id) 
    INNER JOIN customers USING(customer_id) WHERE phone = '555-5555' AND date_returned 
    IS NULL ORDER BY bike_id;
               
+---------+----------+------+
| bike_id |   type   | size |
+---------+----------+------+
|       1 | Mountain |   27 |
|       2 | Mountain |   28 |
|       3 | Mountain |   29 |
|       4 | Road     |   27 |
|       5 | Road     |   28 |
+---------+----------+------+
(5 rows)

------------------------------------------------------------------------------------------

That's the query you will need to use to get the bikes a customer is renting. In your 
script below the get customer's rentals comment. Create a CUSTOMER_RENTALS variable that 
gets the rentals for the customer. Use the PHONE_NUMBER variable to get them.

# get customer's rentals
CUSTOMER_RENTALS=$($PSQL "SELECT bike_id, type, size FROM bikes INNER JOIN rentals 
    USING(bike_id) INNER JOIN customers USING(customer_id) WHERE phone = '$PHONE_NUMBER' 
    AND date_returned IS NULL ORDER BY bike_id;")

(see bike-shop.sh)

------------------------------------------------------------------------------------------

Below the variable you just created, use echo to print it. Make sure to put double 
quotes around it.

echo "$CUSTOMER_RENTALS"

(see bike-shop.sh)

------------------------------------------------------------------------------------------

Run the script and go to the return menu. Enter 555-5555 for the phone number to see the 
rentals for Me.

codeally@7daa4e049867:~/project$ ./bike-shop.sh 

~~~~~ Bike Rental Shop ~~~~~

How may I help you?

1. Rent a bike
2. Return a bike
3. Exit
2

What's your phone number?
555-5555
       1 | Mountain |   27
       2 | Mountain |   28
       3 | Mountain |   29
       4 | Road     |   27
       5 | Road     |   28

------------------------------------------------------------------------------------------

The query is working. If the customer has no rentals, the variable will be empty. 
Below the "if no rentals" comment, add an if condition that checks if it's empty. 
Put the "send to main menu" comment in the then area again.

# if no rentals
if [[ -z $CUSTOMER_RENTALS ]]
then
    # send to main menu
fi

(see bike-shop.sh)

------------------------------------------------------------------------------------------

If the customer has no rentals, send them to the main menu with the message 
"You do not have any bikes rented." Add the code below the next comment.

# if no rentals
if [[ -z $CUSTOMER_RENTALS ]]
then
    # send to main menu
    MAIN_MENU "You do not have any bikes rented."
fi

(see bike-shop.sh)

------------------------------------------------------------------------------------------

Add an else to the condition for when the customer does have rentals. Place four single 
line comments in it; display rented bikes, ask for bike to return, if not a number, and 
send to main menu.

# if no rentals
if [[ -z $CUSTOMER_RENTALS ]]
then
    # send to main menu
    MAIN_MENU "You do not have any bikes rented."
else
    # display rented bikes

    # ask for bike to return

    # if not a number

    # send to main menu
fi

(see bike-shop.sh)

------------------------------------------------------------------------------------------

Below the "display rented bikes" comment, print "Here are your rentals:" with a new line 
in front of it.

# display rented bikes
echo -e "\nHere are your rentals:"

(see bike-shop.sh)

------------------------------------------------------------------------------------------

Move the echo $CUSTOMER_RENTALS line to below the line you just printed.

# display rented bikes
echo -e "\nHere are your rentals:"
echo "$CUSTOMER_RENTALS"

(see bike-shop.sh)

------------------------------------------------------------------------------------------

Run the script and go to the return menu. Enter 555-5555 for the phone number to see 
the rented bikes.

------------------------------------------------------------------------------------------

codeally@7daa4e049867:~/project$ ./bike-shop.sh 

~~~~~ Bike Rental Shop ~~~~~

How may I help you?

1. Rent a bike
2. Return a bike
3. Exit
2

What's your phone number?
555-5555

Here are your rentals:
       1 | Mountain |   27
       2 | Mountain |   28
       3 | Mountain |   29
       4 | Road     |   27
       5 | Road     |   28

(see bike-shop.sh)

------------------------------------------------------------------------------------------

Where you print the list of rented bikes, pipe the command into a while loop that reads 
the data. You should read the data into BIKE_ID, BAR, TYPE, BAR, and SIZE variables. 
Make it print each rented bike in the same fashion as the list of available bikes.

# display rented bikes
echo -e "\nHere are your rentals:"
echo "$CUSTOMER_RENTALS" | while read BIKE_ID BAR TYPE BAR SIZE
do
    echo "$BIKE_ID) $SIZE\" $TYPE Bike"
done

(see bike-shop.sh)

------------------------------------------------------------------------------------------

Run the script and go to the return menu. Enter the same phone number again to make 
sure the list is showing up correctly.

codeally@7daa4e049867:~/project$ ./bike-shop.sh 

~~~~~ Bike Rental Shop ~~~~~

How may I help you?

1. Rent a bike
2. Return a bike
3. Exit
2

What's your phone number?
555-5555

Here are your rentals:
1) 27" Mountain Bike
2) 28" Mountain Bike
3) 29" Mountain Bike
4) 27" Road Bike
5) 28" Road Bike

------------------------------------------------------------------------------------------

Below the "ask for bike to return" comment, print "Which one would you like to return?" 
with a new line in front of it.

# ask for bike to return
echo -e "\nWhich one would you like to return?"

(see bike-shop.sh)

------------------------------------------------------------------------------------------

Below the line you just printed, read input into a BIKE_ID_TO_RETURN variable.

# ask for bike to return
echo -e "\nWhich one would you like to return?"
read BIKE_ID_TO_RETURN

(see bike-shop.sh)

------------------------------------------------------------------------------------------

Below the "if not a number" comment, check if the input for the bike ID to return is a 
number using the same method you did earlier. Place the "send to main menu" comment 
in the statement.

# ask for bike to return
echo -e "\nWhich one would you like to return?"
read BIKE_ID_TO_RETURN

# if not a number
if [[ ! $BIKE_ID_TO_RETURN =~ ^[0-9]+$ ]]
then
    # send to main menu
fi

(see bike-shop.sh)

------------------------------------------------------------------------------------------

If they don't input a number, send them to the main menu with 
"That is not a valid bike number." as the message.

# send to main menu
MAIN_MENU "That is not a valid bike number."

(see bike-shop.sh)

------------------------------------------------------------------------------------------

Add an else for when they do input a number. Place "check if input is rented", 
"if input not rented", and "send to main menu" single line comments in it.

# if not a number
if [[ ! $BIKE_ID_TO_RETURN =~ ^[0-9]+$ ]]
then
    # send to main menu
    MAIN_MENU "That is not a valid bike number."
else
    # check if input is rented

    # if input not rented

    # send to main menu
fi

(see bike-shop.sh)

------------------------------------------------------------------------------------------

You need to check if the input is a bike_id rented by the customer so you can return it. 
In the psql prompt, join the rentals and customers tables with an INNER JOIN using the 
USING keyword.

bikes=> SELECT * FROM rentals INNER JOIN customers USING(customer_id);
                                           
+-------------+-----------+---------+-------------+---------------+----------+------+
| customer_id | rental_id | bike_id | date_rented | date_returned |  phone   | name |
+-------------+-----------+---------+-------------+---------------+----------+------+
|           1 |         1 |       1 | 2021-05-25  |               | 555-5555 | Me   |
|           1 |         2 |       2 | 2021-05-25  |               | 555-5555 | Me   |
|           1 |         3 |       3 | 2021-05-27  |               | 555-5555 | Me   |
|           1 |         4 |       4 | 2021-05-27  |               | 555-5555 | Me   |
|           1 |         5 |       5 | 2022-10-27  |               | 555-5555 | Me   |
|           2 |         6 |       6 | 2022-10-27  |               | 000-0000 | Test |
|           2 |         7 |       7 | 2022-10-27  |               | 000-0000 | Test |
+-------------+-----------+---------+-------------+---------------+----------+------+
(7 rows)

------------------------------------------------------------------------------------------

Add three conditions to the previous query. Check the phone, bike_id, and date_returned 
columns to narrow the results to the first bike you rented with Me.

bikes=> SELECT * FROM rentals INNER JOIN customers USING(customer_id) WHERE 
    phone = '555-5555' AND bike_id = 1 AND date_returned IS NULL;
                                           
+-------------+-----------+---------+-------------+---------------+----------+------+
| customer_id | rental_id | bike_id | date_rented | date_returned |  phone   | name |
+-------------+-----------+---------+-------------+---------------+----------+------+
|           1 |         1 |       1 | 2021-05-25  |               | 555-5555 | Me   |
+-------------+-----------+---------+-------------+---------------+----------+------+
(1 row)

------------------------------------------------------------------------------------------

You only need to know what bike is going to be returned. Narrow the columns from the 
last query to only get the one column you would need for returning a bike.

bikes=> SELECT rental_id FROM rentals INNER JOIN customers USING(customer_id) WHERE 
    phone = '555-5555' AND bike_id = 1 AND date_returned IS NULL;
       
+-----------+
| rental_id |
+-----------+
|         1 |
+-----------+
(1 row)

------------------------------------------------------------------------------------------

Back in the script, below the "check if input is rented" comment, create a RENTAL_ID 
variable that gets the rental ID of the bike that was input.

# check if input is rented
RENTAL_ID=$($PSQL "SELECT rental_id FROM rentals INNER JOIN customers USING(customer_id) 
    WHERE phone = '$PHONE_NUMBER' AND bike_id = $BIKE_ID_TO_RETURN AND 
    date_returned IS NULL;")

(see bike-shop.sh)

------------------------------------------------------------------------------------------

Below the "if input not rented" comment, add an if that checks if the RENTAL_ID variable 
is empty. Place the "send to main menu" comment in the then area.

# if input not rented
if [[ -z $RENTAL_ID ]]
then
    # send to main menu
fi

(see bike-shop.sh)

------------------------------------------------------------------------------------------

If the input isn't rented by the given customer, send them to the main menu with 
"You do not have that bike rented." as the message.

# send to main menu
MAIN_MENU "You do not have that bike rented."

(see bike-shop.sh)

------------------------------------------------------------------------------------------

Add an else to the if condition you just added. Use echo to print 
"Rental ID $RENTAL_ID found" in it so you can see if it's all working.

# if input not rented
if [[ -z $RENTAL_ID ]]
then
    # send to main menu
    MAIN_MENU "You do not have that bike rented."
else
    echo "Rental ID $RENTAL_ID found"
fi

(see bike-shop.sh)

------------------------------------------------------------------------------------------

Run the script and go to the return menu. Enter 555-5555 to see the rented bikes. Input 
a bike that isn't on the list, then go to the menu again and input a bike that is on 
the list.

codeally@7daa4e049867:~/project$ ./bike-shop.sh 

~~~~~ Bike Rental Shop ~~~~~

How may I help you?

1. Rent a bike
2. Return a bike
3. Exit
2

What's your phone number?
555-5555

Here are your rentals:
1) 27" Mountain Bike
2) 28" Mountain Bike
3) 29" Mountain Bike
4) 27" Road Bike
5) 28" Road Bike

Which one would you like to return?
8

You do not have that bike rented.
How may I help you?

1. Rent a bike
2. Return a bike
3. Exit
2

What's your phone number?
555-5555

Here are your rentals:
1) 27" Mountain Bike
2) 28" Mountain Bike
3) 29" Mountain Bike
4) 27" Road Bike
5) 28" Road Bike

Which one would you like to return?
1
Rental ID          1 found

------------------------------------------------------------------------------------------

Looks like it works. Delete the line where you print the rental ID.


# if input not rented
if [[ -z $RENTAL_ID ]]
then
    # send to main menu
    MAIN_MENU "You do not have that bike rented."
else
    
fi

(see bike-shop.sh)

------------------------------------------------------------------------------------------

Add three single line comments in the else area; "update date_returned", 
"set bike availability to true", and "send to main menu".

# if input not rented
if [[ -z $RENTAL_ID ]]
then
    # send to main menu
    MAIN_MENU "You do not have that bike rented."
else
    # update date_returned

    # set bike availability to true

    # send to main menu
fi

(see bike-shop.sh)

------------------------------------------------------------------------------------------

After a person picks a bike to return and you know that it's a bike they have rented, 
you need to update all the info in the database to return it. Below the 
"update date_returned" comment, create a RETURN_BIKE_RESULT variable that sets the 
date_returned column to NOW() for the bike rented. Use the RENTAL_ID to figure out which 
row to update.

# update date_returned
RETURN_BIKE_RESULT=$($PSQL "UPDATE rentals SET date_returned = NOW() WHERE 
    rental_id = $RENTAL_ID")

(see bike-shop.sh)

------------------------------------------------------------------------------------------

That should update the rentals table. Lastly, you need to make the bike available again. 
Below the "set bike availability to true" comment, create a SET_TO_TRUE_RESULT variable 
that makes the bike available again.

# set bike availability to true
SET_TO_TRUE_RESULT=$($PSQL "UPDATE bikes SET available = TRUE WHERE 
    bike_id = $BIKE_ID_TO_RETURN")

(see bike-shop.sh)

------------------------------------------------------------------------------------------

After all that is done, send them to the main menu with 
"Thank you for returning your bike." as the message.

# send to main menu
MAIN_MENU "Thank you for returning your bike."

(see bike-shop.sh)

------------------------------------------------------------------------------------------

Run the script and return one of the bikes that Me has rented out. When you are done, 
exit the program.

codeally@7daa4e049867:~/project$ ./bike-shop.sh 

~~~~~ Bike Rental Shop ~~~~~

How may I help you?

1. Rent a bike
2. Return a bike
3. Exit
2

What's your phone number?
555-5555

Here are your rentals:
1) 27" Mountain Bike
2) 28" Mountain Bike
3) 29" Mountain Bike
4) 27" Road Bike
5) 28" Road Bike

Which one would you like to return?
1

Thank you for returning your bike.
How may I help you?

1. Rent a bike
2. Return a bike
3. Exit
3

Thank you for stopping in.

------------------------------------------------------------------------------------------

In the psql prompt, view all the data in the rentals table.

bikes=> SELECT * FROM rentals;
                                  
+-----------+-------------+---------+-------------+---------------+
| rental_id | customer_id | bike_id | date_rented | date_returned |
+-----------+-------------+---------+-------------+---------------+
|         2 |           1 |       2 | 2021-05-25  |               |
|         3 |           1 |       3 | 2021-05-27  |               |
|         4 |           1 |       4 | 2021-05-27  |               |
|         5 |           1 |       5 | 2022-10-27  |               |
|         6 |           2 |       6 | 2022-10-27  |               |
|         7 |           2 |       7 | 2022-10-27  |               |
|         1 |           1 |       1 | 2021-05-25  | 2022-10-27    |
+-----------+-------------+---------+-------------+---------------+
(7 rows)

------------------------------------------------------------------------------------------

Now the rental has been returned. View all the data in the bikes table in order by 
their bike_id.

bikes=> SELECT * FROM bikes ORDER BY bike_id;
                     
+---------+----------+------+-----------+
| bike_id |   type   | size | available |
+---------+----------+------+-----------+
|       1 | Mountain |   27 | t         |
|       2 | Mountain |   28 | f         |
|       3 | Mountain |   29 | f         |
|       4 | Road     |   27 | f         |
|       5 | Road     |   28 | f         |
|       6 | Road     |   29 | f         |
|       7 | BMX      |   19 | f         |
|       8 | BMX      |   20 | t         |
|       9 | BMX      |   21 | t         |
+---------+----------+------+-----------+
(9 rows)

------------------------------------------------------------------------------------------

And the bike is available again. This is the last step. Run the script once more. 
Feel free to play around, rent and return some bikes. When you are ready to be done, 
return all the bikes you rented and exit the program.

codeally@7daa4e049867:~/project$ ./bike-shop.sh 

~~~~~ Bike Rental Shop ~~~~~

How may I help you?

1. Rent a bike
2. Return a bike
3. Exit
1

Here are the bikes we have available:
1) 27" Mountain Bike
8) 20" BMX Bike
9) 21" BMX Bike

Which one would you like to rent?
1

What's your phone number?
555-5555

I have put you down for the 27" Mountain Bike, Me.
How may I help you?

1. Rent a bike
2. Return a bike
3. Exit
2

What's your phone number?
555-5555

Here are your rentals:
1) 27" Mountain Bike
2) 28" Mountain Bike
3) 29" Mountain Bike
4) 27" Road Bike
5) 28" Road Bike

Which one would you like to return?
1

Thank you for returning your bike.
How may I help you?

1. Rent a bike
2. Return a bike
3. Exit
2

What's your phone number?
555-5555

Here are your rentals:
2) 28" Mountain Bike
3) 29" Mountain Bike
4) 27" Road Bike
5) 28" Road Bike

Which one would you like to return?
2

Thank you for returning your bike.
How may I help you?

1. Rent a bike
2. Return a bike
3. Exit
2

What's your phone number?
555-5555

Here are your rentals:
3) 29" Mountain Bike
4) 27" Road Bike
5) 28" Road Bike

Which one would you like to return?
3

Thank you for returning your bike.
How may I help you?

1. Rent a bike
2. Return a bike
3. Exit
2

What's your phone number?
555-5555

Here are your rentals:
4) 27" Road Bike
5) 28" Road Bike

Which one would you like to return?
4

Thank you for returning your bike.
How may I help you?

1. Rent a bike
2. Return a bike
3. Exit
2

What's your phone number?
555-5555

Here are your rentals:
5) 28" Road Bike

Which one would you like to return?
5

Thank you for returning your bike.
How may I help you?

1. Rent a bike
2. Return a bike
3. Exit
2

What's your phone number?
555-5555

You do not have any bikes rented.
How may I help you?

1. Rent a bike
2. Return a bike
3. Exit
2

What's your phone number?
000-0000

Here are your rentals:
6) 29" Road Bike
7) 19" BMX Bike

Which one would you like to return?
6

Thank you for returning your bike.
How may I help you?

1. Rent a bike
2. Return a bike
3. Exit
2

What's your phone number?
000-0000

Here are your rentals:
7) 19" BMX Bike

Which one would you like to return?
7

Thank you for returning your bike.
How may I help you?

1. Rent a bike
2. Return a bike
3. Exit
2

What's your phone number?
000-0000

You do not have any bikes rented.
How may I help you?

1. Rent a bike
2. Return a bike
3. Exit
3

Thank you for stopping in.

------------------------------------------------------------------------------------------