import pickle
import time
from DWT.Quantize import Quantize, IQuantize, dequantize_image, quantize_image
from DWT.huffman import huffman_compress, huffman_decompress
from DWT.prediction import predict
from DWT.raster_scan import raster_scan
from DWT.zero_tree import representation, presentation
from  dwt import dwt,dwt2
from idwt import  idwt2
import numpy as np
import matplotlib.pyplot as plt
from  idwt import idwt
from RD_curve import psnr, bit_rate
def Time():
    print(time.time())
if __name__ == "__main__":
    t0=time.time()
    f = open('Img/image1.512', mode='rb')
    img = np.fromfile(f, dtype=np.ubyte)
    img = img.reshape(512, 512)
    img_data = img.astype(float)
    m,n = img_data.shape
    img_dwt = np.zeros(img.shape)
    imgTrans = np.zeros((m+4, n+4))
    mt,nt = imgTrans.shape
    Height = mt / 2
    Width = nt / 2
    R=[]
    D=[]
    for k in range(2,17):
        img_data=img
        q=k
        Time()
        for i in range (5):
            imgTransResult= dwt(img_data)
        # 应用预测到最低频率子带
        Time()
        imgTransResult=Quantize(imgTransResult,q)
        # # 应用预测到最低频率子带
        Time()
        imgTransResult=predict(imgTransResult,Height,Width)
        # imgTransResult=predict(imgTransResult,Height,Width)
        # # # 执行光栅扫描和零树扫描
        # Time()
        scanned_sequence = []
        # # 最低频率子带的光栅扫描
        # Time()
        scanned_sequence=raster_scan(scanned_sequence,imgTransResult,Height,Width)
        # # 高频子带的零树扫描和EZT符号
        # Time()
        scanned_sequence=representation(scanned_sequence,imgTransResult,Height,Width,mt,nt)
        # Time()
        compressed_data, huffman_codes = huffman_compress(scanned_sequence)
        pickle.dump(compressed_data, open('Data/compressed_data.pkl', 'wb'))
        pickle.dump(huffman_codes, open('Data/huffman_codes.pkl', 'wb'))
        pickle.dump(imgTransResult,open('Data/imgTransResult.pkl', 'wb'))
        # Time()

