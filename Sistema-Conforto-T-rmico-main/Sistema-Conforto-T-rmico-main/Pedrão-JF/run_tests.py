#!/usr/bin/env python
"""
Script para executar testes - Sistema de Conforto Térmico
Compatível com Windows e Linux
"""

import subprocess
import sys
import os

def print_header():
    print("╔════════════════════════════════════════════════════════════╗")
    print("║         🧪 TESTES - Sistema de Conforto Térmico           ║")
    print("╚════════════════════════════════════════════════════════════╝")
    print()

def print_footer():
    print()
    print("╔════════════════════════════════════════════════════════════╗")
    print("║                    ✅ TESTES CONCLUÍDOS                   ║")
    print("╚════════════════════════════════════════════════════════════╝")
    print()

def ensure_pytest():
    """Verifica e instala pytest se necessário"""
    try:
        import pytest
    except ImportError:
        print("📦 Instalando pytest...")
        try:
            # Tentar com uv (gerenciador moderno)
            subprocess.check_call(["uv", "pip", "install", "-q", "pytest"])
        except (FileNotFoundError, subprocess.CalledProcessError):
            # Fallback para pip com --break-system-packages
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", "--break-system-packages", "-q", "pytest"])
            except subprocess.CalledProcessError:
                print("❌ Falha ao instalar pytest. Execute manualmente:")
                print("   uv pip install pytest")
                print("   ou")
                print("   pip install --break-system-packages pytest")
                sys.exit(1)

def run_tests(test_type="all"):
    """Executa testes"""
    print_header()

    ensure_pytest()

    # Definir o caminho dos testes
    test_path = "tests/test_rules.py"

    if test_type == "all":
        print("🏃 Executando 34 testes...")
    elif test_type == "rules":
        print("🏃 Executando testes de regras...")
        test_path += "::TestRegras"
    elif test_type == "classifier":
        print("🏃 Executando testes de classifier...")
        test_path += "::TestClassifier"
    elif test_type == "tree":
        print("🏃 Executando testes de Decision Tree...")
        test_path += "::TestDecisionTree"
    elif test_type == "integration":
        print("🏃 Executando testes de integração...")
        test_path += "::TestIntegracao"

    print()

    # Executar pytest
    result = subprocess.run(
        [sys.executable, "-m", "pytest", test_path, "-v", "--tb=short"],
        capture_output=False
    )

    print_footer()

    print("💡 Opções adicionais:")
    print("   run_tests.py all           # Todos os testes")
    print("   run_tests.py rules         # Apenas regras")
    print("   run_tests.py classifier    # Apenas classifier")
    print("   run_tests.py tree          # Apenas Decision Tree")
    print("   run_tests.py integration   # Apenas integração")
    print()

    return result.returncode

if __name__ == "__main__":
    test_type = sys.argv[1] if len(sys.argv) > 1 else "all"
    sys.exit(run_tests(test_type))
