import prompt
import random


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
    i = 0
    progression_string = ''
    while i <= 9:
        progression_string = progression_string + ' ' + str(progression_list[i])
        i = i + 1
    print('Question:' + progression_string)
    answer = prompt.string('Your answer: ')
    answer_for_comp = answer
    right_ans = str(progression[random_i])
    mirror_ans = right_ans
    return(answer, right_ans, answer_for_comp, mirror_ans)
