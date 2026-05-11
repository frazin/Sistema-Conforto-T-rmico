# 🚀 Como Usar os Testes

## Rápido Início

### 1️⃣ Instalar dependências
```bash
cd Pedrão-JF
pip install -r requirements.txt pytest
```

### 2️⃣ Executar todos os 34 testes
```bash
# Opção A: Usar o script Python (Windows/Linux)
python run_tests.py all

# Opção B: Usar pytest diretamente
python -m pytest tests/test_rules.py -v

# Opção C: Usar o script shell (Linux/Mac)
bash run_tests.sh
```

### 3️⃣ Executar testes específicos
```bash
# Apenas testes de regras
python run_tests.py rules

# Apenas testes de classifier
python run_tests.py classifier

# Apenas testes de Decision Tree
python run_tests.py tree

# Apenas testes de integração
python run_tests.py integration
```

---

## 📊 Resumo dos Testes

### ✅ 34 Testes Automatizados

```
✓ Regras (11 testes)
  - Muito Frio
  - Muito Quente
  - Muito Seco
  - Muito Úmido
  - Confortável
  - Precisa de Sol
  - Precisa de Vento
  - Zona Adaptativa
  - Valores Limite
  - Tipo de Retorno
  - Validação de None

✓ Classifier (4 testes)
  - Criação
  - Tipo de Retorno
  - Validação
  - Coerência com Regras

✓ Decision Tree (8 testes)
  - Modelo Criado
  - Dataset Gerado
  - Labels Válidas
  - Treinamento
  - Previsões
  - Feature Importance
  - Profundidade
  - Número de Folhas

✓ Integração (2 testes)
  - Fluxo Completo
  - Coerência Regras vs Tree

✓ Dados (2 testes)
  - Dataset Válido
  - Sem Duplicatas

✓ Parametrizados (7 testes)
  - 7 casos comuns testados
```

---

## 📈 Resultado Esperado

```
============================= test session starts =============================
collected 34 items

tests/test_rules.py::TestRegras::test_muito_frio PASSED                  [  2%]
...
============================= 34 passed in 1.67s ==============================

✅ TODOS OS 34 TESTES PASSARAM!
```

---

## 🎯 Comandos Práticos

| Comando | Descrição |
|---------|-----------|
| `python run_tests.py all` | Todos os testes |
| `python run_tests.py rules` | Apenas regras |
| `python -m pytest tests/test_rules.py -v` | Verbose |
| `python -m pytest tests/test_rules.py -k "muito_frio" -v` | Filtrar por nome |
| `python -m pytest tests/test_rules.py --tb=short` | Erros resumidos |
| `pytest tests/test_rules.py --cov=src --cov-report=html` | Com cobertura |

---

## ✨ Recursos Disponíveis

### Documentos
- 📄 `TESTING_GUIDE.md` - Guia completo de testes
- 📄 `EVIDENCE_DECISION_TREE.md` - Atividade de modelagem
- 📄 `TECHNICAL_SUMMARY.md` - Análise técnica
- 📄 `DELIVERY_CHECKLIST.md` - Checklist de entrega

### Scripts
- 🐍 `run_tests.py` - Script Python (multiplataforma)
- 🔧 `run_tests.sh` - Script Shell (Linux/Mac)

### Visualizações
- 📊 `outputs/decision_tree.png` - Árvore completa (300 DPI)
- 📊 `outputs/decision_tree_compact.png` - Versão comprimida
- 📊 `outputs/dataset_decision_tree.csv` - Dataset usado

---

## 🎓 Conclusão

✅ **100% dos testes passando**
✅ **Sistema validado e pronto para uso**
✅ **Documentação completa**

**Atividade Concluída!** 🎉
