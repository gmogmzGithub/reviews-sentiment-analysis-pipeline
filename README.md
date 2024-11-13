# Reviews Sentiment Analysis Pipeline

A complete end-to-end data engineering and machine learning pipeline that processes Amazon reviews through Apache Flume into HDFS, and performs sentiment analysis using Hugging Face transformers and RAG (Retrieval Augmented Generation).

## Project Architecture
```ascii
[Amazon Reviews] → [Apache Flume] → [HDFS] → [HuggingFace Model] → [RAG Implementation]
```

## Components

### 1. Data Ingestion Layer
- Apache Flume configuration for streaming review data into HDFS
- Custom spooling directory setup for batch processing
- Configured memory channel for optimal performance

### 2. Storage Layer
- HDFS integration for storing processed reviews
- Structured data organization for efficient retrieval
- Scalable storage solution for large datasets

### 3. Processing Layer (Coming Soon)
- Sentiment Analysis using HuggingFace Transformers
- RAG implementation for enhanced analysis
- Python scripts for data processing and model integration

## Setup Instructions

### Prerequisites
- Apache Hadoop (HDFS)
- Apache Flume 1.11.0
- Python 3.x
- Access to a Hadoop cluster

### Configuration Files
1. Flume Configuration (`f.config`):
```properties
# Key configurations shown here
ReviewHDFSAgent.sources = ReviewSource
ReviewHDFSAgent.sinks = HdfsSink
ReviewHDFSAgent.channels = MemoryChannel
...
```

### Running the Pipeline
1. Start HDFS:
```bash
start-dfs.sh
```

2. Run Flume agent:
```bash
flume-ng agent \
  --conf /path/to/flume/conf \
  -n ReviewHDFSAgent \
  -f /path/to/f.config
```

## Project Status
- [x] HDFS Cluster Setup
- [x] Flume Configuration
- [x] Data Ingestion Pipeline
- [ ] Sentiment Analysis Integration
- [ ] RAG Implementation
- [ ] API Development

## Future Enhancements
1. Real-time sentiment analysis
2. Dashboard for visualization
3. API endpoints for querying results
4. Scaling to handle larger datasets

## Technologies Used
- Apache Hadoop
- Apache Flume
- Python
- HuggingFace Transformers
- LangChain/LlamaIndex (upcoming)

## Directory Structure
```
├── flume/
│   ├── f.config
│   └── README.md
├── scripts/
│   ├── generate_reviews.py
│   └── sentiment_analysis.py
├── notebooks/
│   └── sentiment_analysis_demo.ipynb
├── tests/
├── docs/
└── README.md
```

## Contributing
Feel free to open issues or submit pull requests.
