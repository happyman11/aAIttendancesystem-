import numpy as np
import cv2


def save_dataset(image,ID,Name,sampleNum):


        cv2.imwrite("dataset/ " + Name + "." + ID + '.' + str(sampleNum) + ".jpg",
                                image)