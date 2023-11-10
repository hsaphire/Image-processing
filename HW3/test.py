import numpy as np
import os ,sys
import cv2
import matplotlib.pyplot as plt
'''
//dataloader & select indicate photo *100 & resize photo to 8*8
'''

datapath  = r"train1000"
number  = [n for n in range(10)]
selectlist = []
img = []
l1_filiter = np.zeros((2,3,3))
l1_filiter[0,:,:]  = np.array([[[-1,-1, 1],
                                [-1, 0, 1],
                                [-1, 1, 1]]])

l1_filiter[1,:,:]  = np.array([[ 1, 1, 1],
                                [ 0, 0, 0],
                                 [-1,-1,-1]])   


'''        
/// cnn start
'''
class Conv:                   
    def conv(img,conv_filiter):
        '''
        if len(img.shape) >2 or len(conv_filiter.shape)>3:
            if img.shape[-1] != conv_filiter[-1]:
                print("Error: channels in both image and filiter must match")    
                sys.exit()
        if conv_filiter.shape[1] != conv_filiter.shape[2]:
            print('Error2 :filiter must be square matrix')
            sys.exit()
        if conv_filiter.shape[1]%2 ==0 :
            print("Error3:filiter must have an odd size")
            sys.exit()
        '''
        # define the featuremap after conv  size
        feature_maps = np.zeros((img.shape[0],
                                img.shape[1],
                                conv_filiter.shape[0]))
        

        for filiter_num in range(conv_filiter.shape[0]):
            #print("filiter",filiter_num+1)

            curr_filiter = conv_filiter[filiter_num,:,:]
            if len(img.shape) ==2:
                for i in range(img.shape[0]-2):
                    for j in range(img.shape[1]-2):
                        im_region =  img[i:i+3,j:j+3]
                        feature_maps[i,j] = np.sum(im_region*curr_filiter)
                return feature_maps    
            else :
                image1 = img[:,:,0]
                image2 = img[:,:,1] 
                feature_maps_special = np.zeros((img.shape[0],
                                                img.shape[1],
                                                conv_filiter.shape[0]-1))

                feature_maps_special2 = feature_maps_special               
                for i in range(image1.shape[0]-2):
                    for j in range(image1.shape[1]-2):
                        im_region =  image1[i:i+3,j:j+3]
                        feature_maps_special[i,j] = np.sum(im_region*curr_filiter)
                for i in range(image2.shape[0]-2):
                    for j in range(image2.shape[1]-2):
                        im_region =  image2[i:i+3,j:j+3]
                        feature_maps_special2[i,j] = np.sum(im_region*curr_filiter)
                #print(feature_maps_special.shape)  
                #print(feature_maps_special2.shape)   
                feature_maps = np.concatenate([feature_maps_special,feature_maps_special2],axis=2)
                return feature_maps


class MaxPool2:
    def maxpool2(input):
        h,w,c = input.shape
        new_h = h // 2
        new_w = w // 2
        output = np.zeros((new_h,new_w,c))
        for i in range(new_h):
            for j in range(new_w):
                im_region = input[(i*2):(i*2+2),(j*2):(j*2+2)]
                output[i,j] = np.amax(im_region,axis=(0,1))
        return output  
    


for s in range(2):
    select = int(input("plz enter num:"))
    selectlist.append(select)
for i,i2 in enumerate (selectlist):    
    for mnistselect in range(selectlist[i]*100+1,selectlist[i]*100+101,1):
        
        imageloader = os.path.join(datapath,str(mnistselect)+".png")
        #print(imageloader)
        image = cv2.imread(imageloader,cv2.IMREAD_GRAYSCALE)
        image = cv2.resize(image,(8,8),interpolation = cv2.INTER_AREA)
        #print(image.shape)
        feature = Conv.conv(image,l1_filiter)
        feature = MaxPool2.maxpool2(feature)
        feature = Conv.conv(feature,l1_filiter)
        feature = MaxPool2.maxpool2(feature)
        feature = feature.flatten() 
        print(feature)
        
       
