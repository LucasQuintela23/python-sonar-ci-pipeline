#!/bin/bash

# Script para executar testes em múltiplos ambientes (Homologação e Produção)

set -e

SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
cd "$SCRIPT_DIR"

echo "=========================================="
echo "Multi-Environment Test Execution"
echo "=========================================="
echo ""

# Cores para output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Criar ou ativar ambiente virtual
PYTHON_BIN=""
if command -v python3 >/dev/null 2>&1; then
  PYTHON_BIN="python3"
elif command -v python >/dev/null 2>&1; then
  PYTHON_BIN="python"
else
  echo "❌ Python não encontrado no PATH"
  exit 127
fi

if [ ! -d "venv" ]; then
  echo "Creating virtual environment..."
  "$PYTHON_BIN" -m venv venv
fi

source venv/bin/activate

# Instalar dependências
echo "Installing dependencies..."
pip install -q -r requirements.txt

# Criar diretório para relatórios combinados
COMBINED_RESULTS="allure-results-combined"
rm -rf "$COMBINED_RESULTS"
mkdir -p "$COMBINED_RESULTS"

# ============================================
# AMBIENTE 1: HOMOLOGAÇÃO
# ============================================

echo ""
echo -e "${BLUE}=========================================="
echo "ENVIRONMENT 1: STAGING (Homologação)"
echo "==========================================${NC}"
echo ""

# Limpar resultados anteriores
rm -rf allure-results htmlcov coverage.xml .pytest_cache

# Variáveis de ambiente
export TEST_ENVIRONMENT="staging"

# Executar testes
echo "Running tests in STAGING environment..."
pytest \
  -v \
  -m "not production" \
  --tb=short \
  --alluredir=allure-results \
  --cov=src \
  --cov-report=xml \
  --cov-report=html:htmlcov-staging \
  --cov-report=term-missing

# Copiar resultados para diretório combinado
cp -r allure-results/* "$COMBINED_RESULTS/" 2>/dev/null || true

echo -e "${GREEN}✅ STAGING tests completed!${NC}"
echo ""

# ============================================
# AMBIENTE 2: PRODUÇÃO
# ============================================

echo -e "${BLUE}=========================================="
echo "ENVIRONMENT 2: PRODUCTION (Produção)"
echo "==========================================${NC}"
echo ""

# Limpar resultados anteriores
rm -rf allure-results htmlcov coverage.xml .pytest_cache

# Variáveis de ambiente
export TEST_ENVIRONMENT="production"

# Executar testes
echo "Running tests in PRODUCTION environment..."
pytest \
  -v \
  -m "not staging" \
  --tb=short \
  --alluredir=allure-results \
  --cov=src \
  --cov-report=xml \
  --cov-report=html:htmlcov-production \
  --cov-report=term-missing

# Copiar resultados para diretório combinado
cp -r allure-results/* "$COMBINED_RESULTS/" 2>/dev/null || true

echo -e "${GREEN}✅ PRODUCTION tests completed!${NC}"
echo ""

# ============================================
# GERAR RELATÓRIO COMBINADO
# ============================================

echo -e "${BLUE}=========================================="
echo "Generating Combined Allure Report"
echo "==========================================${NC}"
echo ""

# Gerar relatório Allure combinado
if command -v allure &> /dev/null; then
  allure generate "$COMBINED_RESULTS" -o allure-report-combined --clean
  echo -e "${GREEN}✅ Reports generated successfully!${NC}"
else
  echo "⚠️  Allure CLI not found - skipping combined report generation"
  echo "To generate reports locally, install Allure CLI: https://docs.qameta.io/allure/"
fi

echo ""

# ============================================
# RESUMO FINAL
# ============================================

echo -e "${YELLOW}=========================================="
echo "EXECUTION SUMMARY"
echo "==========================================${NC}"
echo ""
echo -e "${GREEN}✅ Both environments completed successfully!${NC}"
echo ""
echo "📊 Reports Available:"
echo "   • Staging Coverage:     htmlcov-staging/index.html"
echo "   • Production Coverage:  htmlcov-production/index.html"
echo "   • Combined Allure:      allure-report-combined/index.html"
echo ""
echo "🚀 To view combined Allure report, run:"
echo "   ./serve_combined_allure.sh"
echo ""
echo "Or use these commands directly:"
echo "   • allure open allure-report-combined"
echo "   • python3 -m http.server 8000 (then visit http://localhost:8000/allure-report-combined)"
echo ""
