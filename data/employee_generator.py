import pandas as pd
import numpy as np
import random

# === Génération des données pour 60 employés ===
def generate_employees(n=60, seed=42):
    np.random.seed(seed)
    random.seed(seed)

    categories = ["Mother", "Senior", "Graduate", "PartTime", "FullTime"]
    salaries = {"Mother": 15, "Senior": 16, "Graduate": 13, "PartTime": 12, "FullTime": 14}
    preferences = [["Morning"], ["Afternoon"], ["No Evening"], ["Weekend"]]
    
    employees = []
    for i in range(n):
        category = random.choice(categories)
        employee = {
            "ID": f"E{i+1}",
            "Name": f"Employee_{i+1}",
            "Category": category,
            "Availability": ",".join(random.sample(
                ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
                k=random.choice([3, 4, 5, 6, 7])
            )),
            "Preference": random.choice(preferences)[0],
            "Salary": salaries[category]
        }
        employees.append(employee)
    
    return pd.DataFrame(employees)

# Génération des employés et exportation en CSV
df_employees = generate_employees()
df_employees.to_csv("employees_60.csv", index=False)
print("Fichier 'employees_60.csv' généré avec succès.")

# Génération de 60 nouveaux employés
def generate_additional_employees(n=60, existing_df=None, seed=43):
    np.random.seed(seed)
    random.seed(seed)

    categories = ["Mother", "Senior", "Graduate", "PartTime", "FullTime"]
    salaries = {"Mother": 15, "Senior": 16, "Graduate": 13, "PartTime": 12, "FullTime": 14}
    preferences = [["Morning"], ["Afternoon"], ["No Evening"], ["Weekend"]]
    
    employees = []
    start_id = len(existing_df) + 1 if existing_df is not None else 1
    for i in range(n):
        category = random.choice(categories)
        employee = {
            "ID": f"E{start_id + i}",
            "Name": f"Employee_{start_id + i}",
            "Category": category,
            "Availability": ",".join(random.sample(
                ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
                k=random.choice([3, 4, 5, 6, 7])
            )),
            "Preference": random.choice(preferences)[0],
            "Salary": salaries[category]
        }
        employees.append(employee)
    
    return pd.DataFrame(employees)

# Lecture des 60 employés existants
existing_employees = pd.read_csv("employees_60.csv")

# Génération des nouveaux employés
additional_employees = generate_additional_employees(n=60, existing_df=existing_employees)

# Fusion des données existantes et nouvelles
all_employees = pd.concat([existing_employees, additional_employees], ignore_index=True)

# Exportation en CSV
all_employees.to_csv("employees_120.csv", index=False)
print("Fichier 'employees_120.csv' généré avec succès.")
