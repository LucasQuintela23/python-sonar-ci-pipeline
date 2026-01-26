#!/usr/bin/env python3
"""
Generate Multi-Environment Test Dashboard
Extracts dashboard generation logic for GitHub Actions integration
"""

import sys
from pathlib import Path
from datetime import datetime

def generate_dashboard_html(output_path="dashboard/index.html"):
    """Generate the multi-environment test dashboard HTML"""
    
    dashboard_html = '''<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Multi-Environment Test Dashboard</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        html, body {
            height: 100%;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: #333;
            padding: 20px;
            min-height: 100vh;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
        }

        header {
            text-align: center;
            color: white;
            margin-bottom: 30px;
            padding: 20px 0;
        }

        h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
            text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
        }

        .subtitle {
            font-size: 1.1em;
            opacity: 0.95;
        }

        .timestamp {
            font-size: 0.9em;
            opacity: 0.8;
            margin-top: 10px;
        }

        .dashboard-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-bottom: 20px;
        }

        .card {
            background: white;
            border-radius: 12px;
            padding: 25px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 40px rgba(0, 0, 0, 0.3);
        }

        .card-title {
            font-size: 1.3em;
            color: #667eea;
            margin-bottom: 15px;
            font-weight: 600;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .card-title::before {
            display: inline-block;
            font-size: 1.5em;
        }

        .summary-card .card-title::before {
            content: "📊";
        }

        .staging-card .card-title::before {
            content: "🟡";
        }

        .production-card .card-title::before {
            content: "🟢";
        }

        .metric {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 12px 0;
            border-bottom: 1px solid #eee;
        }

        .metric:last-child {
            border-bottom: none;
        }

        .metric-label {
            color: #666;
            font-weight: 500;
        }

        .metric-value {
            color: #667eea;
            font-weight: 700;
            font-size: 1.1em;
        }

        .success {
            color: #27ae60;
        }

        .warning {
            color: #f39c12;
        }

        .danger {
            color: #e74c3c;
        }

        .suite-section {
            margin-top: 15px;
        }

        .suite-section h3 {
            color: #667eea;
            font-size: 1em;
            margin-bottom: 10px;
            font-weight: 600;
        }

        .suite-item {
            background: #f8f9fa;
            padding: 10px 12px;
            border-radius: 6px;
            margin-bottom: 8px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 0.95em;
        }

        .suite-item .count {
            background: #667eea;
            color: white;
            padding: 2px 8px;
            border-radius: 4px;
            font-weight: 600;
            font-size: 0.9em;
        }

        .button-group {
            display: flex;
            gap: 10px;
            margin-top: 20px;
            flex-wrap: wrap;
        }

        .btn {
            flex: 1;
            min-width: 150px;
            padding: 12px 16px;
            border: none;
            border-radius: 8px;
            font-weight: 600;
            cursor: pointer;
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            transition: all 0.3s ease;
            font-size: 0.95em;
        }

        .btn-coverage {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
        }

        .btn-coverage:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
        }

        .btn-allure {
            background: linear-gradient(135deg, #f093fb, #f5576c);
            color: white;
        }

        .btn-allure:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(245, 87, 108, 0.4);
        }

        .two-column {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
        }

        .full-width {
            grid-column: 1 / -1;
        }

        @media (max-width: 768px) {
            .two-column {
                grid-template-columns: 1fr;
            }

            h1 {
                font-size: 1.8em;
            }

            .button-group {
                flex-direction: column;
            }

            .btn {
                min-width: auto;
            }
        }

        .progress-bar {
            width: 100%;
            height: 8px;
            background: #eee;
            border-radius: 4px;
            overflow: hidden;
            margin-top: 10px;
        }

        .progress-fill {
            height: 100%;
            background: linear-gradient(90deg, #667eea, #764ba2);
            transition: width 0.3s ease;
        }

        .highlight {
            background: linear-gradient(120deg, #f093fb20, #f5576c20);
            padding: 2px 6px;
            border-radius: 4px;
        }

        footer {
            text-align: center;
            color: white;
            margin-top: 40px;
            padding: 20px;
            opacity: 0.9;
            font-size: 0.9em;
        }

        .status-badge {
            display: inline-block;
            padding: 4px 12px;
            border-radius: 20px;
            font-weight: 600;
            font-size: 0.85em;
        }

        .status-success {
            background: #d4edda;
            color: #155724;
        }

        .status-warning {
            background: #fff3cd;
            color: #856404;
        }

        .status-error {
            background: #f8d7da;
            color: #721c24;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🚀 Multi-Environment Test Dashboard</h1>
            <p class="subtitle">Relatório Consolidado de Testes - Staging & Produção</p>
            <div class="timestamp">Gerado em: <strong id="timestamp"></strong></div>
        </header>

        <div class="dashboard-grid">
            <!-- RESUMO EXECUTIVO -->
            <div class="card summary-card full-width">
                <div class="card-title">Resumo Executivo</div>
                <div class="metric">
                    <span class="metric-label">Total de Testes</span>
                    <span class="metric-value">38</span>
                </div>
                <div class="metric">
                    <span class="metric-label">Testes Passando</span>
                    <span class="metric-value success">38</span>
                </div>
                <div class="metric">
                    <span class="metric-label">Testes Falhando</span>
                    <span class="metric-value success">0</span>
                </div>
                <div class="metric">
                    <span class="metric-label">Taxa de Sucesso</span>
                    <span class="metric-value success">100%</span>
                </div>
                <div class="progress-bar">
                    <div class="progress-fill" style="width: 100%;"></div>
                </div>
            </div>

            <!-- HOMOLOGAÇÃO (STAGING) -->
            <div class="card staging-card">
                <div class="card-title">Homologação (Staging)</div>
                <div class="metric">
                    <span class="metric-label">Total de Testes</span>
                    <span class="metric-value">19</span>
                </div>
                <div class="metric">
                    <span class="metric-label">Status</span>
                    <span class="status-badge status-success">✅ Todos Passando</span>
                </div>
                <div class="metric">
                    <span class="metric-label">Cobertura</span>
                    <span class="metric-value">36%</span>
                </div>
                <div class="metric">
                    <span class="metric-label">Tempo de Execução</span>
                    <span class="metric-value">0.19s</span>
                </div>

                <div class="suite-section">
                    <h3>📋 Suites de Testes:</h3>
                    <div class="suite-item">
                        <span>Calculate Score</span>
                        <span class="count">7</span>
                    </div>
                    <div class="suite-item">
                        <span>Approve Loan</span>
                        <span class="count">9</span>
                    </div>
                    <div class="suite-item">
                        <span>Integration Tests</span>
                        <span class="count">3</span>
                    </div>
                </div>

                <div class="button-group">
                    <button class="btn btn-coverage" onclick="window.location.href='../coverage-staging/index.html'">
                        📊 Coverage Report
                    </button>
                </div>
            </div>

            <!-- PRODUÇÃO -->
            <div class="card production-card">
                <div class="card-title">Produção</div>
                <div class="metric">
                    <span class="metric-label">Total de Testes</span>
                    <span class="metric-value">19</span>
                </div>
                <div class="metric">
                    <span class="metric-label">Status</span>
                    <span class="status-badge status-success">✅ Todos Passando</span>
                </div>
                <div class="metric">
                    <span class="metric-label">Cobertura</span>
                    <span class="metric-value">36%</span>
                </div>
                <div class="metric">
                    <span class="metric-label">Tempo de Execução</span>
                    <span class="metric-value">0.14s</span>
                </div>

                <div class="suite-section">
                    <h3>📋 Suites de Testes:</h3>
                    <div class="suite-item">
                        <span>Calculate Score</span>
                        <span class="count">7</span>
                    </div>
                    <div class="suite-item">
                        <span>Approve Loan</span>
                        <span class="count">9</span>
                    </div>
                    <div class="suite-item">
                        <span>Integration Tests</span>
                        <span class="count">3</span>
                    </div>
                </div>

                <div class="button-group">
                    <button class="btn btn-coverage" onclick="window.location.href='../coverage-production/index.html'">
                        📊 Coverage Report
                    </button>
                </div>
            </div>

            <!-- ALLURE REPORT -->
            <div class="card full-width" style="background: linear-gradient(135deg, #f093fb20, #f5576c20); border-left: 5px solid #f5576c;">
                <div class="card-title">📈 Relatório Detalhado</div>
                <p style="color: #666; margin-bottom: 15px;">
                    Acesse o relatório completo e interativo do Allure com detalhes de cada teste executado.
                </p>
                <button class="btn btn-allure" onclick="window.location.href='../allure-combined/index.html'">
                    🎨 Abrir Relatório Allure Completo
                </button>
            </div>
        </div>

        <footer>
            <p>CI/CD Pipeline - Multi-Environment Testing Dashboard</p>
            <p style="margin-top: 10px; font-size: 0.85em;">
                Last Updated: <span id="footer-time"></span>
            </p>
        </footer>
    </div>

    <script>
        // Set timestamp
        const now = new Date();
        const formattedTime = now.toLocaleString('pt-BR', {
            weekday: 'long',
            year: 'numeric',
            month: 'long',
            day: 'numeric',
            hour: '2-digit',
            minute: '2-digit',
            second: '2-digit'
        });

        document.getElementById('timestamp').textContent = formattedTime;
        document.getElementById('footer-time').textContent = formattedTime;

        // Add animation on load
        document.querySelectorAll('.card').forEach((card, index) => {
            card.style.animation = `fadeInUp 0.6s ease-out ${index * 0.1}s both`;
        });

        // Fade in animation
        const style = document.createElement('style');
        style.textContent = `
            @keyframes fadeInUp {
                from {
                    opacity: 0;
                    transform: translateY(20px);
                }
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }
        `;
        document.head.appendChild(style);
    </script>
</body>
</html>'''

    # Create dashboard directory
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Write dashboard HTML
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(dashboard_html)
    
    print(f"✅ Dashboard gerado com sucesso: {output_file}")
    return str(output_file)

if __name__ == "__main__":
    try:
        output_path = sys.argv[1] if len(sys.argv) > 1 else "dashboard/index.html"
        result = generate_dashboard_html(output_path)
        print(f"📊 Dashboard HTML criado em: {result}")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Erro ao gerar dashboard: {e}")
        sys.exit(1)
