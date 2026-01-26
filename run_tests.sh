#!/bin/bash

# Script para executar testes com coverage e gerar relatório Allure

set -e

SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
cd "$SCRIPT_DIR"

echo "=========================================="
echo "Python SonarCloud CI/CD Pipeline - Test Suite"
echo "=========================================="
echo ""

# Ativar ambiente virtual
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

source venv/bin/activate

# Instalar dependências
echo "Installing dependencies..."
pip install -q -r requirements.txt

# Limpar relatórios anteriores
echo "Cleaning previous reports..."
rm -rf allure-results htmlcov coverage.xml .pytest_cache

# Rodar testes
echo ""
echo "Running tests..."
pytest -v

# Gerar relatório Allure
echo ""
echo "Generating Allure report..."
allure generate allure-results -o allure-report --clean

echo ""
echo "=========================================="
echo "✅ Tests completed successfully!"
echo "=========================================="
echo ""
echo "📊 Reports generated:"
echo "   - Coverage Report: htmlcov/index.html"
echo "   - Allure Report: allure-report/index.html"
echo ""
echo "🚀 To view the Allure report, run:"
echo "   ./serve_allure.sh"
echo ""
echo "Or use these commands directly:"
echo "   • With Allure CLI:  allure open allure-report"
echo "   • With Python:      python3 -m http.server 8000 (then visit http://localhost:8000/allure-report)"
echo ""
