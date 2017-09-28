import time
import random
import pyautogui

#wait to open minecraft
def wait():
    for i in range(0, 5):
        print (i+1)
        time.sleep(1)

#move mouse cusor, wait and click
def pointAndClick(x, y):
    pyautogui.moveTo(x, y)
    time.sleep(0.3)
    pyautogui.click()

#start mining in minutes
def startMining(n):
    for i in range(0, n*20): #600
        pyautogui.keyDown('w')
        #pyautogui.keyDown('space')
        pyautogui.mouseDown(button='left')

        #pyautogui.moveTo(random.randint(0, 1920), random.randint(340, 740))
        pyautogui.moveTo(random.randint(0, 1920), None)

        curPass = str(i+1)
        min = str( round( ((i+1)*3)/60 , 1) )
        por = str( round( ((i+1)/(n*20))*100 , 1) )
        print ( 'pass: ' + curPass + '  min: ' + min + '  %: ' + por )
        
        time.sleep(3)

    pyautogui.keyUp('w')
    pyautogui.keyUp('space')    

#return home
def returnHome():
    time.sleep(3)
    pyautogui.typewrite('/portal', interval=0.1)
    pyautogui.press('enter')
    time.sleep(0.3)
    
    pointAndClick(586, 435)
    time.sleep(3)

    pyautogui.typewrite('/f home', interval=0.1)
    pyautogui.press('enter')

#go to mine
def gotoMine():
    pyautogui.typewrite('/portal', interval=0.1)
    pyautogui.press('enter')
    time.sleep(0.3)
    
    pointAndClick(336, 438)
    time.sleep(3)

    pyautogui.moveTo(700, 545)
    pyautogui.keyDown('w')
    pyautogui.keyDown('ctrl')
    time.sleep(3)

    pyautogui.moveTo(550, 545)
    time.sleep(15)

    #mining start position
    pyautogui.moveTo(random.randint(0, 1920), 750)
    time.sleep(3)

    pyautogui.keyUp('w')
    pyautogui.keyUp('ctrl')
    
#sell items
def sellItems():
    pyautogui.typewrite('/portal', interval=0.1)
    pyautogui.press('enter')
    time.sleep(0.3)

    pointAndClick(371, 475)
    time.sleep(3)

    pyautogui.keyDown('w')
    pyautogui.keyDown('ctrl')
    time.sleep(7)
    pyautogui.moveTo(0, 545)
    time.sleep(5)
    pyautogui.moveTo(0, 545)
    time.sleep(9)
    pyautogui.moveTo(0, 545)
    time.sleep(2)
    pyautogui.moveTo(110, 545)
    time.sleep(1)
    pyautogui.keyUp('w')
    pyautogui.keyUp('ctrl')

    pyautogui.click(button='right')
    time.sleep(0.3)

    pointAndClick(335, 367)
    pointAndClick(405, 367)
    pointAndClick(440, 367)
    pointAndClick(475, 367)
    pointAndClick(510, 367)
    pointAndClick(335, 437)
    pointAndClick(375, 437)
    pointAndClick(405, 437)

    pyautogui.press('esc')
    pyautogui.typewrite('/bal', interval=0.1)
    pyautogui.press('enter')
    time.sleep(10)

def main():
    wait()

    for i in range(0, 3):
        gotoMine()
        startMining(1)
        #returnHome()
        sellItems()

if __name__ == "__main__":
    main()