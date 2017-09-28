import time
import random
import pyautogui

#wait to open minecraft
for i in range(0, 5):
    print (i+1)
    #print (random.randint(0, 10000))
    time.sleep(1)

for i in range(0, 600):
    pyautogui.keyDown('w')
    #pyautogui.keyDown('space')
    pyautogui.mouseDown(button='left')

    pyautogui.moveTo(random.randint(0, 1920), random.randint(340, 740))

    curPass = str(i+1)
    min = str( round( ((i+1)*3)/60 , 1) )
    por = str( round( (((i+1))/600)*100 , 1) )
    print ( 'pass: ' + curPass + '  min: ' + min + '  %: ' + por )
    
    time.sleep(3)