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


    def feature_extraction(path: Path, nfeatures = 5000): 
        """
        feature point is composed of two parts: key points and descriptors

        key points: refers to the 2D positions (x,y ig) of the feature point.
            some types of key points also include the orientaation and size of the imahe
         
        descriptiors: descriptors is usually vectors that carry information of the
            pixels around the key point
            (if two descriptors are close in vectore space, they can be considered the same feature.)
        
        """  
        
        orb = cv2.ORB_create(nfeatures)
        img1, img2 = input_img(path)

        kp1, des1 = orb.detectAndCompute(img1, None)
        kp2, des2 = orb.detectAndCompute(img2, None)

        bf = cv2.BFMatcher(cv2.NORM_HAMMING)
        matches = bf.match(des1, des2)

        #sorting matches by distance
        matches = sorted(matches, key = lambda x: x.distance)
        

    
    def pose_estimation():


    

    def TD_Mapping():