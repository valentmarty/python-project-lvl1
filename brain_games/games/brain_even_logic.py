import prompt
import random


def game_condition():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def game_body():
    random_number = random.randint(1, 100)
    print('Question:', random_number)
    right_ans = random_number % 2
    mirror_ans = right_ans
    answer = prompt.string('Your answer: ')
    if answer == 'yes':
        answer_for_comp = 0
        mirror_ans = 'no'
    elif answer == 'no':
        answer_for_comp = 1
        mirror_ans = 'yes'
    return(answer, right_ans, answer_for_comp, mirror_ans)
