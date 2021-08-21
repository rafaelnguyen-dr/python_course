# Declare json library to parse json file
# Declare difflib library to find closed word
import json
from difflib import get_close_matches

# Loading json file to python data format
file = open(r'G:/Workspaces/python-workspace/Python_Course/app01/data.json', 'r')
data = json.load(file)

# Request input
a_String = input('Please insert a word: ')

# Function result to return pair word and its meaning
def result(a_input):
    print(("{}: {}".format(a_input, data[a_input][0])))

# Function checking_World to check the word is in dictionary or not?
def checking_Word(a_input):
    key = get_close_matches (a_input, data.keys())
    print("Do you think the word is in: {0}".format(key))
    s = input("If it is true, please type the correct word, if not please type No: ")
    if s in key:
        result(s)
    else:
        print("Goodbye my friend!")

def checking_first(a_input):
    if a_input in data.keys():
        result(a_input)
    else:
        checking_Word(a_input)

if __name__ == '__main__':
    checking_first(a_String)
