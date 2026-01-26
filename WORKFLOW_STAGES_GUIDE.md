# 🎭 GitHub Actions Pipeline - Estrutura em Estágios

## 📋 Visão Geral

O workflow foi completamente reestruturado em **5 estágios independentes** para melhor organização, debugging e paralelização.

## 🎯 Os 5 Estágios

### ⚙️ STAGE 1: Setup & Multi-Environment Testing
**Job:** `setup-and-test`

**Responsabilidades:**
- Checkout do código
- Setup Python 3.12
- Cache de dependências
- Instalação de pacotes
- **Execução de testes em 2 ambientes:**
  - 🟡 STAGING: 19 testes
  - 🔴 PRODUCTION: 19 testes
- Salva resultados como artifact intermediário

**Saída:**
```
test-results-intermediate/
├── allure-results-combined/
├── htmlcov-staging/
├── htmlcov-production/
└── coverage.xml
```

**Duração esperada:** ~2-3 minutos

---

### 📊 STAGE 2: Generate Reports
**Job:** `generate-reports`
**Dependência:** `setup-and-test`

**Responsabilidades:**
- Baixa resultados do stage anterior
- Gera relatório Allure combinado (38 testes)
- Consolida todos os relatórios em `final-reports/`
- Cria README com links para relatórios

**Saída:**
```
final-reports/
├── allure-combined/
├── coverage-staging/
├── coverage-production/
└── README.md
```

**Duração esperada:** ~1-2 minutos

---

### 📤 STAGE 3: Upload Artifacts
**Job:** `upload-artifacts`
**Dependência:** `generate-reports`

**Responsabilidades:**
- Baixa artefatos dos stages anteriores
- Faz upload dos relatórios finais
- Separa uploads por tipo:
  - 🎨 Allure Report
  - 📊 Coverage Reports (Staging)
  - 📊 Coverage Reports (Production)
  - 📋 Final Reports Summary
  - 📈 Coverage XML (para SonarCloud)

**Artifacts Gerados:**

| Nome | Caminho | Dias |
|------|---------|------|
| `allure-report-combined-multi-env` | `allure-report-combined/` | 30 |
| `coverage-report-staging` | `htmlcov-staging/` | 30 |
| `coverage-report-production` | `htmlcov-production/` | 30 |
| `final-reports-multi-env` | `final-reports/` | 30 |
| `coverage-xml` | `coverage.xml` | 7 |

**Duração esperada:** ~1-2 minutos

---

### 🔍 STAGE 4: SonarCloud Analysis
**Job:** `sonarcloud-analysis`
**Dependência:** `setup-and-test`

**Responsabilidades:**
- Executa testes novamente (para gerar coverage.xml)
- Envia dados para SonarCloud
- Atualiza dashboard de análise

**Saída:**
```
https://sonarcloud.io/dashboard?id=python-sonar-ci-pipeline
```

**Duração esperada:** ~2-3 minutos

---

### ✨ STAGE 5: Workflow Summary
**Job:** `workflow-summary`
**Dependência:** `[setup-and-test, generate-reports, upload-artifacts, sonarcloud-analysis]`

**Responsabilidades:**
- Exibe resumo completo da execução
- Lista todos os artefatos gerados
- Mostra links para relatórios
- Confirma status final

**Exemplo de Saída:**
```
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║              ✅ CI/CD Pipeline Execution Complete! 🎉                   ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝

📊 STAGES EXECUTED:
  1️⃣  Stage 1 - Setup & Multi-Environment Testing
  2️⃣  Stage 2 - Generate Reports
  3️⃣  Stage 3 - Upload Artifacts
  4️⃣  Stage 4 - SonarCloud Analysis
  5️⃣  Stage 5 - Workflow Summary

🧪 TEST RESULTS:
  ✅ Staging:    19/19 tests
  ✅ Production: 19/19 tests
  ✅ Total:      38/38 tests (100%)

📦 ARTIFACTS GENERATED:
  ✅ allure-report-combined-multi-env
  ✅ coverage-report-staging
  ✅ coverage-report-production
  ✅ final-reports-multi-env
  ✅ coverage-xml

🔍 ANALYSIS:
  ✅ SonarCloud scan completed
  📊 View: https://sonarcloud.io/dashboard?id=python-sonar-ci-pipeline
```

---

## 🔄 Fluxo de Execução

```
                    ┌─ Stage 1: Setup & Testing ─┐
                    │                              │
                    │  • Checkout                 │
                    │  • Setup Python             │
                    │  • Install deps             │
                    │  • Run multi-env tests ✅   │
                    │  • Save intermediate artifact
                    └──────────────┬──────────────┘
                                   │
                ┌──────────────────┼──────────────────┐
                │                  │                  │
        ┌───────▼─────────┐ ┌─────▼────────┐ ┌─────▼────────┐
        │  Stage 2:       │ │  Stage 4:    │ │  Stage 5:    │
        │  Generate       │ │  SonarCloud  │ │  Summary     │
        │  Reports        │ │  Analysis    │ │  (depends on │
        │                 │ │              │ │  all stages) │
        └────────┬────────┘ └──────┬───────┘ └──────────────┘
                 │                 │              ▲
                 │                 │              │
        ┌────────▼─────────────────┼──────────────┘
        │
        │  Stage 3: Upload Artifacts
        │
        │  • Allure Report
        │  • Coverage Reports
        │  • Final Reports
        │  • Coverage XML
        │
        └─────────────────────────────
```

---

## 🛠️ Benefícios da Nova Estrutura

### ✅ **Separação de Responsabilidades**
- Cada stage tem uma responsabilidade clara
- Fácil de entender e manter
- Simples de debugar problemas específicos

### ✅ **Paralelização**
- Stages que não dependem um do outro executam em paralelo
- Stage 2 e 4 rodam ao mesmo tempo após Stage 1
- Reduz tempo total de execução

### ✅ **Reusabilidade de Artefatos**
- Testes rodam uma vez no Stage 1
- Resultados são compartilhados entre stages
- Economia de tempo e recursos

### ✅ **Melhor Debugging**
- Logs organizados por stage
- Fácil identificar qual stage falhou
- Pode-se re-rodar um stage específico se necessário

### ✅ **Escalabilidade**
- Fácil adicionar novos stages no futuro
- Padrão consistente para novos jobs
- Comunicação clara entre stages via artifacts

---

## 🚀 Atualização de Versões

### De v3 para v4

**Mudanças Aplicadas:**

```yaml
# Antes (v3)
- uses: actions/upload-artifact@v3
- uses: actions/download-artifact@v3

# Depois (v4)
- uses: actions/upload-artifact@v4
- uses: actions/download-artifact@v4
```

**Benefícios:**
- Suporte moderno
- Melhor performance
- Sem deprecation warnings
- Segurança atualizada

---

## 📊 Tempo Total de Execução

| Stage | Duração | Status |
|-------|---------|--------|
| 1 - Setup & Testing | ~2-3 min | ⚙️ |
| 2 - Generate Reports | ~1-2 min | ⏳ (parallel a 4) |
| 3 - Upload Artifacts | ~1-2 min | ⏳ (depends on 2) |
| 4 - SonarCloud | ~2-3 min | ⏳ (parallel a 2) |
| 5 - Summary | ~30 sec | ✨ (final) |
| **TOTAL** | **~6-8 min** | **✅** |

---

## 🎯 Como Acessar os Artifacts

### No GitHub
1. Vá para **Actions**
2. Clique no workflow mais recente
3. Role até a seção **Artifacts**
4. Clique no artefato desejado

### Estrutura de Artefatos

```
Actions → Run → Artifacts
├── allure-report-combined-multi-env
│   └── Relatório Allure completo com 38 testes
├── coverage-report-staging
│   └── Cobertura ambiente Staging
├── coverage-report-production
│   └── Cobertura ambiente Production
├── final-reports-multi-env
│   └── README.md + links consolidados
├── coverage-xml
│   └── Dados para SonarCloud
```

---

## 🔧 Troubleshooting

### Se um stage falhar

**Opção 1:** Re-rodar o workflow inteiro
```
GitHub → Actions → Run workflow → Re-run all jobs
```

**Opção 2:** Re-rodar um job específico (se necessário)
```
GitHub → Actions → Run workflow → Re-run failed jobs
```

### Se artifacts não forem criados

**Verificar:**
1. Se o stage anterior passou
2. Caminho dos arquivos está correto
3. Permissões de escrita

### Se SonarCloud não sincroniza

**Verificar:**
1. `SONAR_TOKEN` está configurado
2. `sonar-project.properties` está correto
3. `coverage.xml` foi gerado

---

## 📝 Commit Relacionado

```
commit 96a01a2
refactor: Restructure workflow into 5 clear stages
- Separated into independent jobs
- Updated upload-artifact to v4
- Added intermediate artifact communication
- Better error handling
```

---

**Status:** ✅ Implementado e Testado
**Data:** 2026-01-26
**Versão:** 2.0 (Estágios)
