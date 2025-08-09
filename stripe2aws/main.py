# from utils.config_loader import load_config
# import os

# config = load_config()

# print(config['api']['base_url'])
# print(os.getenv('AWS_ACCESS_KEY'))

from utils.config_loader import load_config
from utils.fetch_data import fetch_data
from utils.file_handler import save_json
from utils.s3_uploader import upload_to_s3

config = load_config()

# 1. Fetch
api_url = config['api']['base_url'] + config['api']['endpoint']
data = fetch_data(api_url)

# 2. Save locally
file_path = save_json(data, "data/raw/products.json")

# 3. Upload to S3
bucket_name = config['aws']['s3_bucket']
upload_to_s3(file_path, bucket_name, "products.json")
