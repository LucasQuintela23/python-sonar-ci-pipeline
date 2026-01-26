#!/bin/bash

# Script para servir o relatório Allure em um servidor HTTP

SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
cd "$SCRIPT_DIR"

echo "=========================================="
echo "Allure Report Server"
echo "=========================================="
echo ""

# Verificar se allure-report existe
if [ ! -d "allure-report" ]; then
    echo "❌ Error: allure-report directory not found"
    echo "Run ./run_tests.sh first to generate the report"
    exit 1
fi

echo "Starting HTTP server for Allure Report..."
echo ""
echo "📊 Open your browser and navigate to:"
echo "   http://localhost:7071"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

# Usar allure serve se disponível
if command -v allure &> /dev/null; then
    allure open allure-report --port 7071
else
    echo "⚠️  Allure CLI not found. Using Python HTTP server instead..."
    echo "Navigate to: http://localhost:8000/allure-report/"
    echo ""
    cd "$SCRIPT_DIR"
    python3 -m http.server 8000
fi
