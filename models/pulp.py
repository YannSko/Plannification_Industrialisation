from pulp import LpProblem, LpVariable, LpMaximize, lpSum, PULP_CBC_CMD
from .utils import calculate_priority_weighted_score
# Adjusted PuLP Model
def solve_with_pulp(employees, planning, rules):
    model = LpProblem("Employee_Scheduling_PuLP", LpMaximize)
    x = LpVariable.dicts(
        "schedule", [(row["name"], (day, slot)) for _, row in employees.iterrows() for (day, slot) in planning],
        cat="Binary"
    )

    # Objective Function with Priorities
    model += calculate_priority_weighted_score(employees, planning, rules, x)

    # Constraints
    for (day, slot) in planning:
        model += lpSum(x[(row["name"], (day, slot))] for _, row in employees.iterrows()) >= rules["staffing_requirements"][slot], f"Coverage_{day}_{slot}"

    for _, row in employees.iterrows():
        model += lpSum(x[(row["name"], (day, slot))] * 4 for (day, slot) in planning) <= rules["general"]["max_hours_per_week"], f"Max_Hours_{row['name']}"

    # Solve
    model.solve(PULP_CBC_CMD(msg=False))

    # Results
    assignments = {}
    for _, row in employees.iterrows():
        assignments[row["name"]] = [
            (day, slot) for (day, slot) in planning if x[(row["name"], (day, slot))].value() == 1
        ]
    return assignments