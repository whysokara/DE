import yaml

with open('config/config.yaml',"r") as f:
    config = yaml.safe_load(f)

api_url = config["api"]["base_url"]
print(f"API URL: {api_url}")