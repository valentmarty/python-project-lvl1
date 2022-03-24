import prompt
import random


ROUNDS_MAX_NUMBER = 3


def welcome():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name)
    return(name)


def game_condition():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def game_body():
    random_number = random.randint(1, 100)
    print('Question: ', random_number)
    i = 2 
    while i < random_number:
        if random_number % i != 0:
            right_answer = 0
            i = i + 1
        elif random_number == 2:
            right_answer = 0 
            i = random_number
        elif random_number % i == 0:
            right_answer = 1
            i = random_number
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
