#!/bin/bash

cd ..
# Goes to main directory CS1XA3/

# Asks for user input on what they want to do.
echo -n "What do you want to do? (File Count, To Do, Compile Error)"
read action
echo -n "You want to ${action}!"

if [ "$action" == "File Count" ]; then
	# File Count lists all files then uses find feature to search for file extensions and pipes
	# them into the word count by line function
	count_html=$(ls -Rl | find . -name  '*.html' | wc -l)
	count_js=$(ls -Rl | find . -name  '*.js' | wc -l)
	count_css=$(ls -Rl | find . -name '*.css' | wc -l)
	count_ps=$(ls -Rl | find . -name '*.py' | wc -l)
	count_hs=$(ls -Rl | find . -name '*.hs' | wc -l)
	count_sh=$(ls -Rl | find . -name '*.sh' | wc -l)
	# Output Results
	echo "Html: $count_html"
	echo "Javascript $count_js"
	echo "CSS $count_css"
	echo "Python $count_py"
	echo "Haskell $count_hs"
	echo "Bash Script: $count_sh"

elif [ "$action" == "To Do" ]; then
	# TODO searched text in files with grep and exluded the todo.log file and redirected into todo.log
	grep -r --exclude="todo.log" "#TODO" * > todo.log
	echo "Each line of every file in the current repo with the tag #TODO has been loged in todo.log"

elif [ "$action" == "Compile Error" ]; then
	# Compiler Error (Haskel first then python files are found and ran using find and redirected
	# into compile_fail.log if they cannot be run)
	# The ghc is ghc is mentioning the compiliation system for haskel and -fno-code is suppressing
	# error message.
	echo "Errors have been logged"
	find . -name '*.hs' -exec ghc -fno-code {} \; &> compile_fail.log

	find . -name "*.py" -exec python '{}' \; &> compile_fail.log

else
	echo -n "Invalid Entry"
	# If the users imputs and invalid entry the program will inform them and proceed to exit
fi

exit
#Exits the script
