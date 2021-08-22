import json
from difflib import get_close_matches


file = open(r'G:\Workspaces\python-workspace\Python_Course\app01\data.json', 'r')
data = json.load(file)

a_String = input('Please insert a word: ').lower()

def checking(a_input):
    c_word = get_close_matches(a_input, data.keys())
    if (a_input.lower() or a_input.capitalize()) in data.keys():
        print("{}: {}".format(a_input, data[a_input][0]))
    else:
        yNq = input("Do you think the word is in: ", c_word, \
            "Chose Yes or No")
        if yNq in ["Yes", 'YES', 'yes']:
            word = input("Please insert the word: ")
            print("{}: {}".format(word, data[word][0]))
        else:
            print("Goodbye My Friend!")


if __name__ == '__main__':
    checking(a_String)