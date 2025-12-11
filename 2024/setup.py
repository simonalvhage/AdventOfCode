import requests
from datetime import date
import os
import shutil
import helper_functions.explain
import helper_functions.code

def createfolder(today):
    print(today)
    if not os.path.exists("day" + str(today)):
        os.makedirs("day" + str(today))
        f = open("day" + str(today) + "/main.py", "a")
        shutil.copyfile("template.py", "day" + str(today) + "/main.py")
        f.close()

def download_input(today):
    uri = 'https://adventofcode.com/2024/day/'+ str(today) + '/input'
    response = requests.get(uri, cookies={
        'session': "53616c7465645f5f1b16325f8898102035d6de1e57c880d1ea3cc7382bb1047c5d21720ac824a36357e4885c9693753143f773cbc5a3850bdcf1648d5f02c3f7"})
    if not os.path.exists("day" + str(today) + "/input.txt"):
        text_file = open("day" + str(today) + "/input.txt", "w")
        text_file.write(response.text)
        text_file.close()


def main(today = 9):
    if not today:
        today = date.today().strftime("%d")
        if int(today)<10: today = today.replace("0","")
    createfolder(today)
    download_input(today)

    helper_functions.explain.main()
    helper_functions.code.main()


if __name__ == '__main__':
    main()