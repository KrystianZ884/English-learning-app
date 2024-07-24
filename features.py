def add_new(txt_eng, txt_pol):
    entry = {txt_eng: txt_pol}
    try:
        file = open("words.txt", "x")
        file = open("words.txt", "a")
        file.write(f"{entry} \r")
        file.close()
    except:
        file = open("words.txt", "a")
        file.write(f"{entry} \r")
        file.close()


def read_file():
    file = open("words.txt", "r")
    print(file.read())
