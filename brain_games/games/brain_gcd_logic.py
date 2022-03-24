from math import gcd
import prompt
import random


ROUNDS_MAX_NUMBER = 3


def welcome():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name)
    return(name)


def game_condition():
    print('Find the greatest common divisor of given numbers.')


def game_body():
    random_number_1 = random.randint(1, 100)
    random_number_2 = random.randint(1, 100)
    print('Question: ', random_number_1, random_number_2)
    answer = prompt.string('Your answer: ')
    answer_for_comparing = answer
    right_answer = str(gcd(random_number_1, random_number_2))
    mirror_answer = right_answer
    return(answer, right_answer, answer_for_comparing, mirror_answer)


def answer_check(answer, right_answer, answer_for_comparing, mirror_answer, i):
    if right_answer == answer_for_comparing:
        print('Correct!')
        i = i + 1
    else:
        print("'" + answer + "' is wrong answer ;(. Correct answer was '" + mirror_answer + "'.")
        i = 404
    return(i)


def rounds_check(i, name):
    if i == 3:
        print('Congratulations, ' + name + '!')
    else:
        print("Let's try again, " + name + '!')
