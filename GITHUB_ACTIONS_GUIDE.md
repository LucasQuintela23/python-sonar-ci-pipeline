# 🚀 GitHub Actions CI/CD Pipeline - Multi-Environment Testing

## Visão Geral

O workflow foi atualizado para suportar testes em **múltiplos ambientes** (Staging e Production) com geração automática de relatórios combinados.

## 📋 Etapas do Pipeline

### 1. Setup Inicial
- ✅ Checkout do código
- ✅ Setup Python 3.12
- ✅ Cache de dependências pip
- ✅ Instalação de dependências

### 2. Execução de Testes Multi-Ambiente 🆕
```yaml
# Step: Run multi-environment tests
./run_tests_multi_env.sh
```

**O que faz:**
- Executa 19 testes no ambiente **STAGING** (Homologação)
- Gera cobertura em `htmlcov-staging/`
- Executa 19 testes no ambiente **PRODUCTION** (Produção)
- Gera cobertura em `htmlcov-production/`
- Combina resultados em `allure-results-combined/`

### 3. Geração de Relatórios
- ✅ Relatório Allure combinado (multi-ambiente)
- ✅ Dashboard HTML com comparação de ambientes
- ✅ Relatórios de cobertura separados

### 4. Análise SonarCloud
- ✅ Análise estática de código
- ✅ Integração com SonarCloud

### 5. Upload de Artefatos 🆕

Os seguintes artefatos são salvos automaticamente:

| Artefato | Descrição | Retenção |
|----------|-----------|----------|
| `allure-report-combined-multi-env` | Relatório Allure completo (38 testes) | 30 dias |
| `coverage-report-staging` | Cobertura do ambiente Staging | 30 dias |
| `coverage-report-production` | Cobertura do ambiente Production | 30 dias |
| `final-reports-multi-env` | Resumo consolidado com README | 30 dias |
| `coverage-xml` | Dados de cobertura para SonarCloud | 7 dias |

## 🎯 Como Acessar os Relatórios

### No GitHub Actions
1. Vá para **Actions** → **Latest Run**
2. Role até **Artifacts**
3. Clique em cada artefato para baixar

### Tipos de Relatórios

#### 🎨 Allure Report (Multi-Environment)
```
Artefato: allure-report-combined-multi-env/
Abra: index.html
Contém: 19 testes Staging + 19 testes Production = 38 total
```

#### 📊 Coverage Reports
```
Staging:    coverage-report-staging/index.html
Production: coverage-report-production/index.html
```

#### 📋 Final Reports Summary
```
Artefato: final-reports-multi-env/
Contém: README.md + links para todos os relatórios
```

## 📈 Métricas Capturadas

Para cada ambiente:
- Total de testes executados
- Testes passando/falhando
- Tempo de execução
- Cobertura de código (%)
- Detalhes de cada test case

## 🔄 Fluxo de Execução

```
┌─────────────────────────────────────────────────────────────┐
│                    Git Push / Pull Request                    │
└────────────────────────────────┬────────────────────────────┘
                                 │
                    ┌────────────▼────────────┐
                    │  Setup Environment      │
                    │  Install Dependencies   │
                    └────────────┬────────────┘
                                 │
      ┌──────────────────────────▼──────────────────────────┐
      │     Run Multi-Environment Tests                      │
      │  ┌─────────────────┐    ┌──────────────────┐       │
      │  │  STAGING (19)   │    │  PRODUCTION (19) │       │
      │  │  Generate Cov   │    │  Generate Cov    │       │
      │  └────────┬────────┘    └────────┬─────────┘       │
      │           │                      │                   │
      │           └──────────┬───────────┘                   │
      │                      │                               │
      │        Combine Results (38 total)                    │
      │                      │                               │
      └──────────────────────┬──────────────────────────────┘
                             │
      ┌──────────────────────▼──────────────────────────┐
      │  Generate Reports                                │
      │  ├─ Allure Report (combined)                   │
      │  ├─ Coverage Reports (staging)                 │
      │  ├─ Coverage Reports (production)              │
      │  └─ Dashboard Summary                          │
      └──────────────────────┬──────────────────────────┘
                             │
      ┌──────────────────────▼──────────────────────────┐
      │  SonarCloud Analysis                            │
      │  Upload artifacts to GitHub                     │
      │  Comment on PR with results                     │
      └──────────────────────┬──────────────────────────┘
                             │
                    ┌────────▼────────┐
                    │  ✅ Complete    │
                    └─────────────────┘
```

## 💾 Armazenamento e Retenção

- **30 dias**: Relatórios principais (Allure, Coverage)
- **7 dias**: XML de cobertura (SonarCloud)
- **Ilimitado**: Histórico no repositório Git

## 🔍 Integração com SonarCloud

O workflow automaticamente:
1. Gera relatório de cobertura XML
2. Envia para SonarCloud
3. Atualiza dashboard: https://sonarcloud.io/dashboard?id=python-sonar-ci-pipeline

## 📝 Exemplo de Execução

```
╔════════════════════════════════════════════════════════════╗
║         🎉 CI/CD Pipeline Execution Complete 🎉          ║
╚════════════════════════════════════════════════════════════╝

📊 Multi-Environment Test Results:
  ✅ Staging Environment (19 tests)
  ✅ Production Environment (19 tests)
  ✅ Combined Reports (38 total)

📋 Relatórios Gerados:
  ✅ Multi-Env Coverage Reports (Staging + Production)
  ✅ Combined Allure Report (Interactive HTML)
  ✅ JUnit Test Report (XML)
  ✅ SonarCloud Analysis
  ✅ Final Reports Summary

📦 Artifacts disponíveis em:
  - allure-report-combined-multi-env
  - coverage-report-staging
  - coverage-report-production
  - final-reports-multi-env
  - Actions > Latest Run > Artifacts
```

## 🛠️ Troubleshooting

### Artifact não foi gerado

**Verificar:**
1. Se os testes foram executados com sucesso
2. Se o script `run_tests_multi_env.sh` está no repo
3. Se os diretórios `htmlcov-staging/` e `htmlcov-production/` foram criados

### Allure Report vazio

**Verificar:**
1. Se `allure-results-combined/` foi criado
2. Se há arquivos JSON neste diretório
3. Se o comando `allure generate` foi executado com sucesso

### SonarCloud não atualizou

**Verificar:**
1. Se `secrets.SONAR_TOKEN` está configurado
2. Se `coverage.xml` foi gerado
3. Se `sonar-project.properties` está correto

## 📌 Notas Importantes

- Pipeline executa em **ubuntu-latest**
- Python **3.12** é usado
- Suporta **push** e **pull_request** triggers
- Relatórios comentados automaticamente em PRs
- Todos os steps continuam mesmo se um falhar (`continue-on-error: true`)

---

**Última Atualização:** 2026-01-26
**Status:** ✅ Ativo e Testado
