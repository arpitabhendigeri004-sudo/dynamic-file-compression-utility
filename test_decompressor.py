from src.huffman import *
from src.decompressor import HuffmanDecompressor

text = """
Data Structures and Algorithms
"""

frequency = calculate_frequency(text)

root = build_huffman_tree(frequency)

codes = generate_codes(root)

encoded_text = encode_text(
    text,
    codes
)

decompressor = HuffmanDecompressor(root)

decoded_text = decompressor.decompress(
    encoded_text,
    "decompressed_files/output.txt"
)

print("\nOriginal:")
print(text)

print("\nRecovered:")
print(decoded_text)