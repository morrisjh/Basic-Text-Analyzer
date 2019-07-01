# Basic-Text-Analyzer
A basic text analyzer built with a purview to analyze historical, English-language, secondary sources.

This repository contains some resources built with a purview to analyze historical texts.

# BasicTextAnalyzer.py
This script allows the user to analyze a text in several ways.

When the script is run the user will be asked to type one of four options; 'Analyze', 'Frequency', 'Compile' or 'Search'.

The "analyze" option returns some basic statistical information about the text that is being analyzed. It will count the number of words, number of characters (with spaces), number of characters (without spaces), the approximate number of sentences, average words per sentence, and average characters per word.

The "frequency" option will check the frequency of the words in the text and return the words and their frequencies in numerical order.

The "compile" option compares the analyzed text to the 10,000 most frequently used words in Project Gutenberg (2006) (See: https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/PG/2006/04/1-10000) or another list of words chosen by the user. In order to change the list of words that the script compares the text to the user should replace the 'WordFrequency.txt' (in line 76) with a .txt file of their own choosing. The "find" option will first provide the user with the number of unknown words (those words that don't appear in WordFrequency.txt) and then provide further options. These options include the possibility to view all the unknown terms and to write them to a new file called 'UnknownWordList.txt'. The name of the new file can also be edited by the user.

The "search" option allows the user to search for individual words and check their frequency in the text.

# Religions.txt
This text file contains William Elliot Griffis's "The Religions of Japan from the Dawn of History to the Era of Meiji." This version of the text was taken from Project Gutenberg and can be found at: http://www.gutenberg.net/1/5/5/1/15516/ . The user of the program can replace this with other .txt files by replacing the term 'Religions.txt' at the beginning of the script (line 9) in 'BasicTextAnalyzer.py' with the filename of the text that they wish to analyze. 

# WordFrequency.txt
This text file contains a list of the 10,000 most frequently used words in Project Gutenberg (2006) (See: https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/PG/2006/04/1-10000). The script will compare the analyzed text to this list of words should the user choose the "find" option. This list can be replaced with a list of the user's choosing by replacing the 'WordFrequency.txt' (line 76) with a different .txt file in the script or by inserting the word list into this WordFrequency file.

# pyspellchecker and associated materials
The script imports and uses pyspellchecker (created by Tyler Barrus) which is avaliable under MIT License. For details on this, see: https://pypi.org/project/pyspellchecker/#description or refer to https://github.com/barrust/pyspellchecker. Users should install pyspellchekcer using "pip install pyspellchecker". 
