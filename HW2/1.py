import os
import numpy as np
import cv2 

def imgshow(img):                                           #展示圖片
    cv2.imshow("img",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def im2double(im):                                          #定義im2double
    minval =np.min(im.ravel())                              #將影像打成一維陣列並取最小值          
    maxval =np.max(im.ravel())                              #將影像打成一維陣列並取最大值
    double = (im.astype("float")-minval)/(maxval-minval)    #將影像傳成float形式，同時與minval與maxval做計算
    return double     

a = os.path.join('depthoffield','1bg.jpg')                  #影像位址
b = os.path.join('depthoffield','1fg.jpg')                  #影像位址
cleara = cv2.imread(a)                                      #讀取影像
clearb = cv2.imread(b)
fkame = cv2.imread(a)
bkame = cv2.imread(b)

#a = cv2.cvtColor(fkame, cv2.COLOR_BGR2GRAY)
#print('a',a.shape)
#print(fkame)
laplacian = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])     
fkame = cv2.cvtColor(fkame, cv2.COLOR_BGR2GRAY)             
fkame = abs(cv2.filter2D(fkame,-1,laplacian))               
bkame = cv2.cvtColor(bkame, cv2.COLOR_BGR2GRAY)  
cv2.imwrite("images/fkame.jpg",fkame)            
bkame = abs(cv2.filter2D(bkame,-1,laplacian))
cv2.imwrite("images/bkame.jpg",bkame)              
fkame = im2double(fkame)                        
bkame = im2double(bkame)

mask = fkame - bkame                                        #
img_blur = cv2.blur(mask,(20,20))                          

ret, out = cv2.threshold(img_blur,0, 1, cv2.THRESH_BINARY)  #
one = np.ones((fkame.shape[0],fkame.shape[1]))
output = out*(-1)+one                                       

B, G, R = cv2.split(cleara)                                
merged_imga = cv2.merge([np.array(B*out, dtype=np.uint8), np.array(G*out, dtype=np.uint8),np.array(R*out, dtype=np.uint8)])
cv2.imwrite("images/imga.jpg",merged_imga)
b, g, r = cv2.split(clearb)
merged_imgab = cv2.merge([np.array(b*output, dtype=np.uint8), np.array(g*output, dtype=np.uint8),np.array(r*output, dtype=np.uint8)])
cv2.imwrite("images/imagab.jpg",merged_imgab)
#imgshow(cleara)
#imgshow(merged_imgab+cleara)
cv2.imwrite('images/test1.jpg',merged_imga+merged_imgab)

