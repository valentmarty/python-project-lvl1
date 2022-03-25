#!/usr/bin/env python

from brain_games.games.brain_games_logic import welcome
from brain_games.games.brain_games_logic import answer_check, rounds_check
from brain_games.games.brain_games_logic import ROUNDS_MAX_NUMBER
from brain_games.games.brain_prime_logic import game_condition
from brain_games.games.brain_prime_logic import game_body_1, game_body_2


def main():
    name = welcome()
    game_condition()
    i = 0
    while i <= (ROUNDS_MAX_NUMBER - 1):
        (answer, right_ans) = game_body_1()
        (answer_for_comp, mirror_ans) = game_body_2(answer)
        i = answer_check(answer, right_ans, answer_for_comp, mirror_ans, i)
    rounds_check(i, name)


if __name__ == '__main__':
    main()
