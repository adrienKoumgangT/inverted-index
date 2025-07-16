import os

from manager import run_program


if __name__ == "__main__":

    VERSIONS = ['v1', 'v2']

    TESTS = {
        "test1": "./input/test1",
        "test2": "./input/test2",
        "test3": "./input/test3"
    }

    OUTPUT_BASE_DIR = "./output"

    # Run all tests
    for test_name, input_dir in TESTS.items():
        print(f"\nRunning test: {test_name}")
        if os.path.exists(input_dir):
            run_program(input_dir, OUTPUT_BASE_DIR, test_name)
        else:
            print(f"Warning: Input directory {input_dir} not found, skipping test")
