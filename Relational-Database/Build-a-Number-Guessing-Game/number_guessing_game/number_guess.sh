#!/bin/bash
PSQL="psql --username=freecodecamp --dbname=number_guess -t --no-align -c"

echo -e "\n~~ Number guessing game ~~\n"

echo "Enter your username:"
read USER_NAME

# check if username has been used before
USER_ID=$($PSQL "SELECT user_id FROM users WHERE username = '$USER_NAME';")

if [[ -z $USER_ID ]]
then
  # username has not been used before, add to database
  INSERT_USER_NAME_RESULT=$($PSQL "INSERT INTO users(username) VALUES('$USER_NAME');")

  # get user id
  USER_ID=$($PSQL "SELECT user_id FROM users WHERE username = '$USER_NAME';")

  # output game info
  echo "Welcome, $USER_NAME! It looks like this is your first time here."
else
  # username has been used before, get game info
  GAMES_PLAYED=$($PSQL "SELECT COUNT(guesses) FROM user_games WHERE user_id = $USER_ID GROUP BY user_id;")
  BEST_GAME=$($PSQL "SELECT MIN(guesses) FROM user_games WHERE user_id = $USER_ID GROUP BY user_id;")
  
  # output game info
  echo "Welcome back, $USER_NAME! You have played $GAMES_PLAYED games, and your best game took $BEST_GAME guesses."
fi


NUMBER_GUESS_GAME() {

  SECRET_NUMBER=$(( $RANDOM % 1000 + 1 ))
  NUMBER_OF_GUESSES=1

  echo "Guess the secret number between 1 and 1000:"
  
  # read number from user
  while read GUESS_NUMBER
  do
    # if input is not a number
    if [[ ! $GUESS_NUMBER =~ ^[0-9]+$ ]]
    then
      echo "That is not an integer, guess again:"
    else
      if [[ $GUESS_NUMBER == $SECRET_NUMBER ]]
      then
        echo "You guessed it in $NUMBER_OF_GUESSES tries. The secret number was $SECRET_NUMBER. Nice job!"

        # insert current game into database
        GAME_INSERT_RESULT=$($PSQL "INSERT INTO user_games (user_id, guesses, secret_number) VALUES($USER_ID, $NUMBER_OF_GUESSES, $SECRET_NUMBER);")

        return 0
      elif [[ $GUESS_NUMBER > $SECRET_NUMBER ]]
      then
        echo "It's lower than that, guess again:"
      elif [[ $GUESS_NUMBER < $SECRET_NUMBER ]]
      then
        echo "It's higher than that, guess again:"
      fi
    fi

    ((NUMBER_OF_GUESSES++))
  done
}

NUMBER_GUESS_GAME