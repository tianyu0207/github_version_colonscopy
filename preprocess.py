import cv2
import os
import numpy as np
import pdb


Mask_directory = ".\\Test_data\\GroundTruth\\"
Image_directory = ".\\Test_data\\Original\\"
File_name = "disease_bounding_test.txt"


#file = open(File_name, "w")



with open(File_name, 'w') as f:
  for file in os.listdir(Mask_directory):
    file_name = Mask_directory + file
    img = cv2.imread(file_name) 
    h, w, _ = img.shape
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  
    ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)  
    _, contours, hierarchy = cv2.findContours( thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    c_max = []  
    for i in range(len(contours)):
        cnt = contours[i]
        area = cv2.contourArea(cnt)

        if (area < (h/100*w/100)):
            c_min = []
            c_min.append(cnt)
            cv2.drawContours(img, c_min, -1, (0,0,0), thickness = -1)
            continue
        
        c_max.append(cnt)
   
    img2 = img
    cv2.drawContours(img2, c_max, -1 , (255,0,255), thickness = -2)

    for j in range(len(c_max)):
        c_maxi = c_max[j]
        print(type(c_maxi))
        minx=np.amin(c_maxi[:,:,0])#[0,0]
        maxx=np.amax(c_maxi[:,:,0])#[0,1]
        miny=np.amin(c_maxi[:,:,1])#[0,0]
        maxy=np.amax(c_maxi[:,:,1])#[0,1]
        
        print(type(minx))
        print(minx+1,miny+1,maxx+1,maxy+1)
        original_name = Image_directory + file
        content = '.\' + original_name + ',' +  str(minx+1) + ',' +  str(miny+1) + ',' + str(maxx+1) + ','  + str(maxy+1) + ',' +  'disease' + '\n'
    #print("write into" + '\t' + str(i))
        f.write(content)


    
