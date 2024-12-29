import yaml
import pandas as pd

def load_rules(yaml_file):
    with open(yaml_file, 'r') as file:
        rules = yaml.safe_load(file)
    return rules

# Load employee data
def load_employee_data(file_path):
    return pd.read_csv(file_path)