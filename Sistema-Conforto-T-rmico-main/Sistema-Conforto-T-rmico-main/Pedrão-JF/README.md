# Sistema de Conforto Térmico (IA baseada em regras + Decision Tree)

Projeto desenvolvido para a disciplina de Inteligência Artificial.

## Descrição

Este sistema utiliza um conjunto de regras simbólicas para classificar condições de conforto térmico com base em temperatura e umidade relativa do ar. Agora inclui uma **modelagem com Decision Tree** como upgrade para validação e análise da estrutura de decisão.

## 🆕 Upgrade: Decision Tree Modeling

A partir da versão 2.0, o sistema agora inclui:
- Treinamento de Decision Tree baseada nas regras existentes
- Visualização em alta resolução (300 DPI) da árvore completa
- Análise de importância das features
- Dataset estendido para treinamento
- Documentação completa da atividade de modelagem

**Arquivos de evidência:**
- `EVIDENCE_DECISION_TREE.md` - Documentação detalhada da atividade
- `TECHNICAL_SUMMARY.md` - Sumário técnico e análise de desempenho

## Tecnologias

- Python 3.14
- Pandas
- Matplotlib
- Scikit-learn (novo)

## Execução

### Instalar dependências:

```bash
pip install -r requirements.txt
```

### Rodar o sistema:

```bash
cd Pedrão-JF
python -c "import sys; sys.path.insert(0, 'src'); exec(open('src/main.py').read())"
```

### Saída gerada:

```
--- Gerando Decision Tree ---
Modelo Decision Tree treinado com sucesso!
Profundidade da árvore: 6
Número de folhas: 10
Visualização da árvore salva em: outputs/decision_tree.png
Importância das features: {'temperatura': 0.704, 'umidade': 0.296}
Projeto executado com sucesso!
```

## Estrutura

```
Pedrão-JF/
├── data/
│   └── sample_input.csv
├── outputs/
│   ├── resultados.csv                    # Classificações do sistema original
│   ├── decision_tree.png                 # Árvore completa (300 DPI)
│   ├── decision_tree_compact.png         # Versão comprimida
│   └── dataset_decision_tree.csv         # Dataset de treinamento
├── src/
│   ├── classifier.py
│   ├── data_handler.py
│   ├── decision_tree.py                  # (novo) Módulo Decision Tree
│   ├── main.py                           # (atualizado)
│   ├── rules.py
│   └── visualization.py
├── tests/
│   └── test_rules.py
├── requirements.txt                       # (atualizado)
├── EVIDENCE_DECISION_TREE.md             # (novo) Documentação da atividade
├── TECHNICAL_SUMMARY.md                  # (novo) Análise técnica
└── README.md                             # Este arquivo

```

## Resultados da Modelagem Decision Tree

### Métricas do Modelo
- **Profundidade:** 6
- **Número de folhas:** 10
- **Features:** 2 (temperatura, umidade)
- **Classes:** 9 categorias de conforto

### Importância das Features
- **Temperatura:** 70.4% 🔴
- **Umidade:** 29.6% 💧

A temperatura é aproximadamente 2.4x mais importante que a umidade para a classificação.

### Validação
- Dataset: 152 amostras
- Acurácia: ~95%
- Concordância com regras originais: 95%

## Autor

João Flávio Antunes Teixeira . Aluno 9° período de Engenharia da Computação

## Versão

- v1.0 - Sistema original com regras simbólicas
- **v2.0 - Upgrade com Decision Tree** ⭐ (Atual)

---

**Atividade de Modelagem Concluída:** Data 10 de maio de 2026 ✓
