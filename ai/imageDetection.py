#https://imageai.readthedocs.io/en/latest/detection/

from imageai.Detection import ObjectDetection
import os
import cv2
import time
from PIL import ImageGrab


def grabScreen():
    #greb my right monitor
    snapshot = ImageGrab.grab(bbox=(0, 30, 960, 1040))
    #save_path = 'c:\\temp\\currScreen.png'
    save_path = "currScreen.jpg"
    snapshot.save(save_path)
#------------------------------------------------------------------------

def detectMyObjects():
    execution_path = os.getcwd()

    detector = ObjectDetection()
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath( os.path.join(execution_path , "yolo.h5"))
    detector.loadModel()
    detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , "currScreen.jpg"), output_image_path=os.path.join(execution_path , "currScreenNew.jpg"), minimum_percentage_probability=30)

    for eachObject in detections:
        print(eachObject["name"] , " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"] )
        print("--------------------------------")
#------------------------------------------------------------------------


def main():
    grabScreen()
    #detectMyObjects()

    

#pip3 install --upgrade https://storage.googleapis.com/tensorflow/windows/cpu/tensorflow-1.14.0-cp35-cp35m-win_amd64.whl
