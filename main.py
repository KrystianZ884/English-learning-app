import features
from game import main_game


def main():
    print("1. Add new word/phrase")
    print("2. Display the list of words/phrases")
    print("3. Play a game")
    print("4. Close the app")
    print("5. Display history")

    choice = input("Choose an action: ")
    while int(choice) != 4:

        if int(choice) == 1:
            txt_eng = input("Provide word/phrase in English: ")
            txt_pol = input("Provide word/phrase in Polish: ")
            features.add_new(txt_eng, txt_pol)

        elif int(choice) == 2:
            features.read_word_file()

        elif int(choice) == 3:
            points, tries = main_game()
            print(f"Score is {points} / {tries}")
            features.add_new_record(points, tries)
            break

        elif int(choice) == 4:
            break

        elif int(choice) == 5:
            features.read_history_file()


if __name__ == "__main__":
    main()
