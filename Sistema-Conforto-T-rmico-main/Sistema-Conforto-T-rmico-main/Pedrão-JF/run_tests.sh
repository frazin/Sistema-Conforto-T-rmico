#!/bin/bash
# Script de testes - Sistema de Conforto Térmico

echo "╔════════════════════════════════════════════════════════════╗"
echo "║         🧪 TESTES - Sistema de Conforto Térmico           ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

# Verificar se pytest está instalado
if ! command -v pytest &> /dev/null; then
    echo "📦 Instalando pytest..."
    pip install -q pytest
fi

echo "🏃 Executando 34 testes..."
echo ""

# Executar testes com verbose
python -m pytest tests/test_rules.py -v --tb=short

echo ""
echo "╔════════════════════════════════════════════════════════════╗"
echo "║                    ✅ TESTES CONCLUÍDOS                   ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

# Opções adicionais
echo "💡 Opções adicionais:"
echo "   - Testar apenas regras:      pytest tests/test_rules.py::TestRegras -v"
echo "   - Testar apenas classifier:  pytest tests/test_rules.py::TestClassifier -v"
echo "   - Testar apenas Decision Tree: pytest tests/test_rules.py::TestDecisionTree -v"
echo "   - Com cobertura:             pytest tests/test_rules.py --cov=src --cov-report=html"
echo ""
