#!/usr/bin/env python

import prompt
import random
from brain_games.games.brain_games_logic import welcome, game_condition, answer_check, rounds_check


def main():
    name = welcome()
    game_condition()
    i = 0
    while i <= 2:
        random_number = random.randint(1, 100)
        print('Question: ', random_number)
        right_answer = random_number % 2
        mirror_answer = right_answer
        answer = prompt.string('Your answer: ')
        if answer == 'yes':
            answer_for_comparing = 0
            mirror_answer = 'no'
        elif answer == 'no':
            answer_for_comparing = 1
            mirror_answer = 'yes'
        i = answer_check(answer, right_answer, answer_for_comparing, mirror_answer, i)
    # Check program
    rounds_check(i, name)


if __name__ == '__main__':
    main()
