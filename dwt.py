# forward one time dwt using Le Gall 5/3 wavelet
import time
import numpy as np
import numpy as np
import pywt
import Quantize


def dwt2(data, wavelet='haar',q=0):
    rows, cols = data.shape
    coeffs = []
    while rows >= 2 and cols >= 2:
        cA, (cH, cV, cD) = pywt.dwt2(data, wavelet)
        coeffs.append((cA, (cH, cV, cD)))
        data = cA[:rows//2, :cols//2]
        rows //= 2
        cols //= 2

    coeffs.append(data)
    return coeffs
# 使用示例



def dwt(img):
    # img_data = img.astype(float)
    img_data = img.astype(float)
    m,n = img_data.shape
    img_dwt = np.zeros(img.shape)
    imgTrans = np.zeros((m+4, n+4))
    mt,nt = imgTrans.shape
    Height = mt / 2
    Width = nt / 2
    imgTrans[2:mt-2, 2:nt-2] = img_data
    imgTransResult = np.copy(imgTrans)
    for i in range(2,mt):
        imgTrans[i][0] = imgTrans[i][2]
        imgTrans[i][1] = imgTrans[i][3]
        imgTrans[i][nt-1] = imgTrans[i][nt-3]
        imgTrans[i][nt-2] = imgTrans[i][nt-4]
        for j in range(1,nt-2,2):
            # High fruquency
            j_1 = int(Width + j/2)
            imgTransResult[i][j_1] = imgTrans[i][j] - (imgTrans[i][j-1]+imgTrans[i][j+1])/2
        for j in range(2,nt-2,2):
            i_1 = int(i/2)
            j_1 = int(Width + j / 2)
            j_2 = int(j/2)
            imgTransResult[i][j_2] = imgTrans[i][j] + (imgTransResult[i][j_1-1]+imgTransResult[i][j_1+1]+2)/4

    imgTrans = np.copy(imgTransResult)

    for j in range(2,nt):
        imgTrans[0][j] = imgTrans[2][j]
        imgTrans[1][j] = imgTrans[3][j]
        imgTrans[mt-1][j] = imgTrans[mt-3][j]
        imgTrans[mt-2][j] = imgTrans[mt-4][j]
        for i in range(1, mt-2, 2):
            # High fruquency
            i_1 = int(Width + i/2)
            imgTransResult[i_1][j] = imgTrans[i][j] - (imgTrans[i-1][j]+imgTrans[i+1][j])/2
        for i in range(2, mt-2, 2):
            i_1 = int(Width+i/2)
            i_2 = int(i/2)
            imgTransResult[i_2][j] = imgTrans[i][j] + (imgTransResult[i_1-1][j]+imgTransResult[i_1+1][j]+2)/4



    return imgTransResult[2:mt-2, 2:nt-2]
# forward twice dwt using Le Gall 5/3 wavelet
def twice_dwt(imgin):
    img = np.copy(imgin)
    m, n = img.shape
    img_deal = img[0:int(m/2), 0:int(n/2)]
    img_after_deal = dwt(img_deal)
    img[0:int(m/2), 0:int(n/2)] = img_after_deal
    return abs(img)


# forward three times dwt using Le Gall 5/3 wavelet
def thrice_dwt(imgin):
    img = np.copy(imgin)
    m, n = img.shape
    img_deal = img[0:int(m/4), 0:int(n/4)]
    img_after_deal = dwt(img_deal)
    img[0:int(m / 4), 0:int(n / 4)] = img_after_deal
    return abs(img)
def forice_dwt(imgin):
    img = np.copy(imgin)
    m, n = img.shape
    img_deal = img[0:int(m/8), 0:int(n/8)]
    img_after_deal = dwt(img_deal)
    img[0:int(m / 8), 0:int(n / 8)] = img_after_deal
    return abs(img)
def fivice_dwt(imgin):
    img = np.copy(imgin)
    m, n = img.shape
    img_deal = img[0:int(m/16), 0:int(n/16)]
    img_after_deal = dwt(img_deal)
    img[0:int(m / 16), 0:int(n / 16)] = img_after_deal
    return abs(img)