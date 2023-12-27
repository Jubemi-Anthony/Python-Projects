myfile = open('RECIPIES.txt', 'r')
content = myfile.read(20000)
myfile.close()

content = content.split('\n')

newContent = []

for recipie in content:
    if len(recipie) < 5:
        content.remove(recipie)
    
    x = recipie.replace('Meal: ', '')
    newContent.append(x)

newContent.sort()

newR = ''
i=1
while i<len(newContent):
    newR += f"Meal: {newContent[i]}\n"
    i += 1

myfile = open('SORTED.txt', 'w')
myfile.write(newR)
myfile.close()
print('DONE')