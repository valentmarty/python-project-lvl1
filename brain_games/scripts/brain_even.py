#!/usr/bin/env python

import prompt
import random


def main():
    print('Welcome to the BRAIn Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ', name)
    print('Answer "yes" if the number is even, otherwise answer "no".')
    random_number = random.randint(1, 100)
    i = 0
    while i <= 2:
        print('Question: ', random_number)
        answer = prompt.string('Your answer: ')

        if random_number % 2 == 1 and answer == 'no':
            print('Correct!')
            i = i + 1
            random_number = random.randint(1, 100)
        elif random_number % 2 == 0 and answer == 'yes':
            print('Correct!')
            i = i + 1
            random_number = random.randint(1, 100)
        else:
            if answer == 'yes':
                print('"yes" is wrong answer ;(. Correct answer was "no".')
                i = 4
            else:
                print('"no" is wrong answer ;(. Correct answer was "yes".')
                i = 4
    if i == 3:
        print('Congratulations, ', name, '!')
    else:
        print("Let's try again, ", name, '!')


if __name__ == '__main__':
    main()
