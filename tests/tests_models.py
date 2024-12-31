from models.ortools import solve_with_ortools
from models.pulp import solve_with_pulp
from utils.utils import load_rules, load_employee_data

def test_solve_with_pulp():
    rules = load_rules("rules.yaml")
    employees = load_employee_data("data/raw/employees_60.csv")
    planning = [(day, slot) for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
                for slot in ["Morning", "Afternoon", "Evening"]]

    assignments = solve_with_pulp(employees, planning, rules)
    assert assignments, "PuLP assignments should not be empty"

def test_solve_with_ortools():
    rules = load_rules("rules.yaml")
    employees = load_employee_data("data/raw/employees_60.csv")
    planning = [(day, slot) for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
                for slot in ["Morning", "Afternoon", "Evening"]]

    assignments = solve_with_ortools(employees, planning, rules)
    assert assignments, "OR-Tools assignments should not be empty"
