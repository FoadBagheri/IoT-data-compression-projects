from PIL import Image
import os

def compress_image(input_path, output_path, quality):
    try:
        img = Image.open(input_path)

        if img.mode == 'RGBA':
            img = img.convert('RGB')

        img.save(output_path, 'JPEG', quality=quality)

        original_size = os.path.getsize(input_path)
        compressed_size = os.path.getsize(output_path)
        print(f"Original Image Size: {original_size} bytes")
        print(f"Compressed Image Size: {compressed_size} bytes. Check '{output_path}'.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    input_image_path = "input_image.png"
    compressed_image_path = "compressed_image.jpg"

    compression_quality = 80

    compress_image(input_image_path, compressed_image_path, quality=compression_quality)
