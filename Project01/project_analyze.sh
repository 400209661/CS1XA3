#!/bin/bash
cd ..

# Asks for user input on what they want to do.
echo -n "What do you want to do? (File Count)"
read action
echo -n "You want to ${action}!"

if [ "$action" == "File Count" ]; then
	#File Count
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
else
	echo -n "Invalid Entry"
	exit
fi

