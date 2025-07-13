# inverted-index
This project implements an inverted index—a fundamental data structure used in search engines like Google—using Hadoop MapReduce in a pseudo-distributed environment.
The goal is to process a collection of text files and generate an index that maps each word to the documents where it appears.


---

## 📁 Project Structure

```bash
inverted-index/
│
├── code/
    ├── inverted-index-java/
    └── inverted-index-python/
├── data/
├── hadoop-configs/
│   ├── core-site.xml
│   ├── hdfs-site.xml
│   ├── mapred-site.xml
│   └── yarn-site.xml
├── hadoop-logs/
├── input/
│   ├── test1/                    # First test dataset
│   └── test2/                    # Second test dataset
├── output/
```

### Java version


```bash
inverted-index-java/
│
├── pom.xml                       # Maven project descriptor
├── README.md                     # Project documentation for java version
└── src/
    └── main/
        ├── java/
        │   └── it/unipi/adrien/koumgang/
        │       ├── Main.java                     # Entry point
        │       ├── InvertedIndexMapper.java      # v1 Mapper
        │       ├── InvertedIndexReducer.java     # Reducer
        │       ├── InvertedIndexCombiner.java    # Combiner
        │       ├── InvertedIndexInMapperV2.java  # v2 Mapper (with in-mapper combining)
        │       └── TextUtils.java                # Utility functions
        └── resources/
```

### Python version

```bash
inverted-index-python/
│
├── README.md                     # Project documentation for python version
└── src/
    ├── __init__.py
    └── main.py
```

---

## Technical Stack

- Hadoop 3.4.1 (for distributed processing)
- Docker & Docker Compose (containerized environment)
- Java (MapReduce) (core implementation)
- Python (sequential version for benchmarking)

