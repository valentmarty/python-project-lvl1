import prompt


def welcome():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name)
    return(name)
def game_condition():
    print('Answer "yes" if the number is even, otherwise answer "no".')
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







