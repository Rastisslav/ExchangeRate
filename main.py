import sys
from modules.api import Api
from datetime import datetime, timedelta


def checkExchange(command, year, month, day):
    left, right = command.split()
    api, boolean = Api(left.upper(), right.upper(), year, month, day)
    
    return api, boolean, left, right


def getDate():
    now = datetime.now()
    yesterday = datetime.now() - timedelta(days=1)
    return now.strftime("%G-%m-%d %H:%M:%S"), yesterday.strftime("%G"), yesterday.strftime("%m"), yesterday.strftime("%d")


def cliCommands():
    for command in sys.stdin:
        if 'quit' == command.rstrip():
            break
        elif 'history' == command.rstrip():
            print("show history")
        else:
            try:
                now, year, month, day = getDate()
                rate, higherNow, left, right = checkExchange(
                    command.rstrip(), year, month, day)
                
                print(
                    now,
                    left.upper(),
                    right.upper(),
                    rate,
                    year,
                    month,
                    day,
                    higherNow)
                
            except BaseException:
                print("Wrong input")


def main():
    cliCommands()


if __name__ == "__main__":
    main()
