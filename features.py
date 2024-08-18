import datetime
import random
import rework

# \/ \/  \/ Main Menu features \/   \/  \/


def add_new(txt_eng, txt_pol):
    entry = txt_eng + ":" + txt_pol
    file = open("words.txt", "a")
    file.write(entry)
    file.write("\r")
    file.close()


def read_word_file():
    file = open("words.txt", "r")
    print(file.read())


def read_history_file():
    file = open("history.txt", "r")
    print(file.read())


# \/ \/  \/ Game Features \/   \/  \/

def randomizer():
    with open("words.txt", "r") as file:
        read_file = file.readlines()
        random_number = random.randint(0, len(read_file) - 1)
        select_word = read_file[random_number]
        return select_word


def word_spliter():
    eng_pol_text = randomizer()
    eng_txt = eng_pol_text[:eng_pol_text.find(":")]
    pol_txt = eng_pol_text[eng_pol_text.find(":") + 1:]
    return eng_txt, pol_txt[:pol_txt.find("\n")]


def add_new_record(points, tries):
    date = str(datetime.datetime.today())
    entry = str(date[:date.find(".")]) + ": " + str(points) + " / " + str(tries)
    file = open("history.txt", "a")
    file.write(entry)
    file.write("\r")
    file.close()


def ask_to_leave_decor(func):
    def wrapper(*args, **kwargs):
        func(*args, *kwargs)
        ask_to_leave = input("Would you like to continue?: [N] ")
        if ask_to_leave.lower().strip() == "n":
            print(f"Your score is {rework.points}/{rework.tries}")
            add_new_record(rework.points, rework.tries)
            return rework.main_game(0)
    return wrapper


@ask_to_leave_decor
def game_mode_eng(eng_txt, pol_txt):
    guess = input(f"{pol_txt}: ")
    if guess.lower() == eng_txt.lower():
        print("Correct")
        rework.points += 1
        rework.tries += 1
    else:
        print(f"Error: {eng_txt}")
        rework.tries += 1
