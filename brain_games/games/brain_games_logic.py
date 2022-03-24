import prompt
import random


ROUNDS_MAX_NUMBER = 3


def welcome():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name)
    return(name)


def game_condition():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def game_body():
    random_number = random.randint(1, 100)
    print('Question: ', random_number)
    right_answer = random_number % 2
    mirror_answer = right_answer
    answer = prompt.string('Your answer: ')
    if answer == 'yes':
        answer_for_comparing = 0
        mirror_answer = 'no'
    elif answer == 'no':
        answer_for_comparing = 1
        mirror_answer = 'yes'
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
