import prompt
import random


def game_condition():
    print('What is the result of the expression?')


def game_body():
    random_number_1 = random.randint(1, 100)
    random_number_2 = random.randint(1, 100)
    operations = ['*', '+', '-']
    random_operation = random.choice(operations)
    print('Question: ', random_number_1, random_operation, random_number_2)
    answer = prompt.string('Your answer: ')
    answer_for_comp = answer
    if random_operation == '+':
        right_ans = str(random_number_1 + random_number_2)
    elif random_operation == '-':
        right_ans = str(random_number_1 - random_number_2)
    else:
        right_ans = str(random_number_1 * random_number_2)
    mirror_ans = right_ans
    return(answer, right_ans, answer_for_comp, mirror_ans)
