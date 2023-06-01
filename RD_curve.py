import math
import numpy as np
def psnr(original, compressed):

    # 计算原始图像和压缩图像的均方误差（Mean Squared Error，MSE）
    mse = np.mean((original - compressed) ** 2)

    # 计算图像的最大可能像素值
    max_pixel = np.max(compressed)

    # 计算PSNR值
    psnr = 10 * np.log10(max_pixel**2 / np.sqrt(mse))

    return psnr

def bit_rate(compressed_data,m,n):
    # Calculate the encoding bit rate R(g)
    total_bits = len(compressed_data)
    image_size = m * n
    encoding_bit_rate = total_bits / image_size
    print("------完成bit_rate流程------\n")
    return encoding_bit_rate