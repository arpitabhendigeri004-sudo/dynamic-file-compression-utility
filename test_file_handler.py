from src.file_handler import *

text = read_file("input_files/sample.txt")

print(text)

save_decompressed_file(
    "decompressed_files/test.txt",
    text
)

print(
    get_file_size(
        "decompressed_files/test.txt"
    )
)