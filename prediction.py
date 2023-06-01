# 预测函数，将最低频率子带的像素预测为左边和上方像素值的平均
import numpy as np
def predict(imgTransResult,Height,Width):
    predicted_subband=np.zeros((int(Height),int(Width)))
    # 对最低频率子带的每个像素进行预测
    for i in range(int(Height)):
        for j in range(int(Width)):
            if i == 0 and j == 0:
                # 左上角像素无法预测，直接复制
                predicted_subband[i, j] = imgTransResult[i, j]
            elif i == 0:
                # 第一行像素，预测值为左侧像素值
                predicted_subband[i, j] = imgTransResult[i, j-1]
            elif j == 0:
                # 第一列像素，预测值为上方像素值
                predicted_subband[i, j] = imgTransResult[i-1, j]
            else:
                # 其他位置的像素，预测值为左边和上方像素值的平均
                predicted_subband[i, j] = (imgTransResult[i, j-1] + imgTransResult[i-1, j]) / 2
    imgTransResult[0:int(Height), 0:int(Width)]=0.3*predicted_subband+0.7*imgTransResult[0:int(Height), 0:int(Width)]
    print("------完成predict流程------\n")
    # return imgTransResult[0:int(Height), 0:int(Width)]
    return imgTransResult

