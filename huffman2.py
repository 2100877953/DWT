import heapq
import collections

def build_frequency_table(sequence):
    frequency_table = collections.defaultdict(int)
    for symbol in sequence:
        frequency_table[symbol] += 1
    return frequency_table

def build_huffman_codebook(frequency_table):
    heap = [[weight, [symbol, ""]] for symbol, weight in frequency_table.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

def huffman_encode(sequence):
    frequency_table = build_frequency_table(sequence)
    codebook = build_huffman_codebook(frequency_table)
    encoded_sequence = ''.join(dict(codebook)[symbol] for symbol in sequence)
    return encoded_sequence, codebook

def huffman_decode(encoded_sequence, codebook):
    reverse_codebook = {code: symbol for symbol, code in codebook}
    decoded_sequence = []
    current_code = ''
    for bit in encoded_sequence:
        current_code += bit
        if current_code in reverse_codebook:
            symbol = reverse_codebook[current_code]
            decoded_sequence.append(symbol)
            current_code = ''
    return decoded_sequence
