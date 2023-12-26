from PyDictionary import PyDictionary

dictionary = PyDictionary()

while True:
    word = input("Enter a word to get the meaning: ")
    if word == "":
        break

    print(dictionary.meaning(word))

    #print(dictionary.getmeanings('hi','one','why'))