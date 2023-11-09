from re import L
import cv2
from cv2 import imshow
import numpy as np 
#imshow('wadad',img)
#print(img)
def im2double(im):                                          #定義im2double
    minval =np.min(im.ravel())                              #將影像打成一維陣列並取最小值          
    maxval =np.max(im.ravel())                              #將影像打成一維陣列並取最大值
    double = (im.astype("float")-minval)/(maxval-minval)    #將影像傳成float形式，同時與minval與maxval做計算
    return double                                           #輸出double

def imgshow(img):                                           #展示圖片
    cv2.imshow("img",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def sobel(img,th):                                          #定義sobel濾鏡
    c = np.zeros(img.shape)                                 #生成與img同樣大小的零矩陣
    rows = np.size(img,0)                                   #設定行數目
    col = np.size(img,1)                                    #設定列數目
    sobely = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])         #設定sobel矩陣
    #print(sobely.shape)        
    for i in range(0,rows-3):                               #雙重迴圈讀取以xy為中心的3*3矩陣
        for j in range(0,col-3):
            a = img[i:i+3,j:j+3]            
            f = sum(sum(sobely * a))                        #乘上sobel濾鏡後將數值總和存入F
            c[i, j] = f                                     #將F值導入C

    for x in range(0,rows):                                 #雙重迴圈
        for y in range(0,col):  
            if  c[x,y] <th:                                 #如果小於閥值
                c[x,y] = 0                                  #設定灰階值為0
    return c

img = cv2.imread('ntust_gray.jpg',0)                        #讀取圖片
dimg = im2double(img)                                       #呼叫函式
out =sobel(dimg,0.0012)                                     #呼叫sobel函式
#absout = abs(out)
#normal = cv2.threshold
imgshow(out)                                                #顯示圖片
#print(out)                                                  

cv2.imwrite('sobel.jpg',out*255)                            #儲存
       



        

