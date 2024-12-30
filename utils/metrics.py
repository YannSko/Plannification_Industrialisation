from pulp import LpProblem, LpVariable, LpMaximize, lpSum, PULP_CBC_CMD
from ortools.sat.python import cp_model

# Calculate preference scores
def calculate_preference_score(slot, preferences, weights):
    return weights.get(slot, 0) if slot not in preferences else -1

# Adjusted calculate_priority_weighted_score
def calculate_priority_weighted_score(employees, planning, rules, x):
    total_satisfaction = lpSum(
        x[(row["name"], (day, slot))] * calculate_preference_score(slot, eval(row["preference"]), rules["preferences"]["weights"])
        for _, row in employees.iterrows() for (day, slot) in planning
    )

    total_cost = lpSum(
        x[(row["name"], (day, slot))] * 4 * rules["financials"]["salaries"][row["category"]]
        for _, row in employees.iterrows() for (day, slot) in planning
    )

    total_balance = lpSum(
        abs(lpSum(x[(row["name"], (day, slot))] * 4 for (day, slot) in planning) - rules["general"]["max_hours_per_week"] / 2)
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

    return lpSum(priority_scores)