# Yes - definitely

# It is decidedly so

# Without a doubt

# Reply hazy, try again

# Ask again later

# Better not tell you now

# My sources say no

# Outlook not so good

# Very doubtful


import random
name = ""
question = ""
answer = ""


question_list = ["what is your name?", "what is your favorite color?", "what is your favorite animal?", "what is your favorite food?", "what is your favorite movie?"]


answer_list = ["Yes - definitely", "It is decidedly so", "Without a doubt", "Reply hazy, try again", "Ask again later", "Better not tell you now", "My sources say no", "Outlook not so good", "Very doubtful"]

question_index = random.randint(0, (len(question_list) - 1))
answer_index = random.randint(0, (len(answer_list) - 1))

question=question_list[question_index]
answer=answer_list[answer_index]

if name:
    print(f"{name} ask: {question}")
else:
    print(f"question: {question}")
print(f"answer: {answer}")