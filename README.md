PLANNIFICATION INDUSTRIALISATION

Context:

An after-sales service company asked me to carry out their operational optimization in order to meet the requests and optimize their budget. The objective is to generate the most profit as well as employee/customer satisfaction.

We managed to optimize costs by 10% and overall satisfaction by 18%

Overview
This project focuses on automating employee scheduling using optimization techniques. It utilizes linear programming (PuLP) and constraint programming (OR-Tools) to create efficient schedules based on configurable rules and employee preferences. The application is designed to handle large datasets and provides metrics to evaluate model performance and fairness.

Features
Dynamic Scheduling Models:
Linear Programming (PuLP).
Constraint Programming (OR-Tools).
Configurable Rules: Easily modify constraints and priorities via rules.yaml.
Employee Management:
Generate employee datasets with preferences, salaries, and availability.
Supports datasets of varying sizes (e.g., 60, 120 employees).
Metrics Tracking:
Total scheduling cost.
Employee satisfaction scores.
Uncovered slots.
Workload distribution (mean and standard deviation).
Visualization:
Workload distribution plots.
Comparative satisfaction scores between models.
CI/CD Integration:
Automated testing with pytest and GitHub Actions.
Containerized deployment using Docker.
Project Structure
plaintext
Copier le code
PLANNIFICATION_INDUSTRIALISATION/
│
├── data/                    # Data folder
│   ├── raw/                 # Raw employee data
│   │   ├── employees_60.csv
│   │   ├── employees_120.csv
│   │
│   ├── processed/           # Processed or intermediate datasets
│
├── models/                  # Optimization models
│   ├── __init__.py
│   ├── pulp.py              # PuLP model implementation
│   ├── ortools.py           # OR-Tools model implementation
│
├── rules/                   # Rule definitions
│   ├── __init__.py
│   ├── rules.yaml           # Configurable rules
│
├── utils/                   # Utility functions
│   ├── __init__.py
│   ├── metrics.py           # Metrics calculation
│   ├── utils.py             # Helpers for logging, YAML parsing, etc.
│
├── tests/                   # Unit and integration tests
│   ├── test_scheduler.py    # Tests for scheduler.py
│   ├── test_pulp.py         # Tests for PuLP model
│   ├── test_ortools.py      # Tests for OR-Tools model
│   ├── test_metrics.py      # Tests for metrics calculation
│   ├── ...
│
├── scheduler.py             # Main script to run models and log results
├── employee_generator.py    # Script to generate employee data
├── README.md                # Project documentation
├── requirements.txt         # Python dependencies
├── LICENSE                  # Project license
├── .gitignore               # Files to ignore in git
├── .github/                 # GitHub Actions for CI/CD
│   └── workflows/
│       └── ci.yml           # CI pipeline for testing
└── Dockerfile               # Dockerfile for containerization
Setup
1. Clone the Repository
bash
Copier le code
git clone https://github.com/your-username/plannification_industrialisation.git
cd plannification_industrialisation
2. Install Dependencies
bash
Copier le code
pip install -r requirements.txt
3. Generate Employee Data
Use the employee_generator.py script to generate employee datasets:

bash
Copier le code
python employee_generator.py --output data/raw/employees_60.csv --size 60
python employee_generator.py --output data/raw/employees_120.csv --size 120
4. Configure Rules
Edit rules/rules.yaml to modify scheduling constraints and priorities.

Usage
1. Run the Scheduler
The scheduler.py script runs both the PuLP and OR-Tools models:

bash
Copier le code
python scheduler.py
2. View Results
Results are logged in the registry/ directory as JSON files. Example:

plaintext
Copier le code
registry/pulp_20240101_120000.json
registry/ortools_20240101_120000.json
3. Metrics Visualization
Metrics such as workload distribution and satisfaction scores are visualized as plots.

Testing
Run Unit and Integration Tests
bash
Copier le code
pytest --cov=.
Test coverage is provided via pytest-cov. Ensure all tests pass before deployment.

Docker Deployment
1. Build the Docker Image
bash
Copier le code
docker build -t scheduling-app .
2. Run the Container
bash
Copier le code
docker run -v $(pwd)/data:/app/data scheduling-app
3. Push to DockerHub (Optional)
bash
Copier le code
docker tag scheduling-app your-dockerhub-username/scheduling-app:latest
docker push your-dockerhub-username/scheduling-app:latest
Continuous Integration
The project uses GitHub Actions for CI/CD. The pipeline runs:

Dependency installation.
Code linting.
Unit and integration tests.
The configuration file is located in .github/workflows/ci.yml.

Customization
Modify Rules
The rules.yaml file contains configurable parameters:

yaml
Copier le code
objectives:
  priorities:
    - maximize_satisfaction
    - minimize_cost
    - balance_workload

preferences:
  weights:
    Morning: 2
    Afternoon: 1
    Evening: -1

staffing_requirements:
  Morning: 10
  Afternoon: 8
  Evening: 5

general:
  max_hours_per_week: 35
  min_days_off_per_week: 1
Future Improvements
Scalability:
Adapt the models for larger datasets (e.g., 500+ employees).
Parallelize model solving to reduce computation time.
Advanced Metrics:
Include metrics for resilience against absences.
Web Interface:
Build a simple UI for editing rules and viewing results.
API Integration:
Expose scheduling functionality via a RESTful API.
License
This project is licensed under the MIT License. See LICENSE for details.

Acknowledgments
Special thanks to the creators of:

PuLP for linear programming.
OR-Tools for constraint programming.
The Python ecosystem for providing robust tools for data handling and optimization.