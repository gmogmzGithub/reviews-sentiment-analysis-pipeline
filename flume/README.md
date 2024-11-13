# Apache Flume Configuration

This directory contains the Apache Flume configuration files used in our reviews sentiment analysis pipeline. The configuration is set up to monitor a directory for new review files and ingest them into HDFS.

## Configuration Overview

The main configuration file (`f.config`) defines an agent with three components:
- Source: Spooling directory source monitoring for new files
- Channel: Memory channel for buffering events
- Sink: HDFS sink for writing to Hadoop

```properties
ReviewHDFSAgent.sources = ReviewSource
ReviewHDFSAgent.sinks = HdfsSink
ReviewHDFSAgent.channels = MemoryChannel
```

## Components Detail

### Source Configuration
```properties
ReviewHDFSAgent.sources.ReviewSource.type = spooldir
ReviewHDFSAgent.sources.ReviewSource.spoolDir = /home/guillermo_gomezmora/jsons
ReviewHDFSAgent.sources.ReviewSource.fileHeader = false
ReviewHDFSAgent.sources.ReviewSource.deletePolicy = never
ReviewHDFSAgent.sources.ReviewSource.batchSize = 1000
ReviewHDFSAgent.sources.ReviewSource.inputCharset = UTF-8
```

- **Type**: Spooling directory source
- **Spool Directory**: Directory monitored for new files
- **Delete Policy**: Set to 'never' for debugging purposes
- **Batch Size**: 1000 events per batch for optimal performance
- **Input Charset**: UTF-8 for proper character encoding

### Channel Configuration
```properties
ReviewHDFSAgent.channels.MemoryChannel.type = memory
ReviewHDFSAgent.channels.MemoryChannel.capacity = 1000
ReviewHDFSAgent.channels.MemoryChannel.transactionCapacity = 1000
```

- **Type**: Memory channel
- **Capacity**: 1000 events
- **Transaction Capacity**: 1000 events per transaction

### Sink Configuration
```properties
ReviewHDFSAgent.sinks.HdfsSink.type = hdfs
ReviewHDFSAgent.sinks.HdfsSink.hdfs.path = hdfs://big-data-m:8020/user/guillermo_gomezmora/hdfs-reviews/
ReviewHDFSAgent.sinks.HdfsSink.hdfs.fileType = DataStream
ReviewHDFSAgent.sinks.HdfsSink.hdfs.writeFormat = Text
```

- **Type**: HDFS sink
- **Path**: HDFS path where files are stored
- **File Type**: DataStream for continuous writing
- **Write Format**: Text format for readability

## Usage

### Starting the Flume Agent

```bash
flume-ng agent \
  --conf /home/guillermo_gomezmora/apache-flume-1.11.0-bin/conf \
  -n ReviewHDFSAgent \
  -f /path/to/f.config \
  -Xmx1024m
```

### Monitoring

Monitor the Flume process with:
```bash
tail -f /path/to/flume.log
```

Check HDFS directory for ingested files:
```bash
hdfs dfs -ls /user/guillermo_gomezmora/hdfs-reviews/
```

## Error Handling

Common errors and solutions:

1. **Connection Refused to HDFS**
   - Verify HDFS is running: `jps`
   - Start if needed: `start-dfs.sh`

2. **File Not Found in Spool Directory**
   - Check permissions
   - Verify path in configuration

3. **Memory Issues**
   - Adjust JVM heap size with -Xmx parameter
   - Tune channel capacity settings

## Configuration Tips

1. **Performance Tuning**
   - Adjust `batchSize` based on file sizes
   - Modify `capacity` and `transactionCapacity` for throughput

2. **File Rotation**
   - `rollSize`: Size-based rotation
   - `rollCount`: Event count-based rotation
   - `rollInterval`: Time-based rotation

3. **Data Integrity**
   - Use `fileHeader` for metadata
   - Configure proper `deletePolicy`

## Dependencies

- Apache Flume 1.11.0
- Hadoop/HDFS cluster
- Java Runtime Environment (JRE)

## Notes

- Current configuration is optimized for review data ingestion
- Timestamp interceptor added for event tracking
- HDFS path includes date-based partitioning
