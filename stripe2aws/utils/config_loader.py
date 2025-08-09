import yaml
import os
from dotenv import load_dotenv


def load_config(path="config/config.yaml"):

    load_dotenv()
    if not os.path.exists(path):
        raise FileNotFoundError(f"Configuration file not found: {path}")

    with open(path,'r') as f:
        config = yaml.safe_load(f)


    return config