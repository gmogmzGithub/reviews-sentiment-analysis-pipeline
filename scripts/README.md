# Data Processing Scripts

This directory contains scripts for processing Amazon reviews data and performing sentiment analysis. The scripts are part of a larger pipeline that moves data through Flume into HDFS and performs sentiment analysis.

## Scripts Overview

### 1. `generate_reviews.py`
Processes Amazon reviews dataset into JSON format suitable for Flume ingestion.

### 2. `sentiment_analysis.py` (Coming Soon)
Will implement sentiment analysis on the processed reviews.

## Dataset Information

We use the Amazon Reviews dataset from Kaggle, which contains approximately 36 million reviews.

- **Dataset URL**: [Amazon Reviews Dataset](https://www.kaggle.com/datasets/kritanjalijain/amazon-reviews?resource=download)
- **Size**: ~36M reviews split between test and train files
- **Format**: CSV files containing review text, ratings, and metadata

### Dataset Schema
```python
{
    "reviewerID": str,      # Unique reviewer identifier
    "asin": str,           # Amazon Standard Identification Number
    "reviewerName": str,   # Name of the reviewer
    "helpful": list,       # Helpfulness rating [votes_up, votes_total]
    "reviewText": str,     # The text review
    "overall": float,      # Rating (1-5 stars)
    "summary": str,        # Review summary/title
    "unixReviewTime": int, # Review timestamp (unix)
    "reviewTime": str      # Human readable time
}
```

## Using the Scripts

### Prerequisites
```bash
pip install pandas kagglehub
```

### Setting up Kaggle Authentication
1. Create a Kaggle account if you don't have one
2. Go to 'Account' -> 'Create API Token'
3. Download and place `kaggle.json` in `~/.kaggle/`
4. Set proper permissions:
```bash
chmod 600 ~/.kaggle/kaggle.json
```

### Running `generate_reviews.py`

1. **Basic Usage**:
```bash
python3 generate_reviews.py
```

2. **Default Behavior**:
- Downloads dataset using kagglehub
- Processes both test.csv and train.csv
- Creates JSON files in `/home/guillermo_gomezmora/jsons/`
- Processes 1000 reviews from each file by default

3. **Output Files**:
```
/home/guillermo_gomezmora/jsons/
├── amazon_reviews_test.json
└── amazon_reviews_train.json
```

### Memory Considerations
- Script uses chunked processing to handle large files
- Default chunk size: 10,000 rows
- Adjust `chunksize` in script if memory issues occur

### Error Handling
- Missing fields are replaced with default values
- Progress is reported every 100 reviews
- Script maintains processing even if some fields are malformed

## Integration with Flume

The generated JSON files are formatted to work with our Flume configuration:
```properties
ReviewHDFSAgent.sources.ReviewSource.type = spooldir
ReviewHDFSAgent.sources.ReviewSource.spoolDir = /home/guillermo_gomezmora/jsons
```

### File Processing Order
1. Script generates JSON files in spooling directory
2. Flume picks up files and processes them
3. Files are moved to HDFS

## Resource Links
- [Kagglehub Documentation](https://github.com/Kaggle/kagglehub/blob/main/README.md#download-dataset)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Apache Flume Documentation](https://flume.apache.org/documentation.html)

## Troubleshooting

### Common Issues

1. **Memory Errors**
```python
# Adjust chunk size in generate_reviews.py
chunks = pd.read_csv(input_file, chunksize=5000)  # Reduce if memory issues
```

2. **Kaggle Authentication**
```bash
# Check if kaggle.json is properly set up
ls -l ~/.kaggle/kaggle.json
```

3. **File Permissions**
```bash
# Ensure proper permissions on output directory
chmod 755 /home/guillermo_gomezmora/jsons
```

## Future Enhancements

1. Add support for:
   - Custom number of reviews processing
   - Different output formats
   - Field selection
   - Data cleaning options

2. Integration with:
   - Direct HDFS writing
   - Real-time processing
   - Custom data transformations

## Contributing

Feel free to submit issues and enhancement requests!

## Notes

- Keep `kaggle.json` secure and never commit it to version control
- Monitor disk space when processing large chunks of data
- Check Flume logs for ingestion issues
