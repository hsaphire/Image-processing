import cv2
import numpy as np
import time
def im2double(im):                                      #定義im2double
    minval =np.min(im.ravel())                          #將輸入轉成一維陣列並取最小值
    maxval =np.max(im.ravel())                          #將輸入轉成一維陣列並取最大值
    double = (im.astype("float")-minval)/(maxval-minval)#將輸入轉成float形式並做計算    
    return double                                       #輸出double

def imgshow(img):                                       #定義圖片顯示輸出方式
    cv2.imshow("img",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def saltpepper (img,prob):                              #定義胡椒鹽(輸入,閥值)
    time_s = time.time()                                
    output = np.zeros(img.shape)                        #生成與輸入圖片相同維度的零矩陣
    the = 1- prob                                       #設定閥值
    for i in range(0,img.shape[1]):                     #雙重迴圈
        for j in range(0,img.shape[0]):         
            randpepper = np.random.random()             #生成0-1之間的隨機數
            if randpepper < prob:                       #若小於閥值
                output[j][i] = 0                        #則設定灰階為0
            elif randpepper > the:                      #大於the閥值
                output[j][i] =255                       #設定灰階為255
            else:                                       #其他
                output[j][i] = img[j][i]                #設定為原圖的灰階值        
    time_end = time.time()                      
    timec =time_end - time_s                
    print(timec)    
    return output                                       #回傳    
    
def midium(img):                                        #設定中值濾波方法
    output = np.zeros(img.shape)                        #生成與輸入相同維度的零矩陣
        
    for y in range(0,img.shape[1]-2):                   #雙重迴圈
        for x in range(0,img.shape[0]-2):
            kernal = img[x:x+3,y:y+3]                   #讀取以xy為中心的3*3矩陣
            kernalsort = []                             #設定空list
            for i in range(kernal.shape[1]):            #雙重迴圈讀取3*3矩陣的值
                for j in range(kernal.shape[0]):
                    #print(kernal.shape)
                    kernalsort.append(kernal[j][i])     #存入list
            kernalsort = sorted(kernalsort)             #排序大小    
            output[x][y] = kernalsort[5]                #取中位數值存入output[x][y]
    return output                                       #回傳

img = cv2.imread('ntust_gray.jpg',0)                    #讀取圖片    
img = im2double(img)                                    #呼叫函式double
out = saltpepper(img,0.15)                              #呼叫函式saltpepper
out1 = midium(midium(midium(out)))                      #呼叫函式中值濾波
imgshow(out1)                                           #顯示結果
imgshow(out)

cv2.imwrite('pepper.jpg',out*255)                       #儲存圖片
cv2.imwrite('midium.jpg',out1*255)  