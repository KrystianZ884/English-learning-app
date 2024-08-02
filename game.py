import features
import random

def main_game():
    points = 0
    tries = 0
    enable = 1

    while enable == 1:
        eng_txt, pol_txt = features.word_spliter()
        random_int = random.randint(0, 1)

        if random_int == 0:
            shot = input(f"{eng_txt}: ")
            if shot == pol_txt:
                print("Correct")
                points += 1
                tries += 1
            else:
                print(f"Error: {pol_txt}")
                tries += 1


        if random_int == 1:
            shot = input(f"{pol_txt}: ")
            if shot == eng_txt:
                print("Correct")
                points += 1
                tries += 1
            else:
                print(f"Error: {eng_txt}")
                tries += 1

        continue_choice = input("Would you like to continue?: [Y]/[N] ")
        if continue_choice.strip().lower() == "n":
            enable = 0

    return points, tries