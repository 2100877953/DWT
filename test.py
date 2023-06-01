import numpy as np

def dwt_5_3(img):
    # 获取图像尺寸
    m, n = img.shape

    # 复制输入图像
    img_copy = np.copy(img)

    # 定义水平方向的分析滤波器
    h_analysis_filter = np.array([-1/2, 1, 1/2])

    # 定义水平方向的合成滤波器
    h_synthesis_filter = np.array([1/4, 1/2, 1/4])

    # 水平方向的分析滤波器应用
    for i in range(m):
        img_copy[i, 1:n-1] = np.convolve(img_copy[i, :], h_analysis_filter, mode='valid')

    # 水平方向的高频系数计算
    horizontal_coeff = img_copy[:, 1:n]

    # 水平方向的低频系数
    horizontal_low_freq = img_copy[:, 0:n-1]

    # 水平方向的合成滤波器应用
    for i in range(m):
        img_copy[i, 1:n-1] = np.convolve(img_copy[i, :], h_synthesis_filter, mode='valid')

    return horizontal_coeff, horizontal_low_freq, img_copy

def idwt_5_3(horizontal_coeff, horizontal_low_freq, img):
    # 获取图像尺寸
    m, n = img.shape

    # 复制输入图像
    img_copy = np.copy(img)

    # 定义水平方向的合成滤波器
    h_synthesis_filter = np.array([1/4, 1/2, 1/4])

    # 水平方向的合成滤波器应用
    for i in range(m):
        img_copy[i, 1:n-1] = np.convolve(img_copy[i, :], h_synthesis_filter, mode='valid')

    # 恢复水平方向的高频系数
    img_copy[:, 1:n] += horizontal_coeff

    # 恢复水平方向的低频系数
    img_copy[:, 0:n-1] += horizontal_low_freq

    return img_copy

# 示例用法
# 创建一个大小为4x4的图像
image = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]])

# 执行水平方向的5/3小波变换和反变换
horizontal_coeff, horizontal_low_freq, transformed_image = dwt_5_3(image)
reconstructed_image = idwt_5_3(horizontal_coeff, horizontal_low_freq, transformed_image)

# 输出水平方向的高频系数、低频系数和还原图像
print("水平方向的高频系数:")
print(horizontal_coeff)
print("水平方向的低频系数:")
print(horizontal_low_freq)
print(reconstructed_image)
