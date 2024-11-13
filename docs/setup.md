# Setup Guide

This document provides detailed instructions for setting up the Reviews Sentiment Analysis Pipeline on a Google Cloud Platform (GCP) cluster.

## Prerequisites

### System Requirements
- Google Cloud Platform Account
- Compute Engine instance with sufficient resources
  - Minimum 4 vCPUs
  - 16GB RAM
  - 100GB disk space
- Ubuntu 20.04 LTS or later

### Required Software
- Apache Hadoop 3.x
- Apache Flume 1.11.0
- Python 3.8+
- Java 11

## Installation Steps

### 1. Hadoop Setup

```bash
# Update package list
sudo apt-get update

# Install Java
sudo apt-get install -y openjdk-11-jdk

# Verify Java installation
java -version
```

### 2. Apache Flume Installation

```bash
# Download Flume
wget https://dlcdn.apache.org/flume/1.11.0/apache-flume-1.11.0-bin.tar.gz

# Extract the archive
tar -xvf apache-flume-1.11.0-bin.tar.gz

# Move to final location
mv apache-flume-1.11.0-bin /home/guillermo_gomezmora/
```

### 3. Project Directory Structure

```bash
# Create necessary directories
mkdir -p /home/guillermo_gomezmora/jsons
mkdir -p /home/guillermo_gomezmora/quickstart
```

### 4. Python Environment Setup

```bash
# Install pip if not already installed
sudo apt-get install -y python3-pip

# Install required Python packages
pip3 install transformers
pip3 install torch
pip3 install pandas
```

## Configuration

### 1. HDFS Configuration

Ensure HDFS is properly configured:
```bash
# Create necessary HDFS directories
hdfs dfs -mkdir -p /user/guillermo_gomezmora/hdfs-reviews

# Set appropriate permissions
hdfs dfs -chmod -R 777 /user/guillermo_gomezmora/hdfs-reviews
```

### 2. Flume Configuration

Place the Flume configuration file in the appropriate directory:
```bash
# Copy configuration file
cp f.config /home/guillermo_gomezmora/quickstart/
```

## Testing the Setup

1. Generate sample data:
```bash
python3 scripts/generate_reviews.py
```

2. Start Flume agent:
```bash
flume-ng agent \
  --conf /home/guillermo_gomezmora/apache-flume-1.11.0-bin/conf \
  -n ReviewHDFSAgent \
  -f quickstart/f.config \
  -Xmx1024m
```

3. Verify data ingestion:
```bash
hdfs dfs -ls /user/guillermo_gomezmora/hdfs-reviews
```

## Troubleshooting

### Common Issues

1. **HDFS Connection Issues**
   - Check if Hadoop services are running
   - Verify network connectivity
   - Check port availability

2. **Flume Agent Not Starting**
   - Verify Java installation
   - Check configuration file syntax
   - Examine Flume logs

3. **Data Not Appearing in HDFS**
   - Check source directory permissions
   - Verify Flume agent is running
   - Check HDFS permissions

## Maintenance

### Regular Tasks
1. Monitor disk space usage
2. Check Flume logs for errors
3. Backup configuration files
4. Update software as needed

### Logging
- Flume logs: `/home/guillermo_gomezmora/flume.log`
- HDFS logs: Check Hadoop logging directory

## Security Considerations

1. File Permissions
2. Network Access
3. API Credentials (for future ML integration)
4. Data Privacy

## Next Steps

After completing the setup:
1. Test with sample data
2. Monitor system performance
3. Proceed with ML model integration
4. Set up monitoring and alerting
