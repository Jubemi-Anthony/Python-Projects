myFile = open('test.txt', 'r+')
text = myFile.read(10000)
myFile.close()

def wordReplace(wholeString, old, new):
    return wholeString.replace(old, new)

see = text.count('astronomers')

text = wordReplace(text, 'cosmos', 'field')
text = wordReplace(text, 'the universe', 'Igarra')
text = wordReplace(text, 'we', 'Anthony')
text = wordReplace(text, 'Astronomers', 'Geologers')
text = wordReplace(text, 'astronomers', 'geologers')
text = wordReplace(text, 'cosmic', 'geologic')
text = wordReplace(text, 'planet', 'plot')
text = wordReplace(text, 'Galaxy', 'village')
text = wordReplace(text, 'galaxies', 'villages')
text = wordReplace(text, 'Galaxies', 'Villages')
text = wordReplace(text, 'Milky Way', 'Niger Delta Basin')

myfile = open('test.txt', 'w')
myfile.write(text)
myfile.close()
print(text)

newT = """

I FUCKING DID IT!!!!!!!!!!!2
"""
myfile = open('test.txt', 'a')
myfile.write(newT)
myfile.close()