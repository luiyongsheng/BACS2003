from random import *
import math


def mastermind(guess_param):
    CODES = set(['green', 'cyan', 'red', 'purple', 'blue', 'orange'])
    answer = []
    for i in range(0,4):
        answer.append(list(CODES)[randint(0,5)])

    for i in range(0,4):
        if(answer[i] == guess_param[i]): print "Black"
        else: print "White"

guess = []
for i in range(0,4):
    color = raw_input("Enter color %d : " %(i + 1))
    guess.append(color)

mastermind(guess)
