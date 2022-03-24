#!/usr/bin/env python

from brain_games.games.brain_gcd_logic import welcome, game_condition, game_body, answer_check, rounds_check, ROUNDS_MAX_NUMBER


def main():
    name = welcome()
    game_condition()
    i = 0
    while i <= (ROUNDS_MAX_NUMBER - 1):
        (answer, right_answer, answer_for_comparing, mirror_answer) = game_body()
        i = answer_check(answer, right_answer, answer_for_comparing, mirror_answer, i)
    # Check program
    rounds_check(i, name)


if __name__ == '__main__':
    main()
