eVokab: an automated way to do a tedious homework assignment.

Takes in a file (vocab.txt) created by the user, gets each word's definition from Dictionary.com, and outputs the results into a file (vocab-out.txt). When multiple definitions are available, the program will ask for the user's input in deciding which definition to use in the output.

Uses this article as an initial reference:
https://realpython.com/python-web-scraping-practical-introduction/

Installation:

You will need git, python 3 and pip, which can be installed with the following commands (Debian GNU/Linux):
	sudo apt install git python3 python3-pip
	OR
	sudo apt install git python3 python3-pip -y

You will also need to install the following dependencies:
	requests
	BeautifulSoup4
You can install these dependencies by running:
	pip3 install requests BeautifulSoup4

To download this repository, simply run:
	git clone https://github.com/DrewDalmedo/evokab evokab

And you're done!

To begin using the script, you'll need to:
	1) Enter all of your vocab terms into the file 'vocab.txt'.
	2) Run the python script: python3 evokab.py
	3) Follow the instructions on screen
Your vocab is now finished! Copy the results from vocab-out.txt to a document and print out your "work" for class.
