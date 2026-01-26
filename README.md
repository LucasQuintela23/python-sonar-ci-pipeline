# Python SonarCloud CI/CD Pipeline Demo

A demonstration project showcasing CI/CD integration with SonarCloud for Python code quality analysis with **multi-environment testing** (Staging & Production).

## 🚀 Quick Start (5 minutes)

### Step 1: Execute Tests
```bash
./run_tests_multi_env.sh
```
This runs 19 tests in **STAGING** and 19 tests in **PRODUCTION** environments.

### Step 2: View Results
```bash
./serve_dashboard.sh
```
Open your browser to `http://localhost:8000` and see the beautiful dashboard!

---

## Project Overview

This project simulates a simple **Credit Analysis Engine** with:
- ✅ Clean, well-documented code with type hints
- ✅ Comprehensive unit tests (19 tests per environment)
- ✅ Code coverage reporting (separate for Staging & Production)
- ✅ Multi-environment test execution
- ✅ SonarCloud configuration for continuous code quality monitoring

## 📊 Project Structure

```
.
├── src/
│   └── credit_engine.py          # Credit analysis and loan approval logic
├── tests/
│   └── test_credit_engine.py     # Unit tests with pytest (19 tests)
├── conftest.py                   # Pytest configuration with environment support
├── pytest.ini                    # Pytest settings
├── requirements.txt              # Python dependencies
├── sonar-project.properties      # SonarCloud configuration
│
├── 🎯 Main Scripts (Use These)
│   ├── run_tests_multi_env.sh    # ⭐ Execute tests (Staging + Production)
│   ├── serve_dashboard.sh        # ⭐ View dashboard
│   └── serve_combined_allure.sh  # View detailed Allure report
│
└── README.md                     # This file
```

## ✨ Features

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

## 🔧 Setup

### Prerequisites

- Python 3.8+
- pip
- Java (for Allure Report) - optional
- Node.js/npm (for Allure CLI) - optional

### Installation

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. (Optional) Install Allure CLI:
   ```bash
   npm install -g allure-commandline
   ```

## 🧪 Running Tests

### Main Script - Multi-Environment Testing (RECOMMENDED)
```bash
./run_tests_multi_env.sh
```
Executes tests in both STAGING and PRODUCTION environments, generating combined reports.

**Result:**
- ✅ 19 tests in Staging environment (PASSED)
- ✅ 19 tests in Production environment (PASSED)
- ✅ Combined coverage reports
- ✅ Unified Allure Report

### Alternative: Manual Execution
```bash
# Execute all tests (single environment)
pytest

# With coverage
pytest --cov=src --cov-report=xml --cov-report=html

# Specific test class
pytest tests/test_credit_engine.py::TestCreditAnalysisCalculateScore

# Verbose output
pytest -v
```

## 📊 Viewing Reports

### Dashboard (Visual Interface) 🎨 RECOMMENDED
```bash
./serve_dashboard.sh
```
Access: `http://localhost:8000`

Features:
- Side-by-side comparison of Staging vs Production
- Overall execution summary
- Direct links to detailed reports
- Beautiful, responsive interface

### Allure Report (Detailed) 📋
```bash
./serve_combined_allure.sh
```
Access: `http://localhost:7071`

Features:
- Interactive test dashboard
- Features and stories organization
- Severity levels and statistics
- Timeline of test execution
- Detailed test descriptions

### Coverage Reports 📈
```bash
# Staging coverage
open htmlcov-staging/index.html

# Production coverage
open htmlcov-production/index.html
```

## 📚 Documentation

| Document | Purpose |
|----------|---------|
| [MULTI_ENV_TESTING.md](MULTI_ENV_TESTING.md) | Complete multi-environment testing guide |
| [QUICK_REFERENCE.md](QUICK_REFERENCE.md) | Quick commands reference |
| [INDEX.md](INDEX.md) | Documentation index |
| [GITIGNORE_UPDATE.md](GITIGNORE_UPDATE.md) | .gitignore explanation |
| [IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md) | Implementation details |
| [FINAL_SUMMARY.md](FINAL_SUMMARY.md) | Project summary |

## 🧮 Test Coverage
