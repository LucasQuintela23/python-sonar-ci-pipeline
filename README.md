# Python SonarCloud CI/CD Pipeline Demo

A demonstration project showcasing CI/CD integration with SonarCloud for Python code quality analysis.

## Project Overview

This project simulates a simple **Credit Analysis Engine** with:
- Clean, well-documented code with type hints
- Comprehensive unit tests using pytest
- Code coverage reporting
- SonarCloud configuration for continuous code quality monitoring

## Project Structure

```
.
├── src/
│   └── credit_engine.py          # Credit analysis and loan approval logic
├── tests/
│   └── test_credit_engine.py     # Unit tests with pytest
├── requirements.txt              # Python dependencies
├── sonar-project.properties      # SonarCloud configuration
└── README.md                     # This file
```

## Features

### Credit Engine (src/credit_engine.py)

The `CreditAnalysis` class provides:

1. **calculate_score(income, debt) → int**
   - Calculates a credit score based on income and debt
   - Returns a score between 0 and 1000
   - Formula: (income - debt) × 2, capped at 1000

2. **approve_loan(score, amount) → bool**
   - Approves loans if score > 600 AND amount < 50,000
   - Validates input parameters

3. **legacy_calculation()** (intentionally complex)
   - Demonstrates poor code practices with nested conditionals
   - Used to showcase SonarCloud's detection of cognitive complexity issues

## Setup

### Prerequisites

- Python 3.8+
- pip
- Java (for Allure Report) - optional but recommended
- Node.js/npm (for Allure CLI) - optional but recommended

### Installation

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. (Optional) Install Allure CLI for enhanced reporting:
   ```bash
   npm install -g allure-commandline
   ```
   Or use the convenience script:
   ```bash
   ./run_tests.sh
   ```

## Running Tests

### Quick start with automated script:
```bash
./run_tests.sh
```

### Manual execution

#### Execute all tests:
```bash
pytest
```

#### Run tests with coverage report:
```bash
pytest --cov=src --cov-report=xml --cov-report=html
```

#### Run specific test class:
```bash
pytest tests/test_credit_engine.py::TestCreditAnalysisCalculateScore
```

#### Run with verbose output:
```bash
pytest -v
```

## Allure Report

### Generate Allure Report
```bash
pytest
allure generate allure-results -o allure-report --clean
```

### View Allure Report
```bash
allure open allure-report
```

This generates an interactive, visually appealing test report with:
- ✅ Test results overview
- 📊 Features and stories organization
- 🎯 Severity levels (CRITICAL, NORMAL)
- 📈 Timeline and statistics
- 📝 Detailed test descriptions

## Code Quality Analysis

### Generate Coverage Report
```bash
pytest --cov=src --cov-report=xml --cov-report=html
```

This generates:
- `coverage.xml` - Machine-readable report (used by SonarCloud)
- `htmlcov/index.html` - Human-readable HTML report

### Generate Allure Report
```bash
pytest
allure generate allure-results -o allure-report --clean
allure open allure-report
```

This generates an interactive, visually appealing test report with:
- ✅ Test results overview (Overview, Suites, Graphs)
- 📊 Features and stories organization (hierarchical view)
- 🎯 Severity levels (CRITICAL, NORMAL)
- 📈 Timeline and execution statistics
- 📝 Detailed test descriptions and steps

### SonarCloud Configuration

The `sonar-project.properties` file configures:
- Source directory: `src/`
- Tests directory: `tests/`
- Coverage report: `coverage.xml`

### What SonarCloud Will Find

1. **Code Smells**: The `legacy_calculation()` method has high cognitive complexity
2. **Coverage Gaps**: The `legacy_calculation()` method is intentionally not covered by tests
3. **Best Practices**: Well-documented code and proper type hints in main methods

## Usage Example

```python
from src.credit_engine import CreditAnalysis

# Create analyzer
analyzer = CreditAnalysis()

# Calculate credit score
score = analyzer.calculate_score(income=60000, debt=10000)
print(f"Credit Score: {score}")  # Output: 100000 (capped at 1000)

# Approve loan
approved = analyzer.approve_loan(score=700, amount=30000)
print(f"Loan Approved: {approved}")  # Output: Loan Approved: True
```

## CI/CD Integration

### SonarCloud Setup

1. **Create SonarCloud Account:**
   - Visit: https://sonarcloud.io/
   - Sign up with GitHub/GitLab/Bitbucket

2. **Generate Authentication Token:**
   - Go to: https://sonarcloud.io/account/security/
   - Create new token and copy it

3. **Run Local Analysis (Optional):**
   ```bash
   # Install SonarScanner
   npm install -g sonarqube-scanner
   
   # Generate coverage report
   pytest --cov=src --cov-report=xml
   
   # Run analysis
   ./analyze_with_sonar.sh YOUR_TOKEN
   ```

4. **GitHub Actions Setup:**
   - Push code to GitHub
   - Go to: Settings → Secrets and variables → Actions
   - Add `SONAR_TOKEN` secret (your SonarCloud token)
   - Workflow in `.github/workflows/sonar.yml` will run automatically

5. **View Results:**
   - Dashboard: https://sonarcloud.io/dashboard
   - See code quality metrics, coverage, and issues

For detailed setup instructions, see [SONAR_SETUP.md](SONAR_SETUP.md)

## Test Coverage

Current test coverage includes:

- ✅ `calculate_score()`: All scenarios (positive, negative, edge cases)
- ✅ `approve_loan()`: All conditions (approved, rejected, boundary cases)
- ✅ Integration tests: End-to-end workflows
- ❌ `legacy_calculation()`: Intentionally NOT tested (to show coverage gaps)

## License

MIT
