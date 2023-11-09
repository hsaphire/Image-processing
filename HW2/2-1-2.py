import numpy as np
import cv2
from matplotlib import pyplot as plt




img = cv2.imread("jojo.jpg").astype(np.float32)           #讀取圖片並設定陣列格式為float32
img *= 1./255                                             #將矩陣點乘1/255   (目的是python cv的轉換色彩通道方式與matlab不同所以需要轉換)           
labimg = cv2.cvtColor(img,cv2.COLOR_BGR2LAB)              #色彩通道由RGB轉LAB
labimg2 = cv2.cvtColor(img,cv2.COLOR_BGR2LAB)
labimg[:,:,1] *=0                                         #將a通道設成零
labimg2[:,:,2] *=0                                        #將b通道設為零
labimg1 = cv2.cvtColor(labimg,cv2.COLOR_LAB2BGR)*255      #轉回RGB並乘回255
labimg3 = cv2.cvtColor(labimg2,cv2.COLOR_LAB2BGR)*255
cv2.imwrite(r'test2-1.jpg',labimg1.astype(np.uint8))      #輸出紅綠色盲影像
cv2.imwrite(r'test2-2.jpg',labimg3.astype(np.uint8))      #輸出黃藍色盲影像
#labimg1 = labimg1.astype(np.uint8)

#cv2.imwrite(r'test2.jpg',labimg1)
#labimg2 = cv2.cvtColor(np.uint8(merge2),cv2.COLOR_Lab2BGR)
