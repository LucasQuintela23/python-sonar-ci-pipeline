#!/bin/bash

# Script de Setup - SonarScanner Instalado
# Criado: 22 de Janeiro de 2026

echo ""
echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║        ✅ SONARSCANNER INSTALADO COM SUCESSO                 ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo ""

# Verificar instalação
echo "📊 Informações da Instalação:"
echo "   Local: $(which sonar-scanner)"
echo "   Versão: $(sonar-scanner --version)"
echo ""

# Próximos passos
echo "🎯 Próximos Passos para Usar SonarCloud:"
echo ""
echo "1️⃣  Criar Token no SonarCloud:"
echo "   → Acesse: https://sonarcloud.io/account/security/"
echo "   → Gere um novo token"
echo "   → Copie o token"
echo ""
echo "2️⃣  Gerar Relatório de Cobertura:"
echo "   $ cd /home/quintela/projetos/python-sonar-ci-pipeline"
echo "   $ pytest --cov=src --cov-report=xml"
echo ""
echo "3️⃣  Executar Análise SonarCloud:"
echo "   $ sonar-scanner \\"
echo "     -Dsonar.projectBaseDir=. \\"
echo "     -Dsonar.host.url=https://sonarcloud.io \\"
echo "     -Dsonar.login=SEU_TOKEN_AQUI"
echo ""
echo "4️⃣  Ou Usar o Script Automatizado:"
echo "   $ ./analyze_with_sonar.sh SEU_TOKEN_AQUI"
echo ""
echo "5️⃣  Ver Resultados:"
echo "   → Dashboard: https://sonarcloud.io/dashboard"
echo ""

# Teste rápido
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "🧪 Teste Rápido - Ajuda do SonarScanner:"
echo ""
sonar-scanner --help | head -30
echo ""
echo "... (use 'sonar-scanner --help' para ver mais)"
echo ""

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "✨ SonarScanner está pronto para usar!"
echo ""
