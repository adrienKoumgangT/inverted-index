import os
import re
from collections import defaultdict


def build_inverted_index(directory):
    """
    Builds an inverted index from a collection of files

    Params:
        directory: List of file paths to process

    Returns:
    Dict where keys are words and values are sets of document names
    """
    inverted_index = defaultdict(set)

    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            try:
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
                    content = file.read().lower()
                    words = re.findall(r'\b\w+\b', content)
                    for word in words:
                        inverted_index[word].add(filename)
            except Exception as e:
                print(f"Could not read {filename}: {e}")
    return inverted_index




