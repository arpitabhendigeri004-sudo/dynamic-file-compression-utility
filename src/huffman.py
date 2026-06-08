import heapq
from collections import Counter


# ----------------------------
# Huffman Tree Node
# ----------------------------

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


# ----------------------------
# Calculate Frequencies
# ----------------------------

def calculate_frequency(text):
    return Counter(text)


# ----------------------------
# Build Huffman Tree
# ----------------------------

def build_huffman_tree(frequency):

    heap = []

    for char, freq in frequency.items():
        heapq.heappush(heap, Node(char, freq))

    while len(heap) > 1:

        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = Node(None, left.freq + right.freq)

        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    return heap[0]


# ----------------------------
# Generate Huffman Codes
# ----------------------------

def generate_codes(root):

    codes = {}

    def helper(node, current_code):

        if node is None:
            return

        if node.char is not None:
            codes[node.char] = current_code
            return

        helper(node.left, current_code + "0")
        helper(node.right, current_code + "1")

    helper(root, "")

    return codes


# ----------------------------
# Encode Text
# ----------------------------

def encode_text(text, codes):

    encoded_text = ""

    for char in text:
        encoded_text += codes[char]

    return encoded_text


# ----------------------------
# Decode Text
# ----------------------------

def decode_text(encoded_text, root):

    decoded_text = ""

    current = root

    for bit in encoded_text:

        if bit == "0":
            current = current.left
        else:
            current = current.right

        if current.char is not None:
            decoded_text += current.char
            current = root

    return decoded_text


# ----------------------------
# Print Frequency Table
# ----------------------------

def print_frequency_table(frequency):

    print("\nCharacter Frequencies")
    print("-" * 30)

    for char, freq in sorted(frequency.items()):
        print(f"{repr(char)} : {freq}")


# ----------------------------
# Print Huffman Codes
# ----------------------------

def print_huffman_codes(codes):

    print("\nHuffman Codes")
    print("-" * 30)

    for char, code in sorted(codes.items()):
        print(f"{repr(char)} : {code}")