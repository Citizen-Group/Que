import menu
from BaseQueue import BaseQueue
from database import database


def main():
    queuesystem = database()
    mainQ = BaseQueue(queuesystem)
    mainscreen = menu.menu(mainQ,queuesystem)
    Status = True

    while Status:
        mainscreen.screen1()








if __name__ == "__main__": main()