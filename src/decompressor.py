from src.huffman import decode_text
from src.file_handler import save_decompressed_file


class HuffmanDecompressor:

    def __init__(self, root):
        self.root = root

    def decompress(
            self,
            encoded_text,
            output_path):

        decoded_text = decode_text(
            encoded_text,
            self.root
        )

        save_decompressed_file(
            output_path,
            decoded_text
        )

        return decoded_text