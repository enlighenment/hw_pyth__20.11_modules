from random import randint as rnd
from colorama import Fore
import os



def guess_the_number():
    secret_numb = rnd(1, 100)
    attempts = 0
    os.system('cls')
    strnumb = ""

    print(f"for test >>'{secret_numb}'\n")
    print("1 - 100\n")

    
    while True: 
        user_numb = int(input("Ваше число: "))
        attempts += 1

        if user_numb.is_integer() == True:
            if user_numb > secret_numb:
                print(Fore.RED + "Слишком много!  <" + Fore.RESET + "\n")
            elif user_numb < secret_numb:
                print(Fore.BLUE + "Слишком мало!   >" + Fore.RESET + "\n")
            else:
                strnumb == secret_numb
                if strnumb[::-1] == 1 or "1":
                    print(Fore.GREEN + f"Поздравляю! число {secret_numb} угаданно за {attempts} попытку" + Fore.RESET + "\n\n")
                    break
                elif strnumb[::-1] == 2 or 3 or 4 or "2" or "3" or "4":
                    print(Fore.GREEN + f"Поздравляю! число {secret_numb} угаданно за {attempts} попытки" + Fore.RESET + "\n\n")
                    break
                elif strnumb[::-1] == 5 or 6 or 7 or 8 or 9 or 0 or "5" or "6" or "7" or "8" or "9" or "0":
                    print(Fore.GREEN + f"Поздравляю! число {secret_numb} угаданно за {attempts} попыток" + Fore.RESET + "\n\n")
                    break
                
        else:
            print("Целое число от 1 - 100")


