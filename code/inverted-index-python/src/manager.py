import os
import time
from datetime import datetime
from inverted_index import build_inverted_index
from parallel_inverted_index import build_parallel_inverted_index


def save_index(index, output_dir, test_name):
    # Create output directory if not exists
    os.makedirs(output_dir, exist_ok=True)

    # Generate timestamped filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = os.path.join(output_dir, f"inverted_index_{test_name}_{timestamp}.txt")

    with open(output_file, 'w', encoding='utf-8') as file:
        for word in sorted(index.keys()):
            files = ' '.join(sorted(index[word]))
            file.write(f"{word} {files}\n")

    return output_file


def run_program(input_dir, output_base_dir, test_name, version: str = 'v1'):
    start_time = time.time()

    # Create test-specific output directory
    output_dir = os.path.join(output_base_dir, test_name)
    os.makedirs(output_dir, exist_ok=True)

    # Build and save index
    if version == 'v2':
        index = build_parallel_inverted_index(input_dir)
    else:
        index = build_inverted_index(input_dir)
    output_file = save_index(index, output_dir, test_name)

    end_time = time.time()

    print(f"Test '{test_name}' completed in {end_time - start_time:.2f} seconds")
    print(f"Results saved to: {output_file}")

    return output_file
