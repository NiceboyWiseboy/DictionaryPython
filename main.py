import json
from difflib import get_close_matches

data= json.load(open("data.json"))
def translate(word):
    word =word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys()))>0:
        yn=input("Did you mean %s instead?\nEnter Y if Yes or N if No:  " % get_close_matches(word,data.keys())[0])
        if yn=="Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn=="N":
            return "The word doesn't exist. Please check the word."
        else:
            return "Didn't understood the query."

    else:
        return "Word doesn't exist. Please check the word."

word = input("Enter Word: ")
output=translate(word)

if type(output)==list:
    for item in output:
        print(item)
else:
   print(output)
