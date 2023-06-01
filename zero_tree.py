import numpy as np
import concurrent.futures
def is_zerotree(imgTransResult, i, j):
    if imgTransResult[i, j] == 0:
        if np.all(imgTransResult[i:i+4, j:j+4] == 0):
            return True
        else:
            return False
    else:
        return False
def get_subband_size(imgTransResult, i, j):
    size = 1
    while (i + size) < imgTransResult.shape[0] and (j + size) < imgTransResult.shape[1]:
        if np.any(imgTransResult[i:i+size+1, j:j+size+1] != 0):
            size += 1
        else:
            break
    return size
def  representation(scanned_sequence,imgTransResult,Height,Width,mt,nt):

    for i in range(int(Height), mt-4):
        for j in range(int(Width), nt-4):
            if is_zerotree(imgTransResult, i, j):
                scanned_sequence.append((0, 0))  # 零树符号
            else:
                size = get_subband_size(imgTransResult, i, j)
                amplitude = imgTransResult[i, j]
                scanned_sequence.append((size, amplitude))
    print("------完成representation流程------\n")
    return scanned_sequence
def presentation(imgTransResult,decoded_symbols,Height,Width,mt,nt):
    idx=0
    for i in range(int(Height)):
        for j in range(int(Width)):
            imgTransResult[i, j] = decoded_symbols[idx][1]
            idx += 1
    for i in range(int(Height), mt - 4):
        for j in range(int(Width), nt - 4):
            if decoded_symbols[idx][0] == 0:  # 零树符号
                # imgTransResult[i, j] = 0
                continue
            else:  # 非零系数
                size = decoded_symbols[idx][0]
                amplitude = decoded_symbols[idx][1]
                imgTransResult[i, j] = amplitude
                # imgTransResult[i:i+size, j:j+size] = amplitude
                # i=i+size
                # j=j+size
            idx += 1
    print("------完成presentation流程------\n")
    return imgTransResult