import string
import random

characters = list(string.ascii_uppercase + string.digits + "!@#$%^&*(-+)")

#MINE
def generatePassword():
    random.shuffle(characters)
    length = int(input("How long do you want your password to be?: "))
    password = ''
    i = 0
    while i<length:
        password += f"{characters[random.randint(0,len(characters)-1)]}"
        i += 1
    print(password)


def generatePassword2():
    length = int(input("How long do you want your password to be?: "))
    random.shuffle(characters)
    password = []

    for x in range(length):
        password.append(random.choice(characters))
    
    random.shuffle(password)
    password = ''.join(password)
    print(password)

generatePassword2()