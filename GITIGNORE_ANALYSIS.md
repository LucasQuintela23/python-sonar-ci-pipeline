# 📋 Análise de Arquivos do Projeto e .gitignore

## 🔍 Análise dos Arquivos Gerados Localmente

Durante a execução do projeto, os seguintes arquivos e diretórios são gerados **localmente** e **NÃO devem ser versionados** no git:

---

## 🗑️ Arquivos/Diretórios Ignorados

### 1. **Ambiente Virtual Python**
```
venv/          # Ambiente virtual criado
```
- Gerado por: `python3 -m venv venv`
- Tamanho: ~150-300MB (não versionável)
- Reproduzível com: `pip install -r requirements.txt`

---

### 2. **Cache e Bytecode Python**
```
__pycache__/       # Cache de bytecode
.pytest_cache/     # Cache pytest
.mypy_cache/       # Cache mypy
.pytype/           # Cache pytype
*.py[cod]          # Arquivos compilados
*$py.class         # Bytecode Python
```
- Gerados automaticamente durante execução
- Redundantes (podem ser regenerados)

---

### 3. **Relatórios de Testes**
```
allure-results/              # Dados brutos dos testes
allure-results-combined/     # Dados combinados (multi-env)
allure-report/               # Relatório HTML Allure
allure-report-combined/      # Relatório combinado (multi-env)
```
- Gerados por: `pytest --alluredir=allure-results`
- Regeneráveis a cada execução
- Específicos do ambiente local

---

### 4. **Relatórios de Cobertura**
```
htmlcov/             # Relatório HTML Coverage padrão
htmlcov-staging/     # Cobertura do ambiente Staging
htmlcov-production/  # Cobertura do ambiente Production
coverage.xml         # Relatório XML (para SonarCloud)
.coverage            # Arquivo binário de coverage
.coverage.*          # Variações do arquivo coverage
```
- Gerados por: `pytest --cov=src --cov-report=html`
- Regeneráveis a cada teste
- Dados locais específicos

---

### 5. **Relatórios de Testes**
```
reports/             # Diretório de relatórios gerais
junit.xml            # Relatório JUnit XML
```
- Gerados durante CI/CD
- Dados de execução local

---

### 6. **SonarQube/SonarCloud**
```
.scannerwork/              # Diretório de trabalho SonarScanner
.sonarcloud.properties     # Propriedades locais SonarCloud
sonar-scanner.properties   # Configuração local SonarScanner
```
- Gerados durante análise SonarCloud
- Específicos da máquina local

---

### 7. **Compilação e Build**
```
build/                  # Diretório de build
dist/                   # Distribuição compilada
*.egg-info/             # Metadados de egg
.eggs/
develop-eggs/
```
- Gerados por: `python setup.py build`
- Reproduzíveis a partir do código-fonte

---

### 8. **Variáveis de Ambiente**
```
.env                      # Variáveis locais
.env.local                # Variáveis locais específicas
.env.*.local              # Variáveis por ambiente
.credentials              # Credenciais locais
*.pem, *.key, *.p12       # Chaves de segurança
secrets/                  # Arquivo de segredos
```
- Contêm dados sensíveis
- Nunca devem ser versionados

---

### 9. **IDE e Editor**
```
.vscode/               # Configurações Visual Studio Code
.idea/                 # Configurações JetBrains IDE
*.iml, *.iws, *.ipr   # Arquivos JetBrains
*.sublime-project      # Sublime Text
*.sublime-workspace    # Sublime Text
.history/              # Editor history
*.swp, *.swo, *~       # Vim backups
*.bak, *.backup        # Arquivos backup
```
- Configurações pessoais do editor
- Variam por desenvolvedor

---

### 10. **Sistema Operacional**
```
.DS_Store              # macOS
Thumbs.db              # Windows
Desktop.ini            # Windows
.Trash-*               # Linux
._*                    # macOS
.AppleDouble           # macOS
.LSOverride            # macOS
```
- Arquivos do SO
- Desnecessários para controle de versão

---

### 11. **Logs**
```
*.log                  # Arquivos de log
logs/                  # Diretório de logs
log/                   # Diretório de logs
```
- Gerados durante execução
- Específicos da máquina local

---

### 12. **Node.js (para Allure CLI)**
```
node_modules/          # Dependências npm
npm-debug.log          # Log npm
yarn-error.log         # Log yarn
```
- Grandes volumes
- Reproduzíveis com npm install

---

### 13. **Banco de Dados**
```
*.db                   # SQLite
*.sqlite, *.sqlite3    # SQLite
*.pgsql                # PostgreSQL
```
- Dados temporários
- Nunca devem ser versionados

---

### 14. **Database & Documentação**
```
docs/_build/           # Build Sphinx (se usando)
tmp/, temp/            # Arquivos temporários
*.orig, *.rej          # Arquivos merge/patch
```

---

## ✅ Arquivos que DEVEM ser Versionados

Esses arquivos são **essenciais** e devem estar no git:

```
✅ src/                           # Código-fonte
✅ tests/                         # Testes
✅ requirements.txt               # Dependências Python
✅ pytest.ini                     # Configuração pytest
✅ conftest.py                    # Configuração pytest hooks
✅ sonar-project.properties       # Config SonarCloud
✅ .github/workflows/             # GitHub Actions CI/CD
✅ README.md                      # Documentação principal
✅ .gitignore                     # Este arquivo
✅ setup.py (se existir)          # Setup Python
✅ Dockerfile (se existir)        # Configuração Docker
```

---

## 📊 Estrutura Recomendada para Git

```
github-repo/
│
├── ✅ CORE (Versionado)
│   ├── src/
│   ├── tests/
│   ├── .github/
│   ├── requirements.txt
│   ├── pytest.ini
│   ├── conftest.py
│   ├── sonar-project.properties
│   └── README.md
│
└── ❌ LOCAL (Ignorado)
    ├── venv/                         (ambiente virtual)
    ├── __pycache__/                  (cache)
    ├── htmlcov-staging/              (relatórios)
    ├── htmlcov-production/           (relatórios)
    ├── allure-report-combined/       (relatórios)
    ├── coverage.xml                  (relatórios)
    ├── .env                          (credenciais)
    ├── .vscode/                      (configurações pessoais)
    └── .scannerwork/                 (análise local)
```

---

## 🔧 Como Verificar o que está no .gitignore

### Verificar arquivos ignorados:
```bash
git check-ignore -v *                # Ver todos os ignorados
git status --ignored                 # Status com ignorados
```

### Remover arquivo do rastreamento (se foi commitado antes):
```bash
git rm --cached <arquivo>
git commit -m "Remove tracked but gitignored file"
```

---

## 📝 Atualização Realizada ao .gitignore

Os seguintes itens foram **adicionados** para cobrir testes multi-ambiente:

```gitignore
# Multi-Environment Specific
htmlcov-staging/              # Cobertura ambiente Staging
htmlcov-production/           # Cobertura ambiente Production
allure-results-combined/      # Resultados Allure combinados
allure-report-combined/       # Relatório Allure combinado
reports/                      # Diretório de relatórios gerais
junit.xml                     # Relatório JUnit
```

---

## 🎯 Segurança

⚠️ **Jamais commitar:**
- `.env` - Variáveis de ambiente
- `*.pem`, `*.key` - Chaves SSH/SSL
- `secrets/` - Arquivo de segredos
- Senhas ou tokens no código
- Credenciais AWS/Azure/GCP

✅ **Use ao invés:**
```bash
# Exemplo .env.example para documentação (sem valores reais)
TEST_ENVIRONMENT=development
DEBUG=true
LOG_LEVEL=info

# Em .env local (ignorado):
TEST_ENVIRONMENT=production
DEBUG=false
LOG_LEVEL=error
```

---

## 📈 Tamanho Economizado

Com o .gitignore configurado, você **evita versionar**:

| Item | Tamanho Típico | Motivo |
|------|---|---|
| `venv/` | 150-300MB | Reproduzível com pip |
| `__pycache__/` | 10-50MB | Cache regenerável |
| `allure-results/` | 5-50MB | Dados de execução local |
| `htmlcov/` | 1-10MB | Relatório regenerável |
| `node_modules/` | 100-500MB | Dependências npm |
| **TOTAL** | **300-900MB** | **Economizado!** |

---

## ✨ Resumo

✅ `.gitignore` foi **atualizado** com:
- Diretórios de testes multi-ambiente
- Relatórios combinados
- Cobertura por ambiente
- Relatórios gerais

✅ **Mais de 800MB** economizados em repositório  
✅ Repositório mais **limpo e leve**  
✅ Apenas código essencial versionado  
✅ Máxima segurança (sem credenciais)  

🚀 **Pronto para usar!**
