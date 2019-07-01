#This is a simple program for conducting basic text analysis.
#The user can do four things.
# 1. Conduct a brief analysis of things such as word count.
# 2. Check the frequency of all words that appear in the anaylzed text.
# 3. Check unknown (in comparison to another list of words) and compile these these in a document.
# 4. Search if a term appears in the text and check its frequency.

#File to be analyzed (can be changed as necessary).
filename = 'Religions.txt'

#User inputs one of three options.
response = input("Type 'Analyze', 'Frequency', 'Compile' or 'Search': ")

#Basic analysis of text.
if response.casefold() == "analyze":
    try:
        with open(filename) as file_object:
            text = file_object.read()
    except FileNotFoundError:
        message = 'The file ' + filename + ' cannot be found.'
        print(message)
    else:
        print('Total words:   ', len(text.split())) #Counts total number of words.
        print('Total characters with spaces: ', len(text)) #Counts total number of characters including spaces.
        print('Total characters without spaces: ', len(text) - text.count(' ')) #Counts total number of characters without spaces.

        sentence_end = text.count('.') + text.count('!') + text.count('?') #Defines what the end of a sentence is.
        print('Approximate number of sentences:    ', sentence_end) #Counts the approximate number of sentences.

        print('Average words per sentence: ', (len(text.split())/sentence_end)) #Counts the average words per approximate number of sentences.
        print('Average characters per word: ', (len(text) - text.count(' '))/(len(text.split()))) #Estiamtes the average number of characters per word.
        print('Analysis complete.')

#A function for checking the frequency of words.
if response.casefold() == "frequency":
    try:
        with open(filename) as file_object:
            text = file_object.read()
    except FileNotFoundError:
        message = 'The file ' + filename + ' cannot be found.'
        print(message)
    else:
        for char in '-.,!?-_[]();:\n':
            text = text.replace(char,' ') #Removes punctuation and replaces it with white space.
        text = text.lower() #Makes text lowercase.

        word_list = text.split()

        d = {}
        for word in word_list: 
            d[word] = d.get(word, 0) + 1
    
        word_freq = []
        for key, value in d.items():
            word_freq.append((value, key))
        word_freq.sort(reverse=True)

    print('Words and their Frequencies: ', word_freq) #Returns a list of words in the text and their frequencies sorted by their frequency.
    print('Word frequency check complete.')

#A function to find unknown words in the text and compile them into a document if desired.
if response.casefold() == "compile":
    try:
        with open(filename) as file_object:
            text = file_object.read()
    except FileNotFoundError:
        message = 'The file ' + filename + ' cannot be found.'
        print(message)
    else:
        for char in '-.,!?-_[]();:\n':
            text = text.replace(char,' ') #Removes punctuation and replaces it with white space.
        text = text.lower() #Makes text lowercase.

        from spellchecker import SpellChecker #Imports spellchecker (make sure to instal "pyspellcheker").
        spell = SpellChecker()
        spell.word_frequency.load_text_file('./WordFrequency.txt') #Loads text file containing the 10,000 most frequently used words in Project Gutenberg (2006). See: https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/PG/2006/04/1-10000.
        unknown = spell.unknown(text.split())
        print('Approximate number of unknown terms: ', len(unknown)) #Prints approximate number of words not present in the WordFrequency.txt file.
 
        response2 = input("Would you like to view unknown terms? ('Yes' or 'No'): ")

        if response2.casefold() == "yes":
            print(unknown) #Prints the words not present in the WordFrequency.txt file.

        if response2.casefold() == "no":
            print('Program complete')

        response3 = input("Would you like to add unknown terms to a new file? ('Yes' or 'No'): ")

        if response3.casefold() == "yes":
            newlist = list(unknown)
            fullStr = ' '.join(newlist)
            f = open("UnknownWordList.txt", "x")
            f.write(fullStr) 
            print('Program complete. Unknown words have been written to UnknownWordList.txt') #Writes a new file called UnknownWordList.txt listing the words not present in the WordFrequency.txt file.

        if response3.casefold() == "no":
            print('Program complete.')

#Search for a single term (and its frequency) in the text.
if response.casefold() == "search":
    try:
        with open(filename) as file_object:
            text = file_object.read()
    except FileNotFoundError:
        message = 'The file ' + filename + ' cannot be found.'
        print(message)
    else:
        for char in '-.,!?-_[]();:\n':
            text = text.replace(char,' ') #Removes punctuation and replaces it with white space.
        text = text.lower() #Makes text lowercase.

        word_list = text.split()

        d = {}
        for word in word_list: 
            d[word] = d.get(word, 0) + 1
    
        word_freq = []
        for key, value in d.items():
            word_freq.append((value, key))
        word_freq.sort(reverse=True)
        
        search = input('Search a term: ').casefold()

        if search in d:
            word = search.title()
            print('Word found in text. Word: {}. Number of instances: {}'.format(word, d[search]))
            print('Search complete.')
        else:
            print('Word not found in text.')