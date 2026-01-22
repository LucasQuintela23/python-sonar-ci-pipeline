# Projeto Customizado com Allure Report ✨

## O que foi adicionado:

### 1. **Allure Report Integration**
   - Decoradores Allure em todos os testes (@allure.title, @allure.description, @allure.severity)
   - Organização por Features e Stories
   - Níveis de severidade (CRITICAL, NORMAL)
   - Relatório interativo e visual

### 2. **Configuração automatizada**
   - `pytest.ini`: Configuração de paths e Allure
   - `run_tests.sh`: Script para executar testes completos

### 3. **Requirements atualizados**
   - `allure-pytest==2.13.2`: Integração Allure com pytest

### 4. **Testes enriquecidos**
   - 19 testes com documentação detalhada
   - Decoradores Allure em cada teste
   - Agrupamento por funcionalidade

---

## Como usar:

### Opção 1: Script Automatizado (Recomendado)
```bash
./run_tests.sh
```

### Opção 2: Manualmente
```bash
# Ativar ambiente virtual
source venv/bin/activate

# Rodar testes (gera allure-results)
pytest -v

# Gerar relatório Allure
allure generate allure-results -o allure-report --clean

# Abrir no navegador
allure open allure-report
```

---

## Relatórios Gerados:

| Tipo | Localização | Descrição |
|------|-------------|-----------|
| **Coverage Report** | `htmlcov/index.html` | Cobertura de testes HTML |
| **Coverage XML** | `coverage.xml` | Formato XML para SonarCloud |
| **Allure Results** | `allure-results/` | Dados brutos dos testes |
| **Allure Report** | `allure-report/index.html` | Relatório Allure interativo |

---

## Estrutura Allure:

```
Features (Stories)
├── Credit Analysis
│   ├── Calculate Score (7 testes)
│   ├── Approve Loan (9 testes)
│   └── Integration Tests (3 testes)
```

Cada teste possui:
- ✅ Título descritivo
- 📝 Descrição detalhada
- 🎯 Nível de severidade
- 📊 Resultado (Pass/Fail)

---

## Comandos Úteis:

```bash
# Apenas relatório pytest
pytest -v

# Com coverage
pytest --cov=src --cov-report=html

# Apenas Allure (sem coverage)
pytest --alluredir=allure-results

# Limpar e recriar tudo
./run_tests.sh

# Abrir relatório Allure em porta específica
allure open allure-report -p 7072

# Servir localmente (sem allure)
python3 -m http.server 8000
```

---

## Diferenciais do Allure Report:

🎨 **Visualmente Atrativo**
- Interface moderna e interativa
- Gráficos e estatísticas em tempo real

📊 **Organização Hierárquica**
- Features → Stories → Tests
- Fácil navegação

🎯 **Rastreabilidade**
- Severity levels (CRITICAL/NORMAL)
- Status detalhado
- Timeline de execução

📱 **Responsivo**
- Funciona em desktop e mobile
- Compatible com vários navegadores

---

## Próximos Passos:

1. ✅ Todos os testes passando (19/19)
2. ✅ Coverage reports (36% cobertura intencional)
3. ✅ Allure Report configurado
4. ⏭️ Integração com SonarCloud CI/CD
5. ⏭️ GitHub Actions workflow

