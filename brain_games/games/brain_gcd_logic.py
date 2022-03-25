from math import gcd
import prompt
import random


def game_condition():
    print('Find the greatest common divisor of given numbers.')


def game_body():
    random_number_1 = random.randint(1, 100)
    random_number_2 = random.randint(1, 100)
    print('Question: ', random_number_1, random_number_2)
    answer = prompt.string('Your answer: ')
    answer_for_comp = answer
    right_ans = str(gcd(random_number_1, random_number_2))
    mirror_ans = right_ans
    return(answer, right_ans, answer_for_comp, mirror_ans)
