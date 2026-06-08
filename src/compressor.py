def compress_uploaded_text(text):

    frequency = calculate_frequency(text)

    root = build_huffman_tree(frequency)

    codes = generate_codes(root)

    encoded_text = encode_text(text, codes)

    original_size = len(text.encode("utf-8"))

    compressed_size = max(1, len(encoded_text)//8)

    ratio = (compressed_size/original_size)*100

    return {
        "encoded_text": encoded_text,
        "codes": codes,
        "ratio": ratio,
        "original_size": original_size,
        "compressed_size": compressed_size
    }