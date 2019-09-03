#https://github.com/UpGado/pytorch-yolo-v3/blob/master/detect.py

import torch


def grabScreen():
    #greb my right monitor
    snapshot = ImageGrab.grab(bbox=(0, 30, 960, 1040))
    save_path = 'c:\\temp\\currScreen.png'
    #save_path = "currScreen.jpg"
    snapshot.save(save_path)
#------------------------------------------------------------------------


#------------------------------------------------------------------------


def main():
    grabScreen()
