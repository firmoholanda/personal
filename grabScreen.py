import time
from PIL import ImageGrab


def mouseLocation():
    while True:
        print(pyautogui.position())
        time.sleep(1)
#------------------------------------------------------------------------

def wait():
    for i in range(0, 5):
        print (i+1)
        time.sleep(1)
#------------------------------------------------------------------------

def grabScreen():
    #greb my right monitor
    snapshot = ImageGrab.grab(bbox=(0, 30, 960, 1040))
    #snapshot = ImageGrab.grab(bbox=(2080, 110, 3270, 830))
    save_path = 'c:\\temp\\currScreen.png'
    snapshot.save(save_path)
#------------------------------------------------------------------------

def main():
    wait()
    grabScreen()
   #mouseLocation()
#------------------------------------------------------------------------

#call main
main()    