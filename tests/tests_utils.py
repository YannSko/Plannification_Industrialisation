import pytest
import pandas as pd
from utils.utils import load_rules , load_employee_data

# Test loading YAML rules
def test_load_rules():
    rules = load_rules("rules.yaml")
    assert "general" in rules, "General rules missing in YAML"
    assert "staffing_requirements" in rules, "Staffing requirements missing in YAML"
    assert "preferences" in rules, "Preferences missing in YAML"

    # Check some sample values
    assert rules["general"]["max_hours_per_week"] == 35, "Incorrect max hours per week"
    assert rules["preferences"]["weights"]["Morning"] == 2, "Incorrect weight for Morning"
# Test loading employee data
def test_load_employees():
    employees = load_employee_data("data/raw/employees_60.csv")
    assert not employees.empty, "Employee data should not be empty"
    assert "name" in employees.columns, "Employee data missing 'name' column"
    assert "preference" in employees.columns, "Employee data missing 'preference' column"
    assert "availability" in employees.columns, "Employee data missing 'availability' column"