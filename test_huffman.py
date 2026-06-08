from src.huffman import *

text = "hello world"

frequency = calculate_frequency(text)

print_frequency_table(frequency)

root = build_huffman_tree(frequency)

codes = generate_codes(root)

print_huffman_codes(codes)

encoded = encode_text(text, codes)

print("\nEncoded:")
print(encoded)

decoded = decode_text(encoded, root)

print("\nDecoded:")
print(decoded)