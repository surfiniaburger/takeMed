# config_loader.py
import yaml

class Config:
    def __init__(self, data):
        self.data = data

def load_config_from_file(file_path):
    with open(file_path, 'r') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
    return Config(data)
