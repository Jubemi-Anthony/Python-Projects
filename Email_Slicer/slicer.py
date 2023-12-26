class User:
    def __init__(self, email,userName,domain,extension):
        self.email = email
        self.userName = userName
        self.domain = domain
        self.extension = extension


def slice(allEmails):
    sortedArray = []
    emailArray = allEmails.split('\n')
    emailArray.sort()
    
    for emails in emailArray:
        if emails == '':
            continue
        (userName, domain) = emails.split('@')
        (domain, extension) = domain.split('.')
        newUser = User(emails,userName,domain,extension)
        sortedArray.append(newUser)

    sortedString = ''
    for sorted in sortedArray:
        sortedString += f"""
        Email: {sorted.email}, User: {sorted.userName}, Domain: {sorted.domain}, Extension: {sorted.extension}"""

    myfile = open('sorted.txt', 'w')
    myfile.write(sortedString)
    myfile.close()
    print('OPERATION WAS SUCCESSFUL!')


oldfile = open('emails.txt', 'r')
allStrings = oldfile.read()
oldfile.close()

slice(allStrings)