from Questions import Questions_List
import random

print('Welcome to the Quiz Test')

score = 0
question = 0
gameOn = True


while question < 5:
    question += 1
    choose = random.randint(0, len(Questions_List)-1)
    print(f"{Questions_List[choose]['question']}?")
    answer = input('Answer: ')
    answer = answer.capitalize()

    if(answer == Questions_List[choose]['answer']):
        score += 1

print(f"""
The Test is Over. Your score is {score}/5
{(score/5) * 100}
""")
