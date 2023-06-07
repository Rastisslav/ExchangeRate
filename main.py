import sys
from modules.api import Api
from datetime import datetime


def checkExchange(command):
    left,right = command.split()
    return Api(left,right),left,right

def date():
    now = datetime.now()
    return now.strftime("%G-%m-%d %H:%M:%S")


def cliCommands(): 
    for command in sys.stdin:
        if 'quit' == command.rstrip():
            break
        elif 'history' == command.rstrip():
            print("show history")
        else:
            try:
                rate,left,right = checkExchange(command.rstrip())
                print(date(),left,right,rate)
            except:
                print("Wrong inmput")
    
def main():
    cliCommands()
    

if __name__ == "__main__":
    main()
