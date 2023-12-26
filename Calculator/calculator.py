def add(a,b):
     print(f'The answer is {a+b}')

def sub(a,b):
     print(f'The answer is {a-b}')

def mul(a,b):
     print(f'The answer is {a*b}')

def div(a,b):
     print(f'The answer is {a/b}')

intro = """
This is a Python Calculator!
Enter any of the following option for the mathematical operation you want to carry out.
A: ADDITION
B: SUBTRACTION
C: MULTIPLICATION
D: DIVISION
X: TO CANCEL
"""


running = True
print(intro)

while running:
    operation = input('Enter A, B, C, D or X:  ')

    if operation == 'X' or operation == 'x':
        running = False
        break
    
    inp1 = input('Enter First Input:  ')
    inp2 = input('Enter Second Input:  ')

    inp1 = int(inp1)
    inp2 = int(inp2)

    if operation == 'A' or operation == 'a':
        add(inp1, inp2)
    if operation == 'B' or operation == 'b':
        sub(inp1, inp2)
    if operation == 'C' or operation == 'c':
        mul(inp1, inp2)
    if operation == 'D' or operation == 'd':
        div(inp1, inp2)