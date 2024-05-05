def run_length_encoding(input_data):
    compressed_data = []
    count = 1

    for i in range(1, len(input_data)):
        if input_data[i] == input_data[i - 1]:
            count += 1
        else:
            compressed_data.append((input_data[i - 1], count))
            count = 1

    compressed_data.append((input_data[-1], count))

    return compressed_data

def run_length_decoding(compressed_data):
    decompressed_data = []

    for element in compressed_data:
        value, count = element
        decompressed_data.extend([value] * count)

    return decompressed_data

input_data = [0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1]
compressed_data = run_length_encoding(input_data)
decompressed_data = run_length_decoding(compressed_data)

print("Input Data:", input_data)
print("Compressed Data:", compressed_data)
print("Decompressed Data:", decompressed_data)
