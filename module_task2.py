import os 
from time import sleep as sp
from datetime import datetime as dtt

def time():
    while True:
        os.system("cls")
        data = dtt.now().strftime("%H:%M:%S")
        print(data)
        #print("\n1>> reset\n2>> back")
        sp(1)
 #       choise = int(input("\n\n>>"))

        # if choise == 1:
        #     pass
        # elif choise == 2:
        #     break
        
        #choise = int(input("n"))
