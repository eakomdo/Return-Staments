# Magic 8-Ball simulator that gives random fortune responses
import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return "It is certain." 
    elif answerNumber == 2:
        return "It is decidedly so."
    elif answerNumber == 3:
        return "Yes."
    elif answerNumber == 4:
        return "Reply hazy, try again."
    elif answerNumber == 5:
        return "Ask again later."
    elif answerNumber == 6:
        return "Concentrate and ask again."
    elif answerNumber == 7:
        return "My reply is no."
    elif answerNumber == 8:
        return "Outlook not so good."
    elif answerNumber == 9:
        return "Very doubtful."
    elif answerNumber == 10:
        return "Absolutely!"
    elif answerNumber == 11:
        return "Without a doubt."
    else :
        return "Error: Invalid answer number."


r = random.randint(1, 11)    
fortune = getAnswer(r)
print(fortune)