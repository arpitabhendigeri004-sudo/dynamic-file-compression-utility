import os


# ----------------------------------
# Read Input File
# ----------------------------------

def read_file(filepath):

    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return file.read()

    except FileNotFoundError:
        print("File not found.")
        return None


# ----------------------------------
# Save Compressed Data
# ----------------------------------

def save_compressed_file(filepath, encoded_text):

    with open(filepath, "w") as file:
        file.write(encoded_text)

    print(f"Compressed file saved: {filepath}")


# ----------------------------------
# Save Decompressed Data
# ----------------------------------

def save_decompressed_file(filepath, text):

    with open(filepath, "w", encoding="utf-8") as file:
        file.write(text)

    print(f"Decompressed file saved: {filepath}")


# ----------------------------------
# Save Frequency Table
# ----------------------------------

def save_frequency_table(filepath, frequency):

    with open(filepath, "w", encoding="utf-8") as file:

        file.write("Character Frequency Table\n")
        file.write("=" * 30 + "\n")

        for char, freq in sorted(frequency.items()):
            file.write(f"{repr(char)} : {freq}\n")

    print(f"Frequency table saved: {filepath}")


# ----------------------------------
# Save Huffman Codes
# ----------------------------------

def save_huffman_codes(filepath, codes):

    with open(filepath, "w", encoding="utf-8") as file:

        file.write("Huffman Codes\n")
        file.write("=" * 30 + "\n")

        for char, code in sorted(codes.items()):
            file.write(f"{repr(char)} : {code}\n")

    print(f"Huffman codes saved: {filepath}")


# ----------------------------------
# Save Compression Report
# ----------------------------------

def save_compression_report(
        filepath,
        original_size,
        compressed_size,
        ratio):

    with open(filepath, "w", encoding="utf-8") as file:

        file.write("Compression Report\n")
        file.write("=" * 40 + "\n\n")

        file.write(f"Original Size : {original_size} bytes\n")
        file.write(f"Compressed Size : {compressed_size} bytes\n")
        file.write(f"Compression Ratio : {ratio:.2f}%\n")

    print(f"Report saved: {filepath}")


# ----------------------------------
# Get File Size
# ----------------------------------

def get_file_size(filepath):

    return os.path.getsize(filepath)