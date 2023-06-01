import numpy as np

def Quantize(imgTransResult,step_size):
    print("------完成Quantize流程------\n")
    # step_size = (imgTransResult.max() - imgTransResult.min()) / levels
    quantized_signal = np.round(imgTransResult/step_size)

    return quantized_signal


def quantize_image(image_list, levels):
    # 将列表中的图像逐个进行量化
    quantized_images = []
    for image in image_list:
        scaled_image = image * (levels - 1) / 255.0
        quantized_image = np.round(scaled_image)
        quantized_images.append(quantized_image)

    return quantized_images

def dequantize_image(quantized_image, levels):
    # 将量化的图像从 [0, levels-1] 的范围缩放到 [0, 255]
    scaled_image = quantized_image * 255.0 / (levels - 1)

    # 将缩放后的图像取整，将其还原为连续的灰度值
    dequantized_image = np.round(scaled_image)

    return dequantized_image.astype(np.uint8)
def IQuantize(imgTrans,step_size):
    # step_size = (imgTrans.max() - imgTrans.min()) / levels

    # 反量化：将离散级别映射回连续信号值
    reconstructed_signal = imgTrans * step_size
    return reconstructed_signal
