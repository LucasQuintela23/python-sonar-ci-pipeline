#!/bin/bash

# Script para executar análise SonarCloud
# Uso: ./analyze_with_sonar.sh YOUR_SONAR_TOKEN

set -e

if [ -z "$1" ]; then
    echo "❌ Erro: Token SonarCloud não fornecido"
    echo ""
    echo "Uso: ./analyze_with_sonar.sh YOUR_TOKEN"
    echo ""
    echo "Para obter seu token:"
    echo "  1. Acesse: https://sonarcloud.io/account/security/"
    echo "  2. Gere um novo token"
    echo "  3. Use-o como argumento"
    echo ""
    exit 1
fi

SONAR_TOKEN=$1
SONAR_HOST="https://sonarcloud.io"
PROJECT_KEY="python-sonar-ci-pipeline"

echo "=========================================="
echo "SonarCloud Analysis"
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

# Gerar relatório de cobertura
echo "Generating coverage report..."
pytest --cov=src --cov-report=xml --cov-report=html -q

# Executar análise SonarCloud
echo ""
echo "Running SonarCloud analysis..."
sonar-scanner \
  -Dsonar.projectBaseDir=. \
  -Dsonar.host.url=$SONAR_HOST \
  -Dsonar.login=$SONAR_TOKEN

echo ""
echo "=========================================="
echo "✅ Analysis completed!"
echo "=========================================="
echo ""
echo "View results at:"
echo "  🌐 https://sonarcloud.io/dashboard?id=$PROJECT_KEY"
echo ""
