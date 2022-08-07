import cv2
import numpy as np
from dbutility import *
from VOICE_COMMANDS import *
from datetime import date
import time

def recognise_person(frames):

    Path_model="C:/Users/Applications/Desktop/PRODUCT_ATTENDANCE/mARK_ATTANDANCE/Assets/model/trained_model2.yml"
    
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read(Path_model)
   
    Id, conf = recognizer.predict(frames)
    print(conf,"Normal")
    if conf <70:
    
        
        print(conf)
        
        today = date.today()
        my_time = time.localtime()
        result_time = time.strftime("%I:%M:%S %p", my_time)
        database_wrapper(str(Id),str(today),str(result_time))
        
        message="Attandance Marked for ID:"+str(Id)
        speak(message)
    
    return (Id,conf)