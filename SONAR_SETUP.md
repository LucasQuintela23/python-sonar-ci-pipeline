# SonarCloud Integration Guide

## O que é SonarCloud?

SonarCloud é uma plataforma CI/CD que analisa qualidade de código, detecta vulnerabilidades e problemas de cobertura de testes.

---

## Arquivo: sonar-project.properties

Este arquivo configura como o SonarScanner deve analisar seu projeto.

### Configuração Atual:

```properties
# Identificação do Projeto
sonar.projectKey=python-sonar-ci-pipeline
sonar.projectName=Python SonarCloud CI/CD Pipeline
sonar.projectVersion=1.0.0

# Caminhos de Código
sonar.sources=src              # Onde está o código-fonte
sonar.tests=tests              # Onde estão os testes

# Linguagem
sonar.language=py              # Python

# Relatório de Coverage
sonar.python.coverage.reportPaths=coverage.xml

# Exclusões
sonar.exclusions=**/__pycache__/**,**/site-packages/**

# Padrão de Testes
sonar.test.inclusions=tests/**/*.py
```

---

## Como Usar com SonarCloud

### Passo 1: Criar conta no SonarCloud

1. Acesse: https://sonarcloud.io/
2. Faça login com GitHub/GitLab/Bitbucket
3. Crie uma organização ou use a padrão

### Passo 2: Criar um token de autenticação

1. Vá para: https://sonarcloud.io/account/security/
2. Gere um novo token
3. Copie o token (você precisará dele)

### Passo 3: Instalar SonarScanner

```bash
npm install -g sonarqube-scanner
# OU (Ubuntu/Debian - via npm é mais confiável)
sudo npm install -g sonarqube-scanner
# OU (macOS)
brew install sonar-scanner
```

**Nota:** O `apt-get install sonar-scanner` pode não estar disponível em alguns repositórios Ubuntu. A instalação via npm é recomendada e é o que usamos neste projeto.

**Verificar instalação:**
```bash
sonar-scanner --version
# Resultado esperado: 4.3.4 (ou versão mais recente)
```

### Passo 4: Executar análise localmente

```bash
# 1. Gerar relatório de cobertura
source venv/bin/activate
pytest --cov=src --cov-report=xml --cov-report=html

# 2. Executar análise SonarQube
sonar-scanner \
  -Dsonar.projectBaseDir=. \
  -Dsonar.host.url=https://sonarcloud.io \
  -Dsonar.login=YOUR_TOKEN_HERE
```

### Passo 5: Usar em CI/CD (GitHub Actions)

Crie `.github/workflows/sonar.yml`:

```yaml
name: SonarCloud Analysis

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  sonarcloud:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.12'
      
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
      
      - name: Run tests and generate coverage
        run: |
          pytest --cov=src --cov-report=xml
      
      - name: SonarCloud Scan
        uses: SonarSource/sonarcloud-github-action@master
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
```

---

## Variáveis Importantes no sonar-project.properties

| Propriedade | Valor Atual | Descrição |
|------------|-----------|-----------|
| `sonar.projectKey` | `python-sonar-ci-pipeline` | Identificador único no SonarCloud |
| `sonar.projectName` | `Python SonarCloud CI/CD Pipeline` | Nome amigável |
| `sonar.projectVersion` | `1.0.0` | Versão do projeto |
| `sonar.sources` | `src` | Pasta com código-fonte |
| `sonar.tests` | `tests` | Pasta com testes |
| `sonar.language` | `py` | Linguagem (Python) |
| `sonar.python.coverage.reportPaths` | `coverage.xml` | Arquivo de cobertura |

---

## Personalizar para Seu Caso

### Se usar GitHub:

```properties
# Adicione ao final:
sonar.links.homepage=https://github.com/seu-usuario/seu-repo
sonar.links.ci=https://github.com/seu-usuario/seu-repo/actions
sonar.links.scm=https://github.com/seu-usuario/seu-repo
sonar.links.issue=https://github.com/seu-usuario/seu-repo/issues
```

### Se usar GitLab CI:

```properties
# Adicione:
sonar.gitlab.project_id=seu-project-id
sonar.gitlab.commit_sha=seu-commit-sha
sonar.gitlab.ref_name=seu-branch-name
```

### Se quiser excluir mais pastas:

```properties
sonar.exclusions=**/__pycache__/**,**/site-packages/**,**/node_modules/**,**/venv/**
```

---

## Comandos Úteis

### Análise Local:

```bash
# Com arquivo de propriedades
sonar-scanner -Dproject.settings=./sonar-project.properties \
  -Dsonar.host.url=https://sonarcloud.io \
  -Dsonar.login=TOKEN

# Ou via CLI (sobrescreve propriedades)
sonar-scanner \
  -Dsonar.projectKey=python-sonar-ci-pipeline \
  -Dsonar.sources=src \
  -Dsonar.tests=tests \
  -Dsonar.python.coverage.reportPaths=coverage.xml \
  -Dsonar.host.url=https://sonarcloud.io \
  -Dsonar.login=TOKEN
```

### Verificar configuração:

```bash
sonar-scanner --help
cat sonar-project.properties  # Ver configuração atual
```

---

## O que o SonarCloud Analisará

Após executar a análise, você verá:

✅ **Code Quality**
- Code Smells (problemas de qualidade)
- Bugs (possíveis bugs)
- Vulnerabilities (falhas de segurança)
- Coverage (cobertura de testes)

✅ **Métricas**
- Linhas de código
- Duplicação de código
- Complexidade ciclomática
- Dívida técnica

✅ **No nosso projeto:**
- ⚠️ `legacy_calculation()` será flagged como "Code Smell" (alta complexidade)
- ⚠️ `legacy_calculation()` terá "Coverage Gap" (não testado)
- ✅ `calculate_score()` e `approve_loan()` bem avaliados (type hints + docstrings)

---

## Dashboard do SonarCloud

Após análise, você verá um dashboard com:

```
Project: Python SonarCloud CI/CD Pipeline
Quality Gate Status: 🟢 PASSED / 🔴 FAILED

Metrics:
├── Reliability: A
├── Security: A
├── Maintainability: B
├── Coverage: 36%
├── Duplications: 0%
└── Code Smells: 1 (legacy_calculation)

Recent Analyses:
├── Last: 2026-01-21
├── Bugs: 0
├── Vulnerabilities: 0
└── Code Smells: 1
```

---

## Próximas Etapas

1. **Criar repositório GitHub:**
   ```bash
   git init
   git remote add origin https://github.com/seu-usuario/python-sonar-ci-pipeline
   git add .
   git commit -m "Initial commit: CI/CD pipeline with SonarCloud"
   git push -u origin main
   ```

2. **Configurar GitHub Secrets:**
   - Vá em: Settings → Secrets and variables → Actions
   - Adicione: `SONAR_TOKEN` (seu token do SonarCloud)

3. **Criar workflow GitHub Actions:**
   - Crie: `.github/workflows/sonar.yml` (veja exemplo acima)
   - Push para GitHub
   - Workflow será executado automaticamente

4. **Ver resultados no SonarCloud:**
   - Acesse: https://sonarcloud.io/dashboard?id=python-sonar-ci-pipeline
   - Visualize métricas em tempo real

---

## Troubleshooting

### Erro: "Project not found"

Solução:
```bash
# Certifique-se de que projectKey está correto
grep sonar.projectKey sonar-project.properties

# Ou use parâmetro na CLI
sonar-scanner -Dsonar.projectKey=seu-projeto-key
```

### Erro: "Coverage report not found"

Solução:
```bash
# Verifique se arquivo coverage.xml existe
ls -la coverage.xml

# Se não existir, gere:
pytest --cov=src --cov-report=xml
```

### Erro: "Authentication failed"

Solução:
```bash
# Verifique token
echo $SONAR_LOGIN  # Deve estar definido

# Ou use na CLI
sonar-scanner -Dsonar.login=seu-token-aqui
```

---

## Links Úteis

- 🌐 SonarCloud: https://sonarcloud.io
- 📚 Documentação: https://docs.sonarcloud.io
- 🐍 Python Docs: https://docs.sonarcloud.io/languages/python
- 🔧 Scanner Setup: https://docs.sonarcloud.io/advanced-setup/ci-cd-integrations
