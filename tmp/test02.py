# The program to testing purpose

paraphase = ""

while True:
    sentence = input("Say something: ")
    if sentence == 'quit()':
        break

    sentence = sentence.capitalize() + '. '
    paraphase = paraphase + sentence

print(paraphase)



