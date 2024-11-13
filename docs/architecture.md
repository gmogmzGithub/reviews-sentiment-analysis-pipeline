# Architecture Overview

## System Architecture

```
[Amazon Reviews] → [Apache Flume] → [HDFS] → [HuggingFace Model] → [RAG Implementation]
```

### Data Flow
1. Reviews data ingestion via Flume
2. Storage in HDFS
3. Processing through ML pipeline
4. Result storage and retrieval

## Component Details

### 1. Data Ingestion Layer

#### Apache Flume
- **Purpose**: Reliable data ingestion
- **Configuration**: 
  - Source: Spooling directory
  - Channel: Memory-based
  - Sink: HDFS
- **Features**:
  - Fault tolerance
  - Back-pressure handling
  - Configurable batching

### 2. Storage Layer

#### HDFS
- **Purpose**: Distributed storage
- **Structure**:
  ```
  /user/guillermo_gomezmora/
  └── hdfs-reviews/
      ├── YYYY-MM-DD/
      │   ├── reviews.1.txt
      │   └── reviews.2.txt
      └── _SUCCESS
  ```
- **Features**:
  - Data replication
  - Fault tolerance
  - Scalability

### 3. Processing Layer

#### Sentiment Analysis
- **Technology**: HuggingFace Transformers
- **Model**: Sentiment analysis pre-trained model
- **Integration**: Python-based processing pipeline

#### RAG Implementation
- **Purpose**: Enhanced analysis capabilities
- **Components**:
  - Document retrieval
  - Context generation
  - Query processing

## Data Flow Details

### 1. Ingestion Flow
```
[Source Files] → [Flume Agent] → [Memory Channel] → [HDFS Sink]
```
- Monitoring directory for new files
- Batch processing of events
- Reliable delivery to HDFS

### 2. Processing Flow
```
[HDFS] → [Python Scripts] → [ML Model] → [Results Storage]
```
- Data extraction from HDFS
- Preprocessing for ML
- Model inference
- Results storage

## Security Architecture

### Data Security
- File-level permissions
- Network security
- API authentication

### Access Control
- HDFS permissions
- Service authentication
- API access control

## Scalability Considerations

### Current Scale
- Single node setup
- Batch processing capability
- Limited by hardware resources

### Future Scaling
- Distributed processing
- Multiple Flume agents
- Parallel processing

## Monitoring and Logging

### System Monitoring
- Flume metrics
- HDFS health
- Processing pipeline metrics

### Logging
- Centralized logging
- Error tracking
- Performance metrics

## Future Enhancements

### Planned Improvements
1. Real-time processing
2. Enhanced error handling
3. Advanced monitoring
4. API development

### Integration Points
1. Additional data sources
2. Alternative ML models
3. Visualization tools
4. External APIs

## Dependencies

### Software Dependencies
- Apache Hadoop
- Apache Flume
- Python 3.8+
- HuggingFace Transformers

### Infrastructure Dependencies
- GCP Compute Engine
- Network connectivity
- Storage capacity

## Backup and Recovery

### Backup Strategy
1. Configuration backups
2. Data replication
3. Code version control

### Recovery Procedures
1. Service restoration
2. Data recovery
3. Configuration restoration
