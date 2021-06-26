import sys
import os

URL = sys.argv[1]
commands = URL.split('//')
command_tmp = commands[1]
t22 = command_tmp[len(command_tmp) - 1]
if t22 == "/":
    command_tmp2 = command_tmp[:-1]
else:
    command_tmp2 = command_tmp
command = command_tmp2.replace('%20', ' ').replace('%5C', '\\').replace('%7C', '|').replace('-/', '-')
print("     URL = " + URL)

print("     command = " + command)
a = 1
while a == 1:
    start = input("Are you sure you want to execute[Y/N]")
    if start=="Y":
        if URL=="cmd:///":
            os.system("cmd")
            exit()
        os.system("cmd /c " + command)
        exit()
    if start=="y":
        if URL=="cmd:///":
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
