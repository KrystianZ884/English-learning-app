import time
import features
from selenium import webdriver
from selenium.webdriver.common.by import By


points = 0
tries = 0
already_answered = []


def main_game(enable=1):
    print("1. English only")
    print("2. Polish only")
    print("3. Both")
    driver = webdriver.Firefox()
    time.sleep(3)
    driver.get("https://translate.google.com/?sl=en&tl=pl&op=translate")
    mode_selection = input("Choose mode: ")
    text_box = driver.find_element(By.XPATH, "//body/c-wiz[1]/div[1]/div[2]/c-wiz[1]/div[2]/c-wiz[1]/div[1]/div[2]/div[2]/div[1]/c-wiz[1]/span[1]/span[1]/div[1]/textarea[1]")

    while enable == 1:
        eng_txt, pol_txt = features.word_spliter()

        if eng_txt in already_answered:
            pass
        else:
            if int(mode_selection) == 1:
                text_box.send_keys(eng_txt)
                features.game_mode_eng(eng_txt, pol_txt)
                text_box.click()
                already_answered.append(eng_txt)
                speaker = driver.find_element(By.XPATH, "/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/div/c-wiz/div[5]/div/div[2]/div/div[2]/span/button/div[3]")
                speaker.click()
                ask_to_leave = input("Would you like to continue?: [N] ")
                if ask_to_leave.lower().strip() == "n":
                    print(f"Your score is {points}/{tries}")
                    features.add_new_record(points, tries)
                    quit()

                text_box.clear()
