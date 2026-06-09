import cv2
import numpy as np
from pathlib import Path
from inputs import input_img




class SLAM():
    def __init__(self, W, H, K):  
        """ w -> width of cam img, h -> height, k -> cam intrinsic matrix"""

        #self.mapp = Map()

        #def image_frames():
        self.W = W
        self.H = H
        self.K = K


    def feature_extraction(input_img, nfeatures = 5000): 
        """
        feature point is composed of two parts: key points and descriptors

        key points: refers to the 2D positions (x,y ig) of the feature point.
            some types of key points also include the orientaation and size of the imahe
         
        descriptiors: descriptors is usually vectors that carry information of the
            pixels around the key point
            (if two descriptors are close in vectore space, they can be considered the same feature.)
        
        """  
        
        orb = cv2.ORB_create(nfeatures)

        keypoints, descriptors = orb.detectAndCompute()

        if len(keypoints) == len(descriptors):
            for i in range(len(keypoints)):
                matches = cv2.

        

    
    def pose_estimation():


    

    def TD_Mapping():