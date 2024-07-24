def count_entry():
    file = open("words.txt", "r")
    counter = len(file.readlines())
    return counter


def add_new(txt_eng, txt_pol):
    entry = {txt_eng: txt_pol}
    file = open("words.txt", "a")
    file.write(f"{count_entry() + 1}. {entry} \r")
    file.close()


def read_file():
    file = open("words.txt", "r")
    print(file.read())
