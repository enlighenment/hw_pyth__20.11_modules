from module_task1 import *
from module_task2 import *
from module_task3 import *
import os
os.system("cls")


user_numb = 0


while True:
    numb_task = input("1 / 2 / 3\n>>")
    while True:
        if numb_task == "1":
            guess_the_number()
            break

        elif numb_task == "2":
            time()
            break

        elif numb_task == "3":
            url = input("Введите URL сайта для проверки: ").strip()
            check_website_status(url)
            break

        else:
            print("\nuncorrect number")
            break
            

