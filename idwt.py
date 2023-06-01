import pickle
import time
import numpy as np
import pywt


def idwt2(coeffs, wavelet = 'haar'):
    data = coeffs[-1]

    for i in range(len(coeffs) - 2, -1, -1):
        cA = data
        cH, cV, cD = coeffs[i][1]
        data = pywt.idwt2((cA, (cH, cV, cD)), wavelet)

    return data
def idwt(img):
    m, n = img.shape
    imgDWT = np.zeros((m+4, n+4))
    mt, nt = imgDWT.shape
    height = mt/2
    width = nt/2
    imgDWT[2:mt-2, 2:nt-2] = img
    imgInTrans = np.copy(imgDWT)
    for j in range(2, nt-2):
        imgInTrans[0][j] = imgInTrans[2][j]
        imgInTrans[1][j] = imgInTrans[3][j]
        imgInTrans[mt - 1][j] = imgInTrans[mt - 3][j]
        imgInTrans[mt - 2][j] = imgInTrans[mt - 4][j]
        for i in range(2, mt-2, 2):
            imgInTrans[i][j] = imgDWT[int(i/2)][j] - (imgDWT[int(i/2+width-1)][j]+imgDWT[int(i/2+width+1)][j]+2)/4
        for i in range(1, mt-2, 2):
            imgInTrans[i][j] = imgDWT[int(i/2+width)][j] + (imgInTrans[i-1][j]+imgInTrans[i+1][j])/2

    imgDWT = np.copy(imgInTrans)

    for i in range(2, mt):
        imgInTrans[i][0] = imgInTrans[i][2]
        imgInTrans[i][1] = imgInTrans[i][3]
        imgInTrans[i][nt-1] = imgInTrans[i][nt-3]
        imgInTrans[i][nt-2] = imgInTrans[i][nt-4]
        for j in range(2, nt-2, 2):
            imgInTrans[i][j] = imgDWT[i][int(j/2)] - (imgDWT[i][int(j/2+height-1)] + imgDWT[i][int(j/2+height+1)]+2) / 4
        for j in range(1, nt-2, 2):
            imgInTrans[i][j] = imgDWT[i][int(j/2+height)] + (imgInTrans[i][j-1]+imgInTrans[i][j+1])/2
    return imgInTrans[2:mt-2, 2:nt-2]