import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import time
import random
import string

def generate_random_text_file(filename, size_in_mb):
    size_in_bytes = size_in_mb * 1024 * 1024
    chars = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation + ' ', k=1024))
    
    with open(filename, 'w') as f:
        for _ in range(size_in_bytes // 1024):
            f.write(chars)

def convert_to_uppercase(filename):
    start_time = time.time()

    with open(filename, 'r') as f:
        content = f.read()
        content_upper = content.upper()

    output_filename = f"uppercase_{filename}"
    with open(output_filename, 'w') as f:
        f.write(content_upper)
    
    end_time = time.time()
    time_taken = end_time - start_time
    return time_taken

file_sizes = [200, 400, 600, 800, 1000]
time_taken = []

for size in file_sizes:
    filename = f'random_text_{size}MB.txt'
    generate_random_text_file(filename, size)
    print(f"{size}MB file generated.")

    time_taken_for_file = convert_to_uppercase(filename)
    print(f"Time taken to convert {size}MB file to uppercase: {time_taken_for_file:.2f} seconds")
    
    time_taken.append(time_taken_for_file)

plt.figure(figsize=(10, 6))
plt.plot(file_sizes, time_taken, marker='o', color='b', label='Time to convert to uppercase')
plt.title('Time Taken to Convert Text Files to Upper Case')
plt.xlabel('File Size (MB)')
plt.ylabel('Time Taken (seconds)')
plt.grid(True)
plt.legend()
plt.show()