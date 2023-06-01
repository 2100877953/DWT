from collections import defaultdict
from heapq import heappop, heappush
def huffman_decompress(compressed_data, huffman_codes):
    # 哈夫曼解压缩
    decoded_symbols = []
    current_code = ""
    for bit in compressed_data:
        current_code += bit
        for symbol, code in huffman_codes.items():
            if current_code == code:
                decoded_symbols.append(symbol)
                current_code = ""
                break
    print("------完成huffman_decompress流程------\n")
    return decoded_symbols
def huffman_compress(symbols):
    # 哈夫曼压缩
    freq = calculate_frequency(symbols)
    huffman_tree = build_huffman_tree(freq)
    huffman_codes = generate_huffman_codes(huffman_tree)
    encoded_symbols = [huffman_codes[symbol] for symbol in symbols]
    compressed_data = ''.join(encoded_symbols)
    print("------完成huffman_compress流程------\n")
    return compressed_data, huffman_codes
def generate_huffman_codes(huffman_tree):
    # 生成哈夫曼编码
    huffman_codes = {}
    for pair in huffman_tree[1:]:
        symbol, code = pair
        huffman_codes[symbol] = code
    print("------完成generate_huffman_codes流程------\n")
    return huffman_codes
def build_huffman_tree(freq):
    # 构建哈夫曼树
    heap = [[weight, [symbol, ""]] for symbol, weight in freq.items()]
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    print("------完成build_huffman_tree流程------\n")
    return heap[0]
def calculate_frequency(symbols):
    # 计算符号的频率
    freq = defaultdict(int)
    for symbol in symbols:
        freq[symbol] += 1
    print("------完成calculate_frequency流程------\n")
    return freq
