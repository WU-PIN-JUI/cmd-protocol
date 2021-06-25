import sys
import os

URL = sys.argv[1]
commands = URL.split('/')
command_tmp = commands[2]
command = command_tmp.replace('%20', ' ')

print("     URL = " + URL)

print("     command = " + command)
a = 1
while a == 1:
    start = input("Are you sure you want to execute[Y/N]")
    if start=="Y":
        if URL=="cmd://":
            os.system("cmd")
            exit()
        os.system("cmd /c " + command)
        exit()
    if start=="y":
        if URL=="cmd://":
            os.system("cmd")
            exit()
        os.system("cmd /c " + command)
        exit()
    elif start=="N":
        exit()
    elif start=="n":
        exit()
    else:
        print("Wrong input")
        



