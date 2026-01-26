# 🧪 Multi-Environment Test Execution

## Visão Geral

Este projeto agora suporta execução de testes em **múltiplos ambientes separados** (Homologação e Produção) com relatórios combinados no Allure Report.

---

## 🚀 Como Usar

### Passo 1: Executar Testes em Ambos os Ambientes

```bash
./run_tests_multi_env.sh
```

Este script irá:
- ✅ Executar 19 testes no ambiente **STAGING (Homologação)**
- ✅ Executar 19 testes no ambiente **PRODUCTION (Produção)**
- ✅ Gerar relatórios de cobertura separados para cada ambiente
- ✅ Combinar resultados em um único relatório Allure
- ✅ Total: **38 testes** com **100% de sucesso**

**Tempo esperado:** ~30-40 segundos

---

### Passo 2: Visualizar Resultados

Você tem 2 opções:

#### **Opção A: Dashboard Visual (Recomendado)**
```bash
./serve_dashboard.sh
```

Acesse: `http://localhost:8000`

- 🎨 Interface moderna e intuitiva
- 📊 Comparação lado-a-lado dos ambientes
- 📈 Resumo executivo com métricas principais
- 🔗 Links para relatórios detalhados

#### **Opção B: Relatório Allure Completo**
```bash
./serve_combined_allure.sh
```

Acesse: `http://localhost:7071` ou `http://localhost:8000/allure-report-combined`

- 📋 Detalhamento completo de cada teste
- 📊 Gráficos e estatísticas em tempo real
- 🎯 Severidades e classificações
- 📈 Timeline de execução

---

## 📊 Estrutura de Relatórios

Após executar `run_tests_multi_env.sh`, você terá:

```
📦 Projeto
├── 📁 allure-report-combined/
│   └── 📄 index.html              ← Relatório Allure unificado
│
├── 📊 Coverage Reports:
│   ├── htmlcov-staging/           ← Cobertura Homologação
│   └── htmlcov-production/        ← Cobertura Produção
│
└── 📁 Resultado da Execução:
    ├── allure-results-combined/   ← Dados combinados Allure
    └── logs de execução
```

---

## 🔍 O Que Cada Script Faz

### `run_tests_multi_env.sh`
```bash
1. Cria/ativa ambiente virtual Python
2. Instala dependências
3. STAGING: Executa 19 testes
   └─ Gera htmlcov-staging/
   └─ Cria allure-results/
4. PRODUCTION: Executa 19 testes
   └─ Gera htmlcov-production/
   └─ Cria allure-results/ (adiciona aos anteriores)
5. Combina resultados em allure-report-combined/
```

### `serve_dashboard.sh`
```bash
1. Cria dashboard HTML personalizado
2. Inicia servidor Python na porta 8000
3. Mostra resumo visual dos dois ambientes
4. Fornece links para todos os relatórios
```

### `serve_combined_allure.sh`
```bash
1. Verifica se relatório Allure existe
2. Inicia servidor HTTP
3. Abre http://localhost:7071 no navegador
```

---

## 📈 Métricas Mostradas

### Por Ambiente:

| Métrica | Staging | Production |
|---------|---------|-----------|
| **Testes** | 19 | 19 |
| **Taxa Sucesso** | 100% | 100% |
| **Cobertura** | 36% | 36% |
| **Tempo** | 0.19s | 0.14s |

### Suites por Ambiente:

1. **Calculate Score** (7 testes)
   - Valor positivo
   - Com dívida
   - Cap em 1000
   - Valores zero
   - Dívida > renda
   - Valores negativos (2 testes)

2. **Approve Loan** (9 testes)
   - Aprovação válida
   - Rejeição por score baixo
   - Score em threshold
   - Score acima de threshold
   - Amount muito alto
   - Amount abaixo do limite
   - Ambas condições falham
   - Validação de negativos (2 testes)

3. **Integration Tests** (3 testes)
   - Workflow completo aprovado
   - Rejeição por renda baixa
   - Rejeição por valor alto

---

## 🔧 Configuração de Ambientes

### Variáveis de Ambiente

Os testes detectam automaticamente o ambiente via:

```bash
export TEST_ENVIRONMENT="staging"    # Ou "production"
```

Isso é definido automaticamente no script `run_tests_multi_env.sh`.

### Arquivo de Configuração

- `pytest.ini` - Configuração pytest base
- `conftest.py` - Hooks pytest para ambiente
- `.env` - (opcional) Variáveis de ambiente locais

---

## 📝 Exemplo de Saída

```
==========================================
Multi-Environment Test Execution
==========================================

==========================================
ENVIRONMENT 1: STAGING (Homologação)
==========================================

Running tests in STAGING environment...
============================= test session starts ==============================
...
============================== 19 passed in 0.19s ==============================
✅ STAGING tests completed!

==========================================
ENVIRONMENT 2: PRODUCTION (Produção)
==========================================

Running tests in PRODUCTION environment...
============================= test session starts ==============================
...
============================== 19 passed in 0.14s ==============================
✅ PRODUCTION tests completed!

==========================================
Generating Combined Allure Report
==========================================
Report successfully generated to allure-report-combined

✅ Both environments completed successfully!

📊 Reports Available:
   • Staging Coverage:     htmlcov-staging/index.html
   • Production Coverage:  htmlcov-production/index.html
   • Combined Allure:      allure-report-combined/index.html

🚀 To view combined Allure report, run:
   ./serve_combined_allure.sh
```

---

## 🎯 Fluxo Recomendado

### Development/Testing:
```bash
# 1. Execute os testes
./run_tests_multi_env.sh

# 2. Visualize o dashboard
./serve_dashboard.sh

# Ou visualize Allure completo
./serve_combined_allure.sh
```

### CI/CD Pipeline:
```bash
# O script run_tests_multi_env.sh pode ser executado em pipeline:
bash run_tests_multi_env.sh

# Resultados são salvos para integração:
# - allure-results-combined/
# - htmlcov-staging/
# - htmlcov-production/
```

---

## 🔗 Links Rápidos

Após executar os scripts:

1. **Dashboard Visual**
   - URL: `http://localhost:8000`
   - Arquivo: `/tmp/multi_env_dashboard.html`

2. **Allure Report Completo**
   - URL: `http://localhost:7071`
   - Arquivo: `allure-report-combined/index.html`

3. **Coverage Staging**
   - Arquivo: `htmlcov-staging/index.html`

4. **Coverage Production**
   - Arquivo: `htmlcov-production/index.html`

---

## 🆘 Troubleshooting

### Erro: "allure-report-combined não encontrado"
```bash
# Solução: Execute os testes primeiro
./run_tests_multi_env.sh
```

### Erro: "Porta 8000/7071 já em uso"
```bash
# Solução: Use porta diferente
python3 -m http.server 9000
allure open allure-report-combined --port 9090
```

### Erro: "Allure CLI não encontrado"
```bash
# Solução: Instale Allure
npm install -g allure-commandline

# Ou deixe o script usar fallback com Python HTTP server
```

---

## 📚 Documentação Relacionada

- [ALLURE_SETUP.md](ALLURE_SETUP.md) - Setup Allure
- [CI_CD_WORKFLOW_GUIDE.md](CI_CD_WORKFLOW_GUIDE.md) - Pipeline GitHub Actions
- [QUICK_REFERENCE.md](QUICK_REFERENCE.md) - Comandos rápidos

---

## ✅ Checklist

Após executar:

- [ ] Executei `./run_tests_multi_env.sh`
- [ ] Visualizei o dashboard com `./serve_dashboard.sh`
- [ ] Confirmei que ambos os ambientes passaram
- [ ] Revisei a cobertura em ambos os ambientes
- [ ] Explorei o relatório Allure detalhado

---

## 🎉 Resultado Final

✅ **38 testes totais** (19 Staging + 19 Production)  
✅ **100% de sucesso** em ambos os ambientes  
✅ **Cobertura 36%** mantida em ambos  
✅ **Relatórios combinados** prontos para análise  
✅ **Dashboard visual** para fácil visualização  

Tudo pronto para **produção**! 🚀
