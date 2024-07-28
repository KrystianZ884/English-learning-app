from features import word_spliter
import random


def main_game():
    points = 0
    tries = 0

    while tries != 0:
        eng_txt, pol_txt = word_spliter()
        random_int = random.randint(0, 1)

        if random_int == 0:
            shot = input(f"{eng_txt}: ")
            if shot == pol_txt:
                tries += 1
                points += 1
            else:
                tries += 1

        elif random_int == 1:
            shot = input(f"{pol_txt}: ")
            if shot == eng_txt:
                tries += 1
                points += 1
            else:
                tries += 1



main_game()
