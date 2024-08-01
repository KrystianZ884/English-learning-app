import random

# \/ \/  \/ Main Menu features \/   \/  \/


def add_new(txt_eng, txt_pol):
    entry = txt_eng + ":" + txt_pol
    file = open("words.txt", "a")
    file.write(entry)
    file.write("\r")
    file.close()


def read_file():
    file = open("words.txt", "r")
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
    pol_txt = eng_pol_text[eng_pol_text.find(":") + 1 :]
    return eng_txt, pol_txt[:pol_txt.find("\n")]


def add_new_record(points, tries):
    entry = str(points) + " / " + str(tries)
    file = open("history.txt", "a")
    file.write(entry)
    file.write("\r")
    file.close()

