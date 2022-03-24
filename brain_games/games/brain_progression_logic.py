import prompt
import random


ROUNDS_MAX_NUMBER = 3


def welcome():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name)
    return(name)


def game_condition():
    print('What number is missing in the progression?')


def game_body():
    step = random.randint(1, 10)
    start = random.randint(1, 50)
    stop = start + 10 * step
    progression = range(start, stop, step)
    progression_list = list(progression)
    random_i = random.randint(0, 9)
    progression_list[random_i] = '..'
    # чисто для вывода на экран вопроса
    i = 0
    progression_string = ''
    while i <= 9:
        progression_string = progression_string + ' ' + str(progression_list[i])
        i = i + 1
    print('Question:' + progression_string)
    answer = prompt.string('Your answer: ')
    answer_for_comparing = answer
    right_answer = str(progression[random_i])
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
