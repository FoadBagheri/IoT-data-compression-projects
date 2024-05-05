import gzip
import io


def compress_text(input_path, output_path):
    with open(input_path, 'rt') as input_file, gzip.open(output_path, 'wb') as gzipped_file:
        text_content = input_file.read()
        gzipped_file.write(text_content.encode('utf-8'))


def decompress_text(input_path, output_path):
    with gzip.open(input_path, 'rb') as compressed_file, open(output_path, 'wt') as output_file:
        decompressed_text = compressed_file.read().decode('utf-8')
        output_file.write(decompressed_text)


input_text_file = "input.txt"
compressed_file = "compressed_text.gz"
decompressed_text_file = "decompressed_text.txt"

compress_text(input_text_file, compressed_file)

decompress_text(compressed_file, decompressed_text_file)
