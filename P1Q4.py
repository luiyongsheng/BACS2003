import random

CODES = set(['green','cyan','red','purple','blue','orange'])
correctAnswer = False
continueGame = 'yes'

def masterMind(guess):
    print "Your guess >> ", guess
    count = 0
    for i in range (len(guess)):
        if guess[i] in answer:
            if guess[i] == answer[i]:
                print "Black"
                count += 1
            else:
                print "White"
    return count

answer = random.sample(CODES, 4)

while continueGame != 'no':
    for i in range(10):
        print "Trial number: ", i + 1
        print "Choose 4 colors from gree, cyan, red, purple, blue, orange"
        colors = raw_input("Enter 4 colors separated by comma(no space) >> ")
        guess = colors.split(',')
        count = masterMind(guess)
        if count == 4:
            print "Congratulations"
            correctAnswer = True
            break
    if(correctAnswer == False):
        print "You lose! The answer is ", answer
    continueGame=raw_input('Continue?(yes/no) >> ')
    
    
