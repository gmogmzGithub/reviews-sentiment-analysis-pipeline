import pandas as pd
import json
from datetime import datetime
import os

def process_reviews_to_json(input_file, output_file, num_reviews=1000):
    """
    Process Amazon reviews from CSV to JSON format
    
    Args:
        input_file: Path to the CSV file
        output_file: Path to output JSON file
        num_reviews: Number of reviews to process (default 1000)
    """
    print(f"Reading {input_file}...")
    
    chunks = pd.read_csv(input_file, 
                        chunksize=10000,  # Process 10000 rows at a time
                        nrows=num_reviews)
    
    count = 0
    with open(output_file, 'w') as f:
        for chunk in chunks:
            for _, row in chunk.iterrows():
                if count >= num_reviews:
                    break
                    
                # Create review object
                review = {
                    "reviewerID": str(row.get('reviewerID', f'user_{count}')),
                    "asin": str(row.get('asin', f'product_{count}')),
                    "reviewerName": str(row.get('reviewerName', 'Anonymous')),
                    "helpful": [
                        int(row.get('helpful', [0, 0])[0]) if isinstance(row.get('helpful'), list) else 0,
                        int(row.get('helpful', [0, 0])[1]) if isinstance(row.get('helpful'), list) else 0
                    ],
                    "reviewText": str(row.get('reviewText', '')),
                    "overall": float(row.get('overall', 0)),
                    "summary": str(row.get('summary', '')),
                    "unixReviewTime": int(row.get('unixReviewTime', datetime.now().timestamp())),
                    "reviewTime": str(row.get('reviewTime', datetime.now().strftime("%m %d, %Y")))
                }
                
                # Write review as JSON line
                f.write(json.dumps(review) + '\n')
                count += 1
                
                if count % 100 == 0:
                    print(f"Processed {count} reviews...")
                    
            if count >= num_reviews:
                break
    
    print(f"Successfully processed {count} reviews to {output_file}")

def main():
    # Download dataset using kagglehub
    import kagglehub
    dataset_path = kagglehub.dataset_download("kritanjalijain/amazon-reviews")
    
    # Process both test and train files
    input_files = ['test.csv', 'train.csv']
    
    for input_file in input_files:
        # Construct full input path
        full_input_path = os.path.join(dataset_path, input_file)
        
        # Construct output path
        output_file = f'/home/guillermo_gomezmora/jsons/amazon_reviews_{input_file.split(".")[0]}.json'
        
        # Process reviews
        process_reviews_to_json(full_input_path, output_file, num_reviews=1000)

if __name__ == "__main__":
    main()