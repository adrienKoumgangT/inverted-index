import os
import re
from collections import defaultdict


def build_inverted_index(directory):
    inverted_index = defaultdict(set)

    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            try:
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
                    content = file.read().lower()
                    # words = content.split()
                    words = re.findall(r'\b\w+\b', content)  # removes punctuation
                    for word in words:
                        inverted_index[word].add(filename)
            except Exception as e:
                print(f"Could not read {filename}: {e}")

    return inverted_index


def save_index(index, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for word in sorted(index.keys()):
            files = ' '.join(sorted(index[word]))
            file.write(f"{word} {files}\n")


if __name__ == "__main__":
    import sys
    import time

    if len(sys.argv) != 3:
        print("Usage: python inverted_index.py <input_directory> <output_file>")
        sys.exit(1)

    start_time = time.time()
    index = build_inverted_index(sys.argv[1])
    save_index(index, sys.argv[2])
    end_time = time.time()

    print(f"Index built in {end_time - start_time:.2f} seconds")
