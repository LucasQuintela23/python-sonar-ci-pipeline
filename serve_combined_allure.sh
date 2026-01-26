#!/bin/bash

# Script para servir o relatório combinado Allure (múltiplos ambientes)

SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
cd "$SCRIPT_DIR"

echo "=========================================="
echo "Combined Allure Report Server"
echo "=========================================="
echo ""

# Verificar se allure-report-combined existe
if [ ! -d "allure-report-combined" ]; then
    echo "❌ Error: allure-report-combined directory not found"
    echo "Run ./run_tests_multi_env.sh first to generate the report"
    exit 1
fi

echo "Starting HTTP server for Combined Allure Report..."
echo ""
echo "📊 Open your browser and navigate to:"
echo "   http://localhost:7071"
echo ""
echo "This report shows test results from:"
echo "   • STAGING (Homologação)"
echo "   • PRODUCTION (Produção)"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

# Usar allure serve se disponível
if command -v allure &> /dev/null; then
    allure open allure-report-combined --port 7071
else
    echo "⚠️  Allure CLI not found. Using Python HTTP server instead..."
    echo "Navigate to: http://localhost:8000/allure-report-combined/"
    echo ""
    cd "$SCRIPT_DIR"
    python3 -m http.server 8000
fi
