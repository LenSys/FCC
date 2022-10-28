#!/bin/bash
PSQL="psql -X --username=freecodecamp --dbname=periodic_table --tuples-only -c"

if [[ -z $1 ]]
then
  echo "Please provide an element as an argument."
else
  # check if parameter is numeric
  if [[ $1 =~ ^[0-9]+$ ]]
  then
    ELEMENT_ID=$1
  else
    # check if parameter is symbol

    # get element id from symbol
    ELEMENT_ID=$($PSQL "SELECT atomic_number FROM elements WHERE symbol = '$1'")

    # check if empty element id
    if [[ -z $ELEMENT_ID ]]
    then
      # check if parameter is name

      # get element id from name
      ELEMENT_ID=$($PSQL "SELECT atomic_number FROM elements WHERE name = '$1'")
    fi
  fi

  # trim element id
  ELEMENT_ID=$(echo $ELEMENT_ID | sed -E 's/^ *| *$//g')

  # if element id is empty
  if [[ -z $ELEMENT_ID ]]
  then
    echo "I could not find that element in the database."
  else
    # get element info
    ELEMENT_INFO_RESULT=$($PSQL "SELECT symbol, name, atomic_mass, melting_point_celsius, boiling_point_celsius, type FROM elements INNER JOIN properties USING(atomic_number) INNER JOIN types USING (type_id) WHERE elements.atomic_number = $ELEMENT_ID")

    # print element info in formatted way
    echo $ELEMENT_INFO_RESULT | if read ELEMENT_SYMBOL BAR ELEMENT_NAME BAR ELEMENT_ATOMIC_MASS BAR ELEMENT_MELTING_POINT BAR ELEMENT_BOILING_POINT BAR ELEMENT_TYPE
    then
      echo "The element with atomic number $ELEMENT_ID is $ELEMENT_NAME ($ELEMENT_SYMBOL). It's a $ELEMENT_TYPE, with a mass of $ELEMENT_ATOMIC_MASS amu. $ELEMENT_NAME has a melting point of $ELEMENT_MELTING_POINT celsius and a boiling point of $ELEMENT_BOILING_POINT celsius."
    fi
  fi
fi
