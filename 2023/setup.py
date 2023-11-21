import requests
from datetime import date
import os

def createfolder(today):
    print(today)
    if not os.path.exists("day" + str(today)):
        os.makedirs("day" + str(today))
        f = open("day" + str(today) + "/main.py", "a")
        f.write("import requests\n\ndef readfile():\n\twith open('input.txt', 'r') as k:\n\t\tfor items in k.read().splitlines():\n\t\t\tprint(items)\n\ndef main():\n\treadfile()\n\nif __name__ == '__main__':\n\tmain()")
        f.close()

def download_input(today):
    uri = 'https://adventofcode.com/2023/day/'+ str(today) + '/input'
    response = requests.get(uri, cookies={
        'session': "53616c7465645f5fa817170a15e0c8e5ae15a5dde5fe7e60a93e0a549ab4b4b173a031eb23f34c534d3fb1c93433c93ed4c351b058be3735e7a99b2eae608451"})
    if not os.path.exists("day" + str(today) + "/input.txt"):
        text_file = open("day" + str(today) + "/input.txt", "w")
        text_file.write(response.text)
        text_file.close()


def main(today = None):
    if not today:
        today = date.today().strftime("%d")
        if int(today)<10: today = today.replace("0","")
    createfolder(today)
    download_input(today)


if __name__ == '__main__':
    main()