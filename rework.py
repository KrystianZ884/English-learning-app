import features

points = 0
tries = 0


def main_game(enable=1):
    print("1. English only")
    print("2. Polish only")
    print("3. Both")

    mode_selection = input("Choose mode: ")

    while enable == 1:
        eng_txt, pol_txt = features.word_spliter()

        if int(mode_selection) == 1:
            features.game_mode_eng(eng_txt, pol_txt)
