# 🚀 Quick Reference Card

## Comandos Mais Usados

### 🧪 Testes
```bash
./run_tests.sh                    # Tudo em um comando ⭐
pytest                            # Rodar testes
pytest -v                         # Verbose
pytest -k "calculate_score"       # Teste específico
```

### 📊 Relatórios
```bash
allure open allure-report         # Abrir Allure (navegador)
open htmlcov/index.html           # Abrir Coverage
cat coverage.xml                  # Ver XML do Coverage
```

### 🔍 SonarCloud
```bash
./analyze_with_sonar.sh TOKEN     # Análise local
cat sonar-project.properties      # Ver configuração
```

### 📁 Estrutura
```bash
tree -L 2 -I 'venv|__pycache__'   # Ver estrutura
ls -la src/                       # Ver código
ls -la tests/                     # Ver testes
```

---

## Atalhos de Desenvolvimento

### Setup Inicial
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Antes de Commit
```bash
./run_tests.sh              # Validar tudo
git diff                    # Revisar mudanças
git add .
git commit -m "Descrição"
git push
```

### Debug
```bash
pytest -v -s                # Com print statements
pytest --pdb -x             # Para no primeiro erro
pytest --collect-only       # Lista testes
```

---

## Portais e URLs

| Recurso | URL |
|---------|-----|
| SonarCloud | https://sonarcloud.io |
| SonarCloud Dashboard | https://sonarcloud.io/dashboard |
| GitHub | https://github.com |
| Allure Local | http://localhost:7071 |
| Coverage Local | file:///.../htmlcov/index.html |

---

## Arquivos Importantes

| Arquivo | Propósito |
|---------|-----------|
| `src/credit_engine.py` | Código principal |
| `tests/test_credit_engine.py` | Testes |
| `requirements.txt` | Dependências |
| `sonar-project.properties` | Config SonarCloud |
| `pytest.ini` | Config Pytest + Allure |
| `run_tests.sh` | Script automático |
| `analyze_with_sonar.sh` | Script SonarCloud |
| `.github/workflows/sonar.yml` | GitHub Actions |

---

## Configurações Rápidas

### Para reduzir cobertura necessária no SonarCloud:
Edite `sonar-project.properties`:
```properties
# Adicione:
sonar.qualitygate.gate_status=WARN
```

### Para excluir mais arquivos:
```properties
sonar.exclusions=**/__pycache__/**,**/venv/**,**/node_modules/**
```

### Para adicionar mais linguagens:
```properties
# Para JavaScript também:
sonar.language=py,js
```

---

## Status do Projeto

```
✅ Código-fonte: Pronto
✅ Testes: 19/19 Passing
✅ Coverage: 36% (intencional)
✅ Allure: Configurado
✅ SonarCloud: Pronto
✅ GitHub Actions: Pronto
✅ Documentação: Completa
```

---

## Próximo Passo?

1. **Testar localmente:**
   ```bash
   ./run_tests.sh
   ```

2. **Ver Allure:**
   - Abra: http://localhost:7071

3. **Ler documentação:**
   - [README.md](README.md)
   - [SONAR_SETUP.md](SONAR_SETUP.md)
   - [GUIA_COMPLETO.md](GUIA_COMPLETO.md)

4. **Preparar GitHub:**
   - Criar repositório
   - Adicionar SONAR_TOKEN

---

**Criado em:** Jan 2026 | **Status:** ✅ Pronto | **Versão:** 1.0.0
