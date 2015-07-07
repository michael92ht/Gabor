# -*- coding: utf-8 -*-
    # gabor.py
    # 2015-7-7
    # github: https://github.com/michael92ht
    #__author__ = 'huangtao'
    
# import the necessary packages
import numpy as np
import cv2 as cv
from pylab import *

#定义了一个4尺度6方向的Gabor变换
#并将4尺度6方向变换函数图像及指定图像变换后的图像保存在指定文件夹
#可扩展为各种方法求纹理特征值等
def Gabor_u4v6(image,image_save_path):
    #图像预处理
    image=cv.imread(image,1);
    src = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    src_f = np.array(src, dtype=np.float32)
    src_f /= 255.

    us=[7,12,17,21]             #4种尺度
    vs=[0,30,60,90,120,150]     #6个方向
    kernel_size =21             
    sig = 5                     #sigma 带宽，取常数5
    gm = 1.0                    #gamma 空间纵横比，一般取1
    ps = 0.0                    #psi 相位，一般取0
    i=0
    for u in us:
        for v in vs:
            lm = u
            th = v*np.pi/180
            kernel = cv.getGaborKernel((kernel_size,kernel_size),sig,th,lm,gm,ps)
            kernelimg = kernel/2.+0.5
            dest = cv.filter2D(src_f, cv.CV_32F,kernel)
            cv.imwrite(image_save_path + str(i) + 'Kernel.jpg', cv.resize(kernelimg, (kernel_size*20,kernel_size*20))*256)
            cv.imwrite(image_save_path + str(i) + 'Mag.jpg', np.power(dest,2))
            i+=1


if __name__ == '__main__':
    image_save_path=r'd:/cv/'
    image=r'd:/cv/000.jpg'
    Gabor_u4v6(image,image_save_path)

