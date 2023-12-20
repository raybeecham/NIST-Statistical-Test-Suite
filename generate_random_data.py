import os

def generate_random_binary_file(filename, num_bytes=1000):
    with open(filename, 'wb') as fout:
        fout.write(os.urandom(num_bytes))

# Generate a file with 1000 random bytes (8000 bits)
generate_random_binary_file('random_data.bin', 1000)