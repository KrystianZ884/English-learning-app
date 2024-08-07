import features
import random

def main_game():
    points = 0
    tries = 0
    enable = 1

    print("1. English only")
    print("2. Polish only")
    print("3. Both")

    selection = input("Choose mode: ")

    while enable == 1:
        eng_txt, pol_txt = features.word_spliter()
        random_int = random.randint(0, 1)

        if int(selection) == 1:
            random_int = 1
            if random_int == 1:
                shot = input(f"{pol_txt}: ")
                if shot.lower() == eng_txt.lower():
                    print("Correct")
                    points += 1
                    tries += 1
                else:
                    print(f"Error: {eng_txt}")
                    tries += 1

                continue_choice = input("Would you like to continue?: [Y]/[N] ")
                if continue_choice.strip().lower() == "n":
                    enable = 0

        elif int(selection) == 2:
            random_int = 0
            if random_int == 0:
                shot = input(f"{eng_txt}: ")
                if shot.lower() == pol_txt.lower():
                    print("Correct")
                    points += 1
                    tries += 1
                else:
                    print(f"Error: {pol_txt}")
                    tries += 1

                continue_choice = input("Would you like to continue?: [Y]/[N] ")
                if continue_choice.strip().lower() == "n":
                    enable = 0

        elif int(selection) == 3:

            if random_int == 0:
                shot = input(f"{eng_txt}: ")
                if shot.lower() == pol_txt.lower():
                    print("Correct")
                    points += 1
                    tries += 1
                else:
                    print(f"Error: {pol_txt}")
                    tries += 1

            if random_int == 1:
                shot = input(f"{pol_txt}: ")
                if shot.lower() == eng_txt.lower():
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