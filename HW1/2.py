from re import L
import cv2
from cv2 import imshow
import numpy as np 
#imshow('wadad',img)
#print(img)
def im2double(im):                                          #定義im2double
    minval =np.min(im.ravel())                              #將輸入矩陣轉成一維取最小值
    maxval =np.max(im.ravel())                              #將輸入矩陣轉成一維取最大值
    double = (im.astype("float")-minval)/(maxval-minval)    #將影像傳成float形式，同時與minval與maxval做計算    
    return double                                           #回傳double

def imgshow(img):                                           #定義圖片顯示
    cv2.imshow("img",img)   
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def blur(img):                                              #定義blur
    a = 1/9                                                 #設定變數A=1/9
    
    bkernal =np.array([[a,a,a],[a,a,a],[a,a,a]])            #設定blur矩陣
    c = np.zeros(img.shape)                                 #生成與輸入相同size的零矩陣
    rows = np.size(img,0)                                   #設定行向量數目
    col = np.size(img,1)                                    #設定列向量數目
    
    for i in range(0,rows-3):                               #雙重迴圈
        for j in range(0,col-3):
            a = img[i:i+3,j:j+3]                            #讀取以xy為中心的3*3陣列
            f = sum(sum(bkernal * a))                       #與blur濾鏡相乘後將數值相加後存入F
            c[i, j] = f                                     #存入零矩陣
    '''''
    for x in range(0,rows):
        for y in range(0,col):
            if  c[x,y] <th:
              c[x,y] = 0
    '''''
    return c

img = cv2.imread('ntust_gray.jpg',0)                        #讀取圖片
dimg = im2double(img)                                       #呼叫im2double將影像轉成double格式
out =blur(dimg)                                             #呼叫blur    
#absout = abs(out)
#normal = cv2.threshold
imgshow(0.8*(dimg-out)+dimg)                                           #顯示圖片


cv2.imwrite('blur.jpg',out*255)                             #儲存模糊影像
cv2.imwrite('sharp.jpg',(0.8*(dimg-out)+dimg)*255)                     #儲存銳化影像    



        


