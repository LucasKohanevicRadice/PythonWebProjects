from difflib import get_close_matches
import string

from sqlalchemy import false

def spellChecker(form_data):

    # Make the form data into lower case for comparison
    sentence = form_data.lower()

    # Save all the words from worldist.txt to here for easier comparison between form input and correct words.
    wordlist = [] 

    # Returnable dictionary that has all the necessary data needed for the return
    sentence_data = {
        "false_words" : [],
        "recommendations" : [],
        "highlighted_sentence": f"",
    } 

    # Open wordlist.txt and add the words to a list
    with open("website\wordlist.txt") as file: 

        for row in file:
            row = row.strip()
            row = row.lower()
            wordlist.append(row)
    
    words_of_sentence = sentence.split(" ") # Split the sentence into words and put into list to compare in a for loop

    # Compare sentence words with words from the wordlist
    for word in words_of_sentence: 

        if word not in wordlist:

            # Formats the returnable list item so into the dictionary so it looks a bit nicer 

            recommendations = f"{word}: "
            close_matches = get_close_matches(word, wordlist, n=5)

            for recommendation in close_matches:
                recommendations += f"{recommendation}, "

            # Add everything into the returnable dictionary
            sentence_data["false_words"].append(word) # Appends the false word into the "false_words" list inside the "sentence_data" - dictionary.
            sentence_data["recommendations"].append(recommendations[:-2]) # Compares the word variable to all the words in the wordlist, and returns n-amount of the closest matches
            sentence_data["highlighted_sentence"] += f"<span style='color:red'><i>{word}</i></span> " # Doesnt work like this


        
        else:
            sentence_data["highlighted_sentence"] += f"<i>{word}</i> "

    
    sentence_data["highlighted_sentence"].strip()

    return sentence_data


    




