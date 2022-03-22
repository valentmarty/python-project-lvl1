#!/usr/bin/env python

import prompt
import random


def main():
    # Welcome_user function
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name)
    # Game condition var
    print('Answer "yes" if the number is even, otherwise answer "no".')
    # Program
    i = 0
    while i <= 2:
        random_number = random.randint(1, 100)
        print('Question: ', random_number)
        right_answer = random_number % 2
        answer = prompt.string('Your answer: ')
        if answer == 'yes':
            answer_for_comparing = 0
            mirror_answer = 'no'
        elif answer == 'no':
            answer_for_comparing = 1
            mirror_answer = 'yes'
        # condition check
        if right_answer == answer_for_comparing:
            print('Correct!')
            i = i + 1
        else:
            print("'" + answer + "' is wrong answer ;(. Correct answer was '" + mirror_answer + "'.")
            i = 404
    # Check program
    if i == 3:
        print('Congratulations, ' + name + '!')
    else:
        print("Let's try again, " + name + '!')


if __name__ == '__main__':
    main()
