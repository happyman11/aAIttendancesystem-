import cv2
import numpy as np
import time 
from save_dataset import *
from MESHFACE_FUNCTION import *


        
        
        
def area_calculation(shape,width):


    
    x=shape[0]
    y=shape[1]
    
    centre_x=int(x/2)
    centre_y=int(y/2)
    
    start_x=centre_x-width
    start_y=centre_y-width
    
    end_x=centre_x+width
    end_y=centre_y+width
    
    cordinated_calculated={"centre_x":centre_x,
                           "centre_y":centre_y,
                           "start_x":start_x,
                           "start_y":start_y,
                           "end_x":end_x,
                           "end_y":end_y
                           }
    
    return (cordinated_calculated)
    
def detect_Faces(frames):
    
    Path_cascade="C:/Users/Applications/Desktop/PRODUCT_ATTENDANCE/mARK_ATTANDANCE/Assets/Cascades/haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(Path_cascade)
    
    gray_image=cv2.cvtColor(frames,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray_image, 1.2,5)
    
    if (len(faces)):
        flag=1
        return(faces,flag,gray_image)
        
    else:
        flag=0
        return (faces,flag,gray_image)  


        
def capture_frames(ID,Name,sample_count):
    
    font = cv2.FONT_HERSHEY_SIMPLEX
    resize_shape=(840,640)
    width_area=130
    
    cam = cv2.VideoCapture(0)
    sample=0
    while True:
    
        ret, im =cam.read()
        
        if not ret:
            break    
        
        img_resized=cv2.resize(im, resize_shape, interpolation = cv2.INTER_AREA)
        cordinates=area_calculation(resize_shape,width_area)
        
        cv2.rectangle( img_resized, (cordinates["start_x"], cordinates["start_y"]), (cordinates["end_x"],cordinates["end_y"]), (0, 0, 0), 2)
        
        area_faces=img_resized[ cordinates["start_y"]:cordinates["end_y"],cordinates["start_x"]:cordinates["end_x"],]
        
        notification_area=(cordinates["start_x"]+5,cordinates["end_x"]+5)
        
        
        faces,flag,gray_image=detect_Faces(area_faces) 
       
        if not flag:
        
            font = cv2.FONT_HERSHEY_SIMPLEX
            msg="Face Not Detected!"
            cv2.putText(img_resized,msg, notification_area,font, 1, (0,0,255), 2)
            cv2.imshow('Attandance window',img_resized)
        
        elif (len(faces)>1):
        
            font = cv2.FONT_HERSHEY_SIMPLEX
            msg="Too Many Faces Detected"
            cv2.putText(img_resized,msg, notification_area,font, 1, (0,0,255), 2)
            cv2.imshow('Attandance window',img_resized)
            
            
        elif (len(faces)==1):    
            x,y,w,h=faces[0]
            
            save_dataset(gray_image[y:y+h,x:x+w],ID,Name,sample)
            
            
            mesh_returned_frame=draw_mesh(img_resized) 
            cv2.rectangle( mesh_returned_frame, (cordinates["start_x"], cordinates["start_y"]), (cordinates["end_x"],cordinates["end_y"]), (0, 255, 0), 2)
            msg="Saving Images"+ (str(sample))
            cv2.putText(mesh_returned_frame,msg, notification_area,font, 1, (0,255,0), 2)   
            cv2.imshow('Attandance window',mesh_returned_frame)
            sample=sample+1    
            
        if sample > int(sample_count):
            break        
        
        if cv2.waitKey(10) & 0xFF==ord('q'):
            break
    cam.release()
    cv2.destroyAllWindows()    
          
          
          