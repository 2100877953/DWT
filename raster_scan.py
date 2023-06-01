def raster_scan(scanned_sequence,imgTransResult,Height,Width):
    for i in range(int(Height)):
        for j in range(int(Width)):
            scanned_sequence.append((1, imgTransResult[i, j]))
    print("------完成raster_scan流程------\n")
    return scanned_sequence
