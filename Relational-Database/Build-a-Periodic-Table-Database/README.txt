==================================================
Build a Periodic Table Database
==================================================

This is one of the required projects to earn your certification. 
For this project, you will create Bash a script to get information about chemical 
elements from a periodic table database.

Step 1: Complete the project
The project runs in a virtual machine, complete the user stories described in there 
and get all the tests to pass to finish step 1.
Important: After you pass all the project tests, save a dump of your database into a 
periodic_table.sql file, as well as your element.sh file, so you can complete step 2. 
There will be instructions on how to do that within the virtual machine.

Instructions
You are started with a periodic_table database that has information about some 
chemical elements. You can connect to it by entering 
psql --username=freecodecamp --dbname=periodic_table in the terminal. 
You may want to get a little familiar with the existing tables, columns, and rows. 
Read the instructions below and complete user stories to finish the project. 
Certain tests may not pass until other user stories are complete. Good luck!


Part 1: Fix the database
There are some mistakes in the database that need to be fixed or changed. 
See the user stories below for what to change.

Part 2: Create your git repository
You need to make a small bash program. The code needs to be version controlled with git, 
so you will need to turn the suggested folder into a git repository.

Part 3: Create the script
Lastly, you need to make a script that accepts an argument in the form of an atomic number, 
symbol, or name of an element and outputs some information about the given element.

Notes:
If you leave your virtual machine, your database may not be saved. You can make a dump of 
it by entering pg_dump -cC --inserts -U freecodecamp periodic_table > periodic_table.sql 
in a bash terminal (not the psql one). It will save the commands to rebuild your database 
in periodic_table.sql. The file will be located where the command was entered. If it's 
anything inside the project folder, the file will be saved in the VM. You can rebuild the 
database by entering psql -U postgres < periodic_table.sql in a terminal where the .sql 
file is.

If you are saving your progress on freeCodeCamp.org, after getting all the tests to pass, 
follow the instructions above to save a dump of your database. Save the periodic_table.sql 
file, as well as the final version of your element.sh file, in a public repository and 
submit the URL to it on freeCodeCamp.org.


Complete the tasks below
You should rename the weight column to atomic_mass

You should rename the melting_point column to melting_point_celsius and the boiling_point 
column to boiling_point_celsius

Your melting_point_celsius and boiling_point_celsius columns should not accept null values

You should add the UNIQUE constraint to the symbol and name columns from the elements table

Your symbol and name columns should have the NOT NULL constraint

You should set the atomic_number column from the properties table as a foreign key that 
references the column of the same name in the elements table

You should create a types table that will store the three types of elements

Your types table should have a type_id column that is an integer and the primary key

Your types table should have a type column that's a VARCHAR and cannot be null. It will 
store the different types from the type column in the properties table

You should add three rows to your types table whose values are the three different types 
from the properties table

Your properties table should have a type_id foreign key column that references the type_id 
column from the types table. It should be an INT with the NOT NULL constraint

Each row in your properties table should have a type_id value that links to the correct type 
from the types table

You should capitalize the first letter of all the symbol values in the elements table. 
Be careful to only capitalize the letter and not change any others

You should remove all the trailing zeros after the decimals from each row of the atomic_mass 
column. You may need to adjust a data type to DECIMAL for this. Be careful not to change the 
value

You should add the element with atomic number 9 to your database. Its name is Fluorine, 
symbol is F, mass is 18.998, melting point is -220, boiling point is -188.1, and it's a 
nonmetal

You should add the element with atomic number 10 to your database. Its name is Neon, 
symbol is Ne, mass is 20.18, melting point is -248.6, boiling point is -246.1, and it's a 
nonmetal

You should create a periodic_table folder in the project folder and turn it into a git 
repository with git init

Your repository should have a main branch with all your commits

Your periodic_table repo should have at least five commits

You should create an element.sh file in your repo folder for the program I want you to make

Your script (.sh) file should have executable permissions

If you run ./element.sh, it should output Please provide an element as an argument. and 
finish running.

If you run ./element.sh 1, ./element.sh H, or ./element.sh Hydrogen, it should output 
"The element with atomic number 1 is Hydrogen (H). It's a nonmetal, with a mass of 1.008 amu. 
Hydrogen has a melting point of -259.1 celsius and a boiling point of -252.9 celsius."

If you run ./element.sh script with another element as input, you should get the same 
output but with information associated with the given element.

If the argument input to your element.sh script doesn't exist as an atomic_number, symbol, 
or name in the database, the output should be I could not find that element in the database.

The message for the first commit in your repo should be Initial commit

The rest of the commit messages should start with fix:, feat:, refactor:, chore:, or test:

You should delete the non existent element, whose atomic_number is 1000, from the two tables

Your properties table should not have a type column

You should finish your project while on the main branch. Your working tree should be clean 
and you should not have any uncommitted changes

------------------------------------------------------------------------------------------

In the beginning:

periodic_table=> \d
             List of relations
 Schema |    Name    | Type  |    Owner     
--------+------------+-------+--------------
 public | elements   | table | freecodecamp
 public | properties | table | freecodecamp
(2 rows)


periodic_table=> \d elements;
                        Table "public.elements"
    Column     |         Type          | Collation | Nullable | Default 
---------------+-----------------------+-----------+----------+---------
 atomic_number | integer               |           | not null | 
 symbol        | character varying(2)  |           |          | 
 name          | character varying(40) |           |          | 
Indexes:
    "elements_pkey" PRIMARY KEY, btree (atomic_number)
    "elements_atomic_number_key" UNIQUE CONSTRAINT, btree (atomic_number)


periodic_table=> \d properties
                       Table "public.properties"
    Column     |         Type          | Collation | Nullable | Default 
---------------+-----------------------+-----------+----------+---------
 atomic_number | integer               |           | not null | 
 type          | character varying(30) |           |          | 
 weight        | numeric(9,6)          |           | not null | 
 melting_point | numeric               |           |          | 
 boiling_point | numeric               |           |          | 
Indexes:
    "properties_pkey" PRIMARY KEY, btree (atomic_number)
    "properties_atomic_number_key" UNIQUE CONSTRAINT, btree (atomic_number)


periodic_table=> SELECT * FROM elements;
 atomic_number | symbol |   name    
---------------+--------+-----------
             1 | H      | Hydrogen
             2 | he     | Helium
             3 | li     | Lithium
             4 | Be     | Beryllium
             5 | B      | Boron
             6 | C      | Carbon
             7 | N      | Nitrogen
             8 | O      | Oxygen
          1000 | mT     | moTanium
(9 rows)


periodic_table=> SELECT * FROM properties;
 atomic_number |   type    |  weight   | melting_point | boiling_point 
---------------+-----------+-----------+---------------+---------------
             1 | nonmetal  |  1.008000 |        -259.1 |        -252.9
             2 | nonmetal  |  4.002600 |        -272.2 |          -269
             3 | metal     |  6.940000 |        180.54 |          1342
             4 | metal     |  9.012200 |          1287 |          2470
             5 | metalloid | 10.810000 |          2075 |          4000
             6 | nonmetal  | 12.011000 |          3550 |          4027
             7 | nonmetal  | 14.007000 |        -210.1 |        -195.8
             8 | nonmetal  | 15.999000 |          -218 |          -183
          1000 | metalloid |  1.000000 |            10 |           100
(9 rows)

------------------------------------------------------------------------------------------

Finished:

periodic_table=> \d
             List of relations
 Schema |    Name    | Type  |    Owner     
--------+------------+-------+--------------
 public | elements   | table | freecodecamp
 public | properties | table | freecodecamp
 public | types      | table | freecodecamp
(3 rows)


periodic_table=> \d elements;
                        Table "public.elements"
    Column     |         Type          | Collation | Nullable | Default 
---------------+-----------------------+-----------+----------+---------
 atomic_number | integer               |           | not null | 
 symbol        | character varying(2)  |           | not null | 
 name          | character varying(40) |           | not null | 
Indexes:
    "elements_pkey" PRIMARY KEY, btree (atomic_number)
    "elements_atomic_number_key" UNIQUE CONSTRAINT, btree (atomic_number)
    "elements_name_key" UNIQUE CONSTRAINT, btree (name)
    "elements_symbol_key" UNIQUE CONSTRAINT, btree (symbol)
Referenced by:
    TABLE "properties" CONSTRAINT "properties_atomic_number_fkey" FOREIGN KEY (atomic_number) REFERENCES elements(atomic_number)


periodic_table=> \d properties;
                    Table "public.properties"
        Column         |  Type   | Collation | Nullable | Default 
-----------------------+---------+-----------+----------+---------
 atomic_number         | integer |           | not null | 
 atomic_mass           | numeric |           | not null | 
 melting_point_celsius | numeric |           | not null | 
 boiling_point_celsius | numeric |           | not null | 
 type_id               | integer |           | not null | 1
Indexes:
    "properties_pkey" PRIMARY KEY, btree (atomic_number)
    "properties_atomic_number_key" UNIQUE CONSTRAINT, btree (atomic_number)
Foreign-key constraints:
    "properties_atomic_number_fkey" FOREIGN KEY (atomic_number) REFERENCES elements(atomic_number)
    "properties_type_id_fkey" FOREIGN KEY (type_id) REFERENCES types(type_id)


periodic_table=> \d types;
                       Table "public.types"
 Column  |         Type          | Collation | Nullable | Default 
---------+-----------------------+-----------+----------+---------
 type_id | integer               |           | not null | 
 type    | character varying(30) |           | not null | 
Indexes:
    "types_pkey" PRIMARY KEY, btree (type_id)
Referenced by:
    TABLE "properties" CONSTRAINT "properties_type_id_fkey" FOREIGN KEY (type_id) REFERENCES types(type_id)


periodic_table=> SELECT * FROM elements;
 atomic_number | symbol |   name    
---------------+--------+-----------
             1 | H      | Hydrogen
             4 | Be     | Beryllium
             5 | B      | Boron
             6 | C      | Carbon
             7 | N      | Nitrogen
             8 | O      | Oxygen
             2 | He     | Helium
             3 | Li     | Lithium
             9 | F      | Fluorine
            10 | Ne     | Neon
(10 rows)


periodic_table=> SELECT * FROM properties;
 atomic_number | atomic_mass | melting_point_celsius | boiling_point_celsius | type_id 
---------------+-------------+-----------------------+-----------------------+---------
             1 |       1.008 |                -259.1 |                -252.9 |       1
             2 |      4.0026 |                -272.2 |                  -269 |       1
             6 |      12.011 |                  3550 |                  4027 |       1
             7 |      14.007 |                -210.1 |                -195.8 |       1
             8 |      15.999 |                  -218 |                  -183 |       1
             3 |        6.94 |                180.54 |                  1342 |       2
             4 |      9.0122 |                  1287 |                  2470 |       2
             5 |       10.81 |                  2075 |                  4000 |       3
             9 |      18.998 |                  -220 |                -188.1 |       1
            10 |       20.18 |                -248.6 |                -246.1 |       1
(10 rows)


periodic_table=> SELECT * FROM types;
 type_id |   type    
---------+-----------
       1 | nonmetal
       2 | metal
       3 | metalloid
(3 rows)

------------------------------------------------------------------------------------------
