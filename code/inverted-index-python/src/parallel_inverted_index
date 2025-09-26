import os
import re
from collections import defaultdict
from multiprocessing import Pool
from utils import safe_extract


def process_file(args):
    """Helper for parallel processing"""
    filepath, base_dir = args
    text = safe_extract(filepath)
    words = re.findall(r'\b\w+\b', text) if text else []
    return [(word, os.path.relpath(filepath, base_dir)) for word in words]


def build_parallel_inverted_index(directory, workers=4):
    """Faster processing using multiprocessing"""
    filepaths = []
    for root, _, files in os.walk(directory):
        filepaths.extend(os.path.join(root, f) for f in files if f.lower().endswith(('.txt', '.pdf', '.docx', '.html')))

    with Pool(workers) as pool:
        results = pool.map(process_file, [(fp, directory) for fp in filepaths])

    inverted_index = defaultdict(set)
    for word_tuples in results:
        for word, path in word_tuples:
            inverted_index[word].add(path)

    return inverted_index

