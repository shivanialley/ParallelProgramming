from threading import Thread

def doSomeJob():
    while True:
        print('X')


if "__main__" == __name__:
    tObj = Thread(target = doSomeJob)
    tObj.start();
    while True:
        print('O')
