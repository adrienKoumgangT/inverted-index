import os

from manager import run_program


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 4:
        print("Usage: python inverted_index.py <version> <input_directory> <output_file>")
        sys.exit(1)

    version = sys.argv[1]
    input_dir = sys.argv[2].rstrip("/")
    output_dir = sys.argv[3].rstrip("/")

    output_dir_path = output_dir.split("/")
    test_name = output_dir_path[-1]

    print(f"\nRunning program: inverted index (version {version})")
    if os.path.exists(input_dir):
        run_program(input_dir, output_dir, test_name)
    else:
        print(f"Warning: Input directory {input_dir} not found, skipping test")
