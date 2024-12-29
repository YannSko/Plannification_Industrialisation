import yaml

def load_rules(yaml_file):
    with open(yaml_file, 'r') as file:
        rules = yaml.safe_load(file)
    return rules