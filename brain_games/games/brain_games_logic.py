import prompt


ROUNDS_MAX_NUMBER = 3


def welcome():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name)
    return(name)


def answer_check(answer, right_ans, answer_for_comp, mirror_ans, i):
    if right_ans == answer_for_comp:
        print('Correct!')
        i = i + 1
    else:
        print_text = "' is wrong answer ;(. Correct answer was '"
        print("'" + answer + print_text + mirror_ans + "'.")
        i = 404
    return(i)


def rounds_check(i, name):
    if i == 3:
        print('Congratulations, ' + name + '!')
    else:
        print("Let's try again, " + name + '!')
