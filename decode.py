import pickle
import time
from Quantize import Quantize, IQuantize, dequantize_image, quantize_image
from huffman import huffman_compress, huffman_decompress
from prediction import predict
from raster_scan import raster_scan
from zero_tree import representation, presentation
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
        with open('Data/imgTransResult.pkl', 'rb') as file:
            imgTransResult = pickle.load(file)
        with open('Data/compressed_data.pkl', 'rb') as file:
            # 使用pickle.load从文件中读取变量
            compressed_data = pickle.load(file)
        with open('Data/huffman_codes.pkl', 'rb') as file:
            # 使用pickle.load从文件中读取变量
            huffman_codes = pickle.load(file)
        # # Calculate the encoding bit rate R(g)
        R_d=bit_rate(compressed_data,m,n)
        decoded_symbols = huffman_decompress(compressed_data,huffman_codes)
        # # Time()
        imgTransResult=presentation(imgTransResult,decoded_symbols,Height,Width,mt,nt)
        # # # pickle.dump(compressed_data, open('compressed_data.pkl', 'wb'))
        # # # pickle.dump(huffman_codes, open('huffman_codes.pkl', 'wb'))
        # # # pickle.dump(scanned_sequence, open('scanned_sequence.pkl', 'wb'))
        # # # pickle.dump(decoded_symbols, open('decoded_symbols.pkl', 'wb'))
        # # # pickle.dump(imgTransResult, open('imgTransResult.pkl', 'wb'))
        # # Time()
        imgTrans = np.copy(imgTransResult)
        # Time()
        imgTrans=IQuantize(imgTrans,q)
        Time()
        for i in range(5):
            ImgRe = idwt(imgTrans)
        Time()
        t1=time.time()
        PSNR=psnr(ImgRe,img)
        print(t1-t0,"--------------时间")
        print(PSNR,"------PSNR")

        print(R_d,"---------压缩率")
        D.append(PSNR)
        R.append(R_d)
        plt.imshow(ImgRe,'gray')
        print(D)
        print("-----------------------")
        print(R)
        print("-----------------------")
        plt.show()
