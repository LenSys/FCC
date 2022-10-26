================================================
Kitty script commands (Pipe / Input / Output)
================================================

# Build a Kitty Ipsum Translator
# In this 140-lesson course, you will learn some more complex commands, 
# and the details of how commands work.

echo hello bash
echo hello bash > stdout.txt
echo hello bash >> stdout.txt
echo hello bash > stdout.txt
> stdout.txt 

bad_command
bad_command > stderr.txt
bad_command 2> stderr.txt
echo hello bash 1> stdout.txt

read NAME
echo $NAME
echo $NAME 1> stdout.txt 
echo freeCodeCamp 1> name.txt
read NAME < name.txt 
echo $NAME
echo a | read NAME
echo $NAME

cat
cat name.txt 
cat name.txt | name.txt
cat name.txt > name.txt
cat name.txt < name.txt
cat < name.txt
echo a | cat

touch script.sh
chmod +x script.sh 
./script.sh 
echo andy | ./script.sh 
echo andy | ./script.sh 2> stderr.txt
echo andy | ./script.sh 2> stderr.txt > stdout.txt 

./script.sh < name.txt 
./script.sh < name.txt 2> stderr.txt 
./script.sh < name.txt 2> stderr.txt > stdout.txt 
cat kitty_ipsum_1.txt 
cat kitty_ipsum_2.txt 

wc kitty_ipsum_1.txt 
man wc
wc -l kitty_ipsum_1.txt 
wc -w kitty_ipsum_1.txt 
wc -m kitty_ipsum_1.txt 
wc kitty_ipsum_1.txt 

cat kitty_ipsum_1.txt | wc
wc < kitty_ipsum_1.txt 

echo "~~ kitty_ipsum_1.txt info ~~" > kitty_info.txt
echo -e "\nNumber of lines:" >> kitty_info.txt 
cat kitty_ipsum_1.txt | wc -l >> kitty_info.txt 
echo -e "\nNumber of words:" >> kitty_info.txt
cat kitty_ipsum_1.txt | wc -w >> kitty_info.txt 
echo -e "\nNumber of characters:" >> kitty_info.txt
wc -m < kitty_ipsum_1.txt >> kitty_info.txt

grep meow kitty_ipsum_1.txt 
grep meow kitty_ipsum_1.txt --color
grep meow kitty_ipsum_1.txt --color --line-number

# regular expression with grep
grep meow[a-z]* kitty_ipsum_1.txt --color --line-number

echo -e "\nNumber of times meow or meowzer appears:" >> kitty_info.txt

# count number of lines of pattern in kitty_ipsum_1.txt file
grep meow[a-z]* kitty_ipsum_1.txt -c

# -o puts matches on their own lines, use with "wc" to count word lines (= occurrences of word meow or meowzer)
grep meow[a-z]* kitty_ipsum_1.txt -o
grep meow[a-z]* kitty_ipsum_1.txt -o | wc -l
grep meow[a-z]* kitty_ipsum_1.txt -o | wc -l >> kitty_info.txt

echo -e "\nLines that they appear on:" >> kitty_info.txt 
grep meow[a-z]* kitty_ipsum_1.txt -n


# search and replace text 'r' with '2' in content of file name.txt
sed 's/r/2/' name.txt
sed 's/free/f233/' name.txt
sed 's/freecodecamp/f233C0d3C@mp/' name.txt

# search and replace case-insensitive
sed 's/freecodecamp/f233C0d3C@mp/i' name.txt

sed 's/freecodecamp/f233C0d3C@mp/i' < name.txt
cat name.txt | sed 's/freecodecamp/f233C0d3C@mp/i'

# search for meow and output line numbers of occurrence
grep meow[a-z]* kitty_ipsum_1.txt -n

# search for meow and output line numbers of occurrence, then replace line number with 1
grep meow[a-z]* kitty_ipsum_1.txt -n | sed 's/[0-9]/1/'

# search for meow and output line numbers of occurrence, then replace line number with 1
# -E --> use extended regular expressions
grep meow[a-z]* kitty_ipsum_1.txt -n | sed 's/[0-9]+/1/' -E

# search for meow and output line numbers of occurrence, replace with only line number
# (this removes the text after the line number!)
grep meow[a-z]* kitty_ipsum_1.txt -n | sed 's/([0-9]+).*/\1/' -E

# search for meow and output line numbers of occurrence, replace with only line number
# output the line numbers to the end of the file kitty_info.txt 
grep meow[a-z]* kitty_ipsum_1.txt -n | sed 's/([0-9]+).*/\1/' -E >> kitty_info.txt 

# use grep with the --color flag to see all the words that start with cat
grep cat[a-z]* kitty_ipsum_1.txt --color

# use grep with the correct flag to put all the matches of the cat[a-z]* pattern on their own line
grep cat[a-z]* kitty_ipsum_1.txt -o

# pipe the output into the command that outputs the count of lines
grep cat[a-z]* kitty_ipsum_1.txt -o | wc -l

# enter the same command and append the count to the kitty_info.txt file
grep cat[a-z]* kitty_ipsum_1.txt -o | wc -l >> kitty_info.txt

# use echo to add the text Lines that they appear on: to the kitty_info.txt file again
# place a new line in front of the text like before
echo -e "\nLines that they appear on:" >> kitty_info.txt

# The process to add the lines to the file will be the same as you did before
# Start by using grep to match the cat words in the file and showing 
# the line numbers with the output
grep cat[a-z]* kitty_ipsum_1.txt -n

# use sed again to extract only the line numbers 
# Pipe the output of the last command into sed to do that 
# As a reminder, the sed pattern was 's/([0-9]+).*/\1/'
# -E --> use extended regular expressions
grep cat[a-z]* kitty_ipsum_1.txt -n | sed 's/([0-9]+).*/\1/' -E

# append the line numbers to the kitty_info.txt file
grep cat[a-z]* kitty_ipsum_1.txt -n | sed 's/([0-9]+).*/\1/' -E >> kitty_info.txt


# -------------------------------------------------------------------------------------------------------

# do the same thing for the kitty_ipsum_2.txt file
# Using echo in the terminal, append ~~ kitty_ipsum_2.txt info ~~ to the kitty_info.txt file. 
# Put two new lines in front of the text this time.
echo -e "\n\n~~ kitty_ipsum_2.txt info ~~" >> kitty_info.txt

# First piece of info is the number of lines in the file.
# Use the terminal to append "Number of lines:" to the file with a new line in front.
echo -e "\nNumber of lines:" >> kitty_info.txt

# Use cat with the pipe method to append the info to the kitty_info.txt file that it is asking for.
cat kitty_ipsum_2.txt | wc -l >> kitty_info.txt

# Next, use the terminal to append Number of words: to the kitty_info.txt file.
# Put a new line in front of the text again.
echo -e "\nNumber of words:" >> kitty_info.txt 

# Append the suggested info the kitty_info.txt file. 
# Use redirection instead of the pipe method for the input this time.
wc -w < kitty_ipsum_2.txt >> kitty_info.txt

# Next, is the character count. 
# Append Number of characters: to the file with a new line in front of the text. 
# Use the method you have been using.
echo -e "\nNumber of characters:" >> kitty_info.txt 

# Using the pipe or input redirection method, 
# append the character count of kitty_ipsum_2.txt to the kitty_info.txt file
cat kitty_ipsum_2.txt | wc -m >> kitty_info.txt

# Next, use grep to see how many variations of meow there are in kitty_ipsum_2.txt. 
# Use the same pattern you used before and add the flag to show colors so it's easier to see.
grep meow[a-z]* kitty_ipsum_2.txt --color

# Append "Number of times meow or meowzer appears:" to the kitty_info.txt file 
# with a new line in front of it like before.
echo -e "\nNumber of times meow or meowzer appears:" >> kitty_info.txt

# Use grep and wc in the terminal to append the suggested number to the kitty_info.txt file.
grep meow[a-z]* kitty_ipsum_2.txt -o | wc -l >> kitty_info.txt

# Next, use the terminal to append "Lines that they appear on:" to 
# the kitty_info.txt file with a new line in front of the text.
echo -e "\nLines that they appear on:" >> kitty_info.txt

# Use grep and sed in the terminal to append the suggested line numbers 
# to the kitty_info.txt file.
grep meow[a-z]* kitty_ipsum_2.txt -n | sed 's/([0-9]+).*/\1/' -E >> kitty_info.txt

# Use grep to see how many variations of cat there are in kitty_ipsum_2.txt. 
# Use the same pattern you used before and include the flag to show colors so it's easier to see.
grep cat[a-z]* kitty_ipsum_2.txt --color

# Append Number of times cat, cats, or catnip appears: to the kitty_info.txt file. 
# Use the method you have been using.
echo -e "\nNumber of times cat, cats, or catnip appears:" >> kitty_info.txt

# Use grep and wc in the terminal to append the suggested info to kitty_info.txt
grep cat[a-z]* kitty_ipsum_2.txt -o | wc -l >> kitty_info.txt

# Append "Lines that they appear on:" to it like you did for the others.
echo -e "\nLines that they appear on:" >> kitty_info.txt

# Use grep and sed in the terminal to append the suggested numbers to the kitty_info.txt file.
grep cat[a-z]* kitty_ipsum_2.txt -n | sed -E 's/([0-9]+).*/\1/' >> kitty_info.txt

# -------------------------------------------------------------------------------------------------------

# Next, create a small script to translate both them into doggy ipsum. 
# It will be as simple as replacing all the cat references with similar words for dogs. 
# In the terminal, use touch to create translate.sh
touch translate.sh

# Give your new script executable permissions so you can run it in the terminal.
chmod +x translate.sh

# Add a shebang to the script that uses bash like you did for the other script you made.
# (add to file translate.sh:)
#!/bin/bash

# The script will take a file as input that can be passed as an argument or read from stdin. 
# Below the shebang, use cat to print the content of the first argument passed to the script.
# (add to file translate.sh:)
cat $1

# Run the script and use the first kitty ipsum file as an argument to see if it's working.
./translate.sh kitty_ipsum_1.txt

# Try the same command using redirection to print the file.
./translate.sh < kitty_ipsum_1.txt

# Try the cat and pipe method.
cat kitty_ipsum_1.txt | ./translate.sh

# In your script file, pipe the input into a sed that replaces catnip with dogchow.
# (add to file translate.sh:)
cat $1 | sed 's/catnip/dogchow/'

# Run the script passing the first kitty ipsum file as a argument to see if it's working.
./translate.sh kitty_ipsum_1.txt

# If you look, you can find dogchow in there so it's probably working. 
# To make sure pipe the results of that into a grep command that searches for dogchow. 
# Output the results in color.
./translate.sh kitty_ipsum_1.txt | grep dogchow --color

# It's showing three places catnip was replaced with dogchow. 
# To make sure you got them all, enter the previous command and search for catnip instead.
./translate.sh kitty_ipsum_1.txt | grep catnip --color

# It didn't output anything, so it must be replacing all the instances of catnip. 
# You can replace many patterns using sed like this: 
# sed 's/<pattern_1>/<replacement_1>/; s/<pattern_2>/<replacement_2>/'. 
# Note that you need the semi-colon between the two replacement patterns and 
# they both need to be wrapped in the quotes. 
# In your script, add another pattern to the sed command that replaces cat with dog.
# (modify in file translate.sh:)
cat $1 | sed 's/catnip/dogchow/; s/cat/dog/'

# Now, it should replace catnip with dogchow and cat with dog. 
# Use the script the translate the first ipsum file again. 
# Search the results with grep for any words that start with dog. 
# Part of that search pattern should be [a-z]*. Make sure to show the results in color.
./translate.sh kitty_ipsum_1.txt | grep dog[a-z]* --color

# As expected, it replaced instances of cat with dog. 
# Enter the same command, but search for anything starting with cat to make sure 
# it replaced them all.
./translate.sh kitty_ipsum_1.txt | grep cat[a-z]* --color

# It didn't find any so it must be replacing them all. 
# You added two patterns as part of the sed in your script. 
# Add a third that replaces all meow words with woof.
# (modify in file translate.sh:)
cat $1 | sed 's/catnip/dogchow/; s/cat/dog/; s/meow/woof/'

# Using your script, translate the first ipsum file again. 
# Check the results with grep for words that start with dog or woof. 
# Here's an example of the search pattern you want: grep '<dog_words>|<woof_words>'. 
# To view "dog words", you would use dog[a-z]*. Be sure to view the result in color.
./translate.sh kitty_ipsum_1.txt | grep 'dog[a-z]*|woof[a-z]*' --color

# That didn't work. Enter the same command, but add the flag to use 
# extended regular expressions to the grep search so it recognizes the "|"
./translate.sh kitty_ipsum_1.txt | grep 'dog[a-z]*|woof[a-z]*' -E --color

# If you look closely, you can see that the meow part of meowzer on that one line 
# didn't get replaced with woof. grep only matched the first instance of meow it 
# found on that line. Add the "global" regex flag to all three patterns of the sed 
# command in your script so it will replace all instances of any of the words.
# (modify in file translate.sh:)
cat $1 | sed 's/catnip/dogchow/g; s/cat/dog/g; s/meow/woof/g'


# Enter the same command to translate the first ipsum file and see the matches 
# of all words starting with dog or woof to see if that worked.
./translate.sh kitty_ipsum_1.txt | grep 'dog[a-z]*|woof[a-z]*' -E --color

# It worked, but woofzer doesn't sound quite right. 
# Change your sed pattern that matched meow to match meow|meowzer. 
# Add the flag to use extended regular expressions to the sed command so it recognizes the |.
# (modify in file translate.sh:)
cat $1 | sed -E 's/catnip/dogchow/g; s/cat/dog/g; s/meow|meowzer/woof/g'

# Now it should replace either of those two words with woof. 
# Check it again with that command you entered before that searches for dog or woof words.
./translate.sh kitty_ipsum_1.txt | grep 'dog[a-z]*|woof[a-z]*' -E --color

# It replaced meowzer that time.
# To be sure it replaced all the words in the file, enter the same command 
# but check for meow or cat words in the same way.
./translate.sh kitty_ipsum_1.txt | grep 'meow[a-z]*|cat[a-z]*' -E --color

# No results means it didn't find any matches for cat or meow words after being translated. 
# Check the second kitty ipsum file for the same pattern to make sure it's replacing 
# all those words.
./translate.sh kitty_ipsum_2.txt | grep 'meow[a-z]*|cat[a-z]*' -E --color

# Okay, your script is finished. Translate the kitty_ipsum_1.txt file and put the output 
# into a new doggy_ipsum_1.txt file.
./translate.sh kitty_ipsum_1.txt > doggy_ipsum_1.txt

# Use cat to print the new file to the terminal.
cat doggy_ipsum_1.txt

# diff is a command to view the difference between two files. 
# You can use it like this: diff <file_1> <file_2>. 
# Use it to view the difference between the kitty_ipsum_1 and doggy_ipsum_1 files.
diff kitty_ipsum_1.txt doggy_ipsum_1.txt

# It may look a little cryptic, but it's showing the lines that don't match in the two files. 
# Check the manual of diff to see if there's any way to make it prettier.
man diff

# Use the flag to show the diff of the same two files in color.
diff kitty_ipsum_1.txt doggy_ipsum_1.txt --color

# That's better. The red lines are lines that aren't in the second file, and the green lines 
# are what they were replaced with. The line numbers that were changed are above 
# each section. 
# Translate your second kitty ipsum file and redirect the output into doggy_ipsum_2.txt.
./translate.sh kitty_ipsum_2.txt > doggy_ipsum_2.txt

# View the content of your new file with cat.
cat doggy_ipsum_2.txt

# Lastly, view the diff of the two files in color again.
diff kitty_ipsum_2.txt doggy_ipsum_2.txt --color
