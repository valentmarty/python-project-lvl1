import prompt
import random


def game_condition():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def game_body():
    random_number = random.randint(1, 100)
    print('Question: ', random_number)
    i = 2
    while i < random_number:
        if random_number % i != 0:
            right_ans = 0
            i = i + 1
        elif random_number == 2:
            right_ans = 0
            i = random_number
        elif random_number % i == 0:
            right_ans = 1
            i = random_number
    mirror_ans = right_ans
    answer = prompt.string('Your answer: ')
    if answer == 'yes':
        answer_for_comp = 0
        mirror_ans = 'no'
    elif answer == 'no':
        answer_for_comp = 1
        mirror_ans = 'yes'
    return(answer, right_ans, answer_for_comp, mirror_ans)
