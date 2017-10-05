import time
from PIL import ImageGrab


def wait():
    for i in range(0, 5):
        print (i+1)
        time.sleep(1)
#------------------------------------------------------------------------

def grabScreen():
    snapshot = ImageGrab.grab(bbox=(0, 30, 960, 1040))
    save_path = 'currScreen.png'
    snapshot.save(save_path)
#------------------------------------------------------------------------

def main():
    wait()
    grabScreen()
#------------------------------------------------------------------------

#call main
main()