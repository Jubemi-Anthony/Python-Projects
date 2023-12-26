from faker import Faker
fake = Faker()

random_emails = [fake.email() for _ in range(100)]
# random_emails = [1,2,3,4,5,6,7,8,9,10]
myfile = open('emails.txt', 'w')

allEmails = ''

for email in random_emails:
    allEmails += f"""
    {email}"""

myfile.write(allEmails)
myfile.close()