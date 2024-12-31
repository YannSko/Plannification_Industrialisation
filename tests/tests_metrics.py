from models.pulp import solve_with_pulp
from utils.utils import load_rules, load_employee_data
from utils.metrics import calculate_priority_weighted_score
def test_calculate_metrics():
    rules = load_rules("rules.yaml")
    employees = load_employee_data("data/raw/employees_60.csv")
    planning = [(day, slot) for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
                for slot in ["Morning", "Afternoon", "Evening"]]

    assignments = solve_with_pulp(employees, planning, rules)
    metrics = calculate_priority_weighted_score(assignments, employees)

    assert "Total Cost" in metrics, "Metrics should include 'Total Cost'"
    assert "Uncovered Slots" in metrics, "Metrics should include 'Uncovered Slots'"
    assert "Total Satisfaction" in metrics, "Metrics should include 'Total Satisfaction'"
