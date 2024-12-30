# scheduler.py
import yaml
import pandas as pd
import numpy as np

import os
import json
from datetime import datetime

# Setup result logging
class Registry:
    def __init__(self, registry_dir="registry"):
        os.makedirs(registry_dir, exist_ok=True)
        self.registry_dir = registry_dir

    def log_results(self, model_name, results):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(self.registry_dir, f"{model_name}_{timestamp}.json")
        with open(filename, "w") as f:
            json.dump(results, f, indent=4)







# Main Execution
if __name__ == "__main__":
    # Load rules and employees
    rules = load_rules("rules.yaml")
    employees = load_employee_data("employees_60.csv")
    planning = [(day, slot) for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
                for slot in ["Morning", "Afternoon", "Evening"]]
    
    # Initialize registry
    registry = Registry()

    # Solve with PuLP
    pulp_assignments = solve_with_pulp(employees, planning, rules)
    pulp_results = {"model": "PuLP", "assignments": pulp_assignments}
    registry.log_results("pulp", pulp_results)

    # Solve with OR-Tools
    ortools_assignments = solve_with_ortools(employees, planning, rules)
    ortools_results = {"model": "OR-Tools", "assignments": ortools_assignments}
    registry.log_results("ortools", ortools_results)
