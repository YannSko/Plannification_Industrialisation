from ortools.sat.python import cp_model
from .utils import calculate_preference_score
# Adjusted OR-Tools Model
def solve_with_ortools(employees, planning, rules):
    model = cp_model.CpModel()
    x = {}
    for _, row in employees.iterrows():
        for (day, slot) in planning:
            x[(row["name"], (day, slot))] = model.NewBoolVar(f"x_{row['name']}_{day}_{slot}")

    # Constraints
    for (day, slot) in planning:
        model.Add(sum(x[(row["name"], (day, slot))] for _, row in employees.iterrows()) >= rules["staffing_requirements"][slot])

    for _, row in employees.iterrows():
        model.Add(sum(x[(row["name"], (day, slot))] * 4 for (day, slot) in planning) <= rules["general"]["max_hours_per_week"])

    # Objective with Priorities
    total_satisfaction = sum(
        x[(row["name"], (day, slot))] * calculate_preference_score(slot, eval(row["preference"]), rules["preferences"]["weights"])
        for _, row in employees.iterrows() for (day, slot) in planning
    )

    total_cost = sum(
        x[(row["name"], (day, slot))] * 4 * rules["financials"]["salaries"][row["category"]]
        for _, row in employees.iterrows() for (day, slot) in planning
    )

    total_balance = sum(
        abs(sum(x[(row["name"], (day, slot))] * 4 for (day, slot) in planning) - rules["general"]["max_hours_per_week"] / 2)
        for _, row in employees.iterrows()
    )

    objectives = {
        "maximize_satisfaction": total_satisfaction,
        "minimize_cost": -total_cost,
        "balance_workload": -total_balance,
    }

    priority_scores = [
        objectives[priority] for priority in rules["objectives"]["priorities"]
    ]

    model.Maximize(sum(priority_scores))

    # Solve
    solver = cp_model.CpSolver()
    solver.Solve(model)

    # Results
    assignments = {}
    for _, row in employees.iterrows():
        assignments[row["name"]] = [
            (day, slot) for (day, slot) in planning if solver.Value(x[(row["name"], (day, slot))]) == 1
        ]
    return assignments