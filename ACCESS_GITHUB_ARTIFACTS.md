# 📊 Como Acessar o Dashboard do GitHub Actions

## 🎯 Passo a Passo - Acessar os Artifacts

### 1️⃣ Vá para GitHub Actions

```
https://github.com/LucasQuintela23/python-sonar-ci-pipeline/actions
```

ou

```
Seu Repositório → Actions (aba no topo)
```

### 2️⃣ Selecione o Workflow Mais Recente

- Clique em **"SonarCloud Analysis & Test Reports"**
- Escolha a execução mais recente (a que você quer ver)

### 3️⃣ Veja os 5 Estágios Executando

Na página do workflow, você verá:

```
✅ Stage 1 - Setup & Multi-Environment Testing
✅ Stage 2 - Generate Reports
✅ Stage 3 - Upload Artifacts
✅ Stage 4 - SonarCloud Analysis
✅ Stage 5 - Workflow Summary
```

---

## 📦 Onde Estão os Artifacts

Role a página para baixo até encontrar a seção **"Artifacts"**

### Arquivos Disponíveis

```
📦 allure-report-combined-multi-env
   └─ Relatório Allure com 38 testes (Staging + Production)
   └─ Clique para baixar

📦 coverage-report-staging  
   └─ Cobertura do ambiente Staging
   └─ Relatório HTML de cobertura

📦 coverage-report-production
   └─ Cobertura do ambiente Production
   └─ Relatório HTML de cobertura

📦 final-reports-multi-env
   └─ Pasta consolidada com README
   └─ Links para todos os relatórios

📦 coverage-xml
   └─ Dados XML para SonarCloud
   └─ Arquivo técnico
```

---

## 🚀 Como Usar Cada Artifact

### 🎨 **Allure Report** (Mais Importante!)

#### Baixar:
1. Clique em `allure-report-combined-multi-env`
2. Navegador baixará um `.zip`
3. Extraia em uma pasta

#### Abrir no navegador:
```bash
# Depois de extrair
open allure-report-combined/index.html
# ou
firefox allure-report-combined/index.html
```

**O que você verá:**
- 📊 Gráficos de execução
- 19 testes Staging ✅
- 19 testes Production ✅
- Detalhes de cada teste
- Tempo de execução

---

### 📊 **Coverage Reports** (2 arquivos)

#### Staging Coverage:
1. Clique em `coverage-report-staging`
2. Baixe e extraia
3. Abra `htmlcov-staging/index.html`

**Mostra:**
- Arquivos testados em Staging
- Taxa de cobertura (36%)
- Linhas cobertas/não cobertas

#### Production Coverage:
1. Clique em `coverage-report-production`
2. Baixe e extraia
3. Abra `htmlcov-production/index.html`

**Mostra:**
- Mesmo formato que Staging
- Cobertura do ambiente Production
- Comparação é útil!

---

### 📋 **Final Reports** (Resumo)

#### O que é:
- Pasta com README.md
- Links consolidados para todos os relatórios
- Guia de navegação

#### Como usar:
1. Clique em `final-reports-multi-env`
2. Extraia
3. Abra `final-reports/README.md` em qualquer editor de texto

---

## 🔍 Alternativa: Acessar Diretamente no GitHub

Sem baixar nada!

### Opção 1: Ver Logs do Workflow

1. Vá para **Actions**
2. Clique no workflow
3. Veja os logs de cada stage
4. O Stage 5 mostra um resumo completo com:
   ```
   📊 STAGES EXECUTED:
   🧪 TEST RESULTS:
   📦 ARTIFACTS GENERATED:
   ```

### Opção 2: SonarCloud Dashboard

Para análise de código:

```
https://sonarcloud.io/dashboard?id=python-sonar-ci-pipeline
```

Mostra:
- 📈 Bugs encontrados
- 🔒 Vulnerabilidades
- 📊 Cobertura geral
- 🎯 Code smells

---

## 💡 Dica Prática: Automação

### Usar Python para Baixar Artifacts

```bash
# Usando GitHub CLI
gh run download <RUN_ID> -n allure-report-combined-multi-env

# Listar artifacts de um run
gh run view <RUN_ID> --json artifacts
```

---

## 📱 Visualização Rápida - Passo a Passo Completo

### 1. Abra GitHub
```
github.com/LucasQuintela23/python-sonar-ci-pipeline
```

### 2. Clique em "Actions"
```
[Code] [Pull requests] [Actions] ← Clique aqui
```

### 3. Selecione o Workflow
```
SonarCloud Analysis & Test Reports (clique no nome)
```

### 4. Escolha a Execução
```
Lista com data e hora → Clique na mais recente
```

### 5. Scroll até "Artifacts"
```
┌─────────────────────────────────────────┐
│ Artifacts                               │
├─────────────────────────────────────────┤
│ allure-report-combined-multi-env  📥   │
│ coverage-report-staging          📥   │
│ coverage-report-production       📥   │
│ final-reports-multi-env          📥   │
│ coverage-xml                     📥   │
└─────────────────────────────────────────┘
```

### 6. Clique em um Artifact
```
Começe com: allure-report-combined-multi-env
```

### 7. Extraia e Abra
```
unzip allure-report-combined-multi-env.zip
open allure-report-combined/index.html
```

### 8. Pronto! 🎉
Veja o dashboard com todos os 38 testes!

---

## 🎯 Resumo Visual

```
GitHub Actions Run
    ↓
Artifacts (5 arquivos)
    ├─→ allure-report-combined-multi-env
    │   └─ 📊 MAIOR PRIORIDADE
    │   └─ 38 testes (19+19)
    │   └─ Gráficos bonitos
    │
    ├─→ coverage-report-staging
    │   └─ 📈 Cobertura Staging
    │
    ├─→ coverage-report-production
    │   └─ 📈 Cobertura Production
    │
    ├─→ final-reports-multi-env
    │   └─ 📋 Links consolidados
    │
    └─→ coverage-xml
        └─ 🔧 Para SonarCloud
```

---

## ❓ FAQ

### P: Quanto tempo os artifacts ficam disponíveis?
**R:** 30 dias para relatórios, 7 dias para coverage.xml

### P: Posso compartilhar o dashboard com alguém?
**R:** Sim! Baixe, extraia e envie o arquivo. Abra em qualquer navegador.

### P: Como comparar Staging com Production?
**R:** Baixe ambos os coverage reports e compare os HTML

### P: Onde vejo o resumo sem baixar nada?
**R:** Vá para Stage 5 (Workflow Summary) nos logs

### P: Como integrar ao CI/CD local?
**R:** Execute `./serve_dashboard.sh` localmente (não precisa GitHub)

---

## 🔗 Links Diretos

### Seu Repositório
```
https://github.com/LucasQuintela23/python-sonar-ci-pipeline
```

### GitHub Actions
```
https://github.com/LucasQuintela23/python-sonar-ci-pipeline/actions
```

### SonarCloud
```
https://sonarcloud.io/dashboard?id=python-sonar-ci-pipeline
```

---

## 🚀 Próxima Execução

Quando você fizer um novo push:

1. GitHub Actions executará automaticamente
2. Os 5 stages rodaram em sequência/paralelo
3. Nuevos artifacts aparecerão
4. Você pode baixar e comparar com anteriores

---

**Status:** ✅ Todos os artifacts estão acessíveis
**Tempo de Retenção:** 30 dias (relatórios), 7 dias (XML)
**Próxima Atualização:** Quando você fizer push
