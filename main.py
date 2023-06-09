import sys
from modules.api import Api
from datetime import datetime, timedelta
from modules.connect_db import connect_to_db, add_to_table, quit_db, show_history


# funkcia ktora porovna exchangerate medzi dneskom a vcerajskom
def check_exchange(command, year, month, day):
    left, right = command.split()
    api, boolean = Api(left.upper(), right.upper(), year, month, day)
    return api, boolean, left, right

# funkcia vrati aktualny cas a rok,mesiac,den ktory bol vcera
def getDate():
    now = datetime.now()
    yesterday = datetime.now() - timedelta(days=1)
    return now.strftime("%G-%m-%d %H:%M"), yesterday.strftime(
        "%G"), yesterday.strftime("%m"), yesterday.strftime("%d")

# zmeni text do jednej z danych farieb
def prRed(skk): return ("\033[91m {}\033[00m" .format(skk))


def prGreen(skk): return ("\033[92m {}\033[00m" .format(skk))

# zadavanie commandov, quit = vypne
#                      history = vypise historiu
#                      zvysok posiela api  
def cli_commands():
    for command in sys.stdin:
        if 'quit' == command.rstrip():
            quit_db()
            break
        elif 'history' == command.rstrip():
            result = show_history()
            for item in result:
                if item[4]:
                    print(item[0], item[1], item[2], prGreen(item[3]))
                else:
                    print(item[0], item[1], item[2], prRed(item[3]))
        else:
            try:
                now, year, month, day = getDate()
                rate, higherNow, left, right = check_exchange(
                    command.rstrip(), year, month, day)

                if higherNow:
                    add_to_table(
                        now,
                        left.upper(),
                        right.upper(),
                        rate,
                        True)
                    print(
                        now,
                        left.upper(),
                        right.upper(),
                        prGreen(rate)
                    )
                if not higherNow:
                    add_to_table(
                        now,
                        left.upper(),
                        right.upper(),
                        rate,
                        False)
                    print(
                        now,
                        left.upper(),
                        right.upper(),
                        prRed(rate)
                    )

            except BaseException:
                print("Wrong input")


def main():
    connect_to_db()
    cli_commands()


if __name__ == "__main__":
    main()
