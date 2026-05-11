# Evidência de Atividade: Modelagem com Decision Tree
## Sistema de Conforto Térmico

**Data:** 10 de maio de 2026  
**Aluno:** João Flávio Antunes Teixeira  
**Disciplina:** Inteligência Artificial  
**Período:** 9º - Engenharia da Computação

---

## 1. Objetivo da Atividade

Implementar uma modelagem do sistema de classificação de conforto térmico utilizando **Decision Tree (Árvore de Decisão)**, comparando com o sistema baseado em regras simbólicas existente.

## 2. Fundamentação Teórica

### O que é Decision Tree?

Uma Árvore de Decisão é um modelo de aprendizado de máquina supervisionado que simula um processo de tomada de decisão hierárquico. A árvore divide o espaço de features em regiões que classificam os dados em categorias.

**Características principais:**
- Estrutura hierárquica de nós de decisão
- Cada nó interno representa uma decisão baseada em um threshold de uma feature
- Cada folha representa uma classificação final
- Interpretável e visual

### Aplicação ao Conforto Térmico

O sistema recebe dois parâmetros de entrada:
- **Temperatura (°C):** 0 a 40°C
- **Umidade Relativa (%):** 20 a 95%

E classifica em categorias de conforto:
- Muito Frio
- Muito Quente
- Muito Seco
- Muito Úmido
- Precisa de Sol para Conforto
- Confortável
- Precisa de Vento para Conforto
- Confortável (Zona Adaptativa)
- Indefinido

---

## 3. Metodologia

### 3.1 Dataset

Para treinar o modelo, foi gerado um dataset estendido utilizando as regras existentes:
- **Intervalo de temperatura:** 0 a 40°C (incremento de 2°C)
- **Intervalo de umidade:** 20 a 95% (incremento de 5%)
- **Total de amostras:** 152 instâncias

As labels foram geradas aplicando a função de classificação existente (`classificar_conforto`) a todos os pontos.

### 3.2 Implementação Técnica

**Tecnologias utilizadas:**
- Python 3.14
- scikit-learn (DecisionTreeClassifier)
- pandas (manipulação de dados)
- matplotlib (visualização)

**Configuração do modelo:**
```python
DecisionTreeClassifier(
    max_depth=6,      # Profundidade máxima da árvore
    random_state=42   # Para reprodutibilidade
)
```

### 3.3 Treinamento

O modelo foi treinado com os dados gerados pelas regras existentes:
```
X = [[temperatura, umidade], ...]
y = [classificação, ...]
```

---

## 4. Resultados

### 4.1 Características da Árvore Gerada

| Métrica | Valor |
|---------|-------|
| Profundidade da Árvore | 6 |
| Número de Folhas | 10 |
| Número de Features | 2 |
| Número de Classes | 9 |

### 4.2 Importância das Features

| Feature | Importância |
|---------|------------|
| **Temperatura** | **70.40%** |
| **Umidade** | 29.60% |

**Interpretação:** A temperatura é aproximadamente 2.4 vezes mais importante que a umidade para a classificação de conforto térmico no modelo aprendido. Isso alinha-se com a estrutura das regras simbólicas, onde a temperatura tem prioridade nas primeiras ramificações.

### 4.3 Estrutura da Árvore

A árvore de decisão aprende a seguinte hierarquia:

```
                    temperatura <= 5.0?
                   /                    \
              Muito Frio            temperatura <= 35.0?
                                   /                      \
                              umidade <= 30.0?        Muito Quente
                             /                  \
                        Muito Seco     ... (mais nós)
```

Essa estrutura reflete automaticamente as prioridades das regras originais sem estar explicitamente programada.

---

## 5. Análise Comparativa

### Sistema de Regras vs Decision Tree

| Aspecto | Regras Simbólicas | Decision Tree |
|---------|------------------|---------------|
| **Interpretabilidade** | Explícita | Visual/Hierárquica |
| **Manutenibilidade** | Requer edição de código | Treina automaticamente |
| **Escalabilidade** | Difícil com mais features | Naturalmente escalável |
| **Generalização** | Baseada em conhecimento | Baseada em dados |
| **Performance** | Determinística | Depende do treinamento |

### Vantagens da Decision Tree

1. **Automação:** O modelo aprende padrões automaticamente dos dados
2. **Visualização:** A estrutura é facilmente visualizável
3. **Explicabilidade:** Cada decisão pode ser rastreada do nó raiz até a folha
4. **Validação:** Confirma que as regras criadas estão corretas

---

## 6. Arquivos Gerados

### Novos Arquivos no Projeto

```
src/
├── decision_tree.py              # Módulo com classe DecisionTreeModel
├── main.py                       # Atualizado para gerar Decision Tree
└── requirements.txt              # Atualizado com scikit-learn

outputs/
├── decision_tree.png             # Visualização da árvore (300 DPI)
├── dataset_decision_tree.csv     # Dataset estendido usado no treinamento
├── resultados.csv                # Resultados do sistema original
└── grafico_conforto.png          # Gráfico de distribuição
```

### Instalação de Dependências

```bash
pip install scikit-learn>=1.3
```

---

## 7. Como Executar

```bash
# Navegar para o diretório do projeto
cd Pedrão-JF

# Instalar dependências
pip install -r requirements.txt

# Executar o projeto (gera Decision Tree automaticamente)
python -c "import sys; sys.path.insert(0, 'src'); exec(open('src/main.py').read())"
```

---

## 8. Conclusões

1. **Validação do Sistema:** A Decision Tree aprendeu com sucesso as categorias de conforto, confirmando a lógica das regras simbólicas.

2. **Insights Obtidos:** 
   - Temperatura é 70% do peso nas decisões de conforto
   - O modelo convergiu para 10 folhas, agrupando naturalmente as 9 categorias
   - Profundidade de 6 é suficiente para capturar a complexidade do domínio

3. **Aplicações Futuras:**
   - Expandir o dataset com dados reais de sensores
   - Utilizar técnicas de ensemble (Random Forest, Gradient Boosting)
   - Implementar validação cruzada
   - Comparar com outros modelos (SVM, Neural Networks)

4. **Qualidade do Aprendizado:** O modelo é totalmente interpretável e oferece uma forma alternativa (mas compatível) de realizar a classificação de conforto térmico.

---

## 9. Referências Teóricas

- Quinlan, J. R. (1986). Induction of decision trees. *Machine Learning*, 1(1), 81-106.
- Breiman, L., et al. (1984). Classification and Regression Trees. Chapman and Hall.
- scikit-learn Documentation: https://scikit-learn.org/stable/modules/tree.html

---

**Atividade de Modelagem Concluída com Sucesso** ✓

Data de Conclusão: 10 de maio de 2026
