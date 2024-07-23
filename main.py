import features


def main():
    print("1. Add new word/phrase")
    print("2. Display the list of words/phrases")
    print("3. Play a game (TBD)")

    choice = input("Choose an action: ")

    if int(choice) == 1:
        txt_eng = input("Provide word/phrase in English: ")
        txt_pol = input("Provide word/phrase in Polish: ")
        features.add_new(txt_eng, txt_pol)

    if int(choice) == 2:
        features.read_file()


main()
