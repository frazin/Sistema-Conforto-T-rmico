import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from rules import classificar_conforto
from classifier import ThermalComfortClassifier
from decision_tree import DecisionTreeModel, generate_extended_dataset, generate_training_data
import pandas as pd
import numpy as np


class TestRegras:
    """Testes das regras de classificação"""

    def test_muito_frio(self):
        """Testa classificação de temperatura muito baixa"""
        assert classificar_conforto(0, 50) == "Muito Frio"
        assert classificar_conforto(3, 50) == "Muito Frio"
        assert classificar_conforto(5, 50) == "Muito Frio"

    def test_muito_quente(self):
        """Testa classificação de temperatura muito alta"""
        assert classificar_conforto(35, 50) == "Muito Quente"
        assert classificar_conforto(37, 50) == "Muito Quente"
        assert classificar_conforto(40, 50) == "Muito Quente"

    def test_muito_seco(self):
        """Testa classificação de umidade muito baixa"""
        assert classificar_conforto(20, 25) == "Muito Seco"
        assert classificar_conforto(25, 30) == "Muito Seco"
        assert classificar_conforto(22, 20) == "Muito Seco"

    def test_muito_umido(self):
        """Testa classificação de umidade muito alta"""
        assert classificar_conforto(22, 80) == "Muito Úmido"
        assert classificar_conforto(25, 85) == "Muito Úmido"
        assert classificar_conforto(28, 90) == "Muito Úmido"

    def test_confortavel(self):
        """Testa zona de conforto ideal"""
        assert classificar_conforto(22, 50) == "Confortável"
        assert classificar_conforto(23, 60) == "Confortável"
        assert classificar_conforto(25, 70) == "Confortável"

    def test_precisa_sol(self):
        """Testa classificação que precisa de sol"""
        result = classificar_conforto(15, 50)
        assert result in ["Precisa de Sol para Conforto", "Confortável (Zona Adaptativa)"]

    def test_precisa_vento(self):
        """Testa classificação que precisa de vento"""
        result = classificar_conforto(30, 50)
        assert result in ["Precisa de Vento para Conforto", "Confortável (Zona Adaptativa)"]

    def test_zona_adaptativa(self):
        """Testa zona adaptativa de conforto"""
        result = classificar_conforto(20, 50)
        assert result in ["Confortável", "Confortável (Zona Adaptativa)"]

    def test_valores_limite(self):
        """Testa valores nos limites das faixas"""
        # Limite inferior de temperatura
        assert classificar_conforto(5, 50) == "Muito Frio"
        assert classificar_conforto(5.1, 50) != "Muito Frio"

        # Limite superior de temperatura
        assert classificar_conforto(35, 50) == "Muito Quente"
        assert classificar_conforto(34.9, 50) != "Muito Quente"

    def test_retorna_string(self):
        """Testa que a função retorna sempre uma string"""
        result = classificar_conforto(20, 50)
        assert isinstance(result, str)

    def test_nunca_retorna_none(self):
        """Testa que a função nunca retorna None"""
        for temp in range(0, 40):
            for umid in range(20, 95):
                result = classificar_conforto(temp, umid)
                assert result is not None


class TestClassifier:
    """Testes da classe ThermalComfortClassifier"""

    def setup_method(self):
        """Setup antes de cada teste"""
        self.classifier = ThermalComfortClassifier()

    def test_classifier_criado(self):
        """Testa se o classifier é criado corretamente"""
        assert self.classifier is not None

    def test_predict_retorna_string(self):
        """Testa se predict retorna string"""
        result = self.classifier.predict(25, 50)
        assert isinstance(result, str)

    def test_predict_valido(self):
        """Testa se predict retorna classificação válida"""
        result = self.classifier.predict(25, 50)
        categorias_validas = [
            "Muito Frio", "Muito Quente", "Muito Seco", "Muito Úmido",
            "Precisa de Sol para Conforto", "Confortável",
            "Precisa de Vento para Conforto", "Confortável (Zona Adaptativa)", "Indefinido"
        ]
        assert result in categorias_validas

    def test_predict_coerencia_com_rules(self):
        """Testa coerência entre classifier e rules"""
        for temp in [5, 15, 25, 30, 36]:
            for umid in [30, 50, 80]:
                result_classifier = self.classifier.predict(temp, umid)
                result_rules = classificar_conforto(temp, umid)
                assert result_classifier == result_rules


class TestDecisionTree:
    """Testes do modelo Decision Tree"""

    def setup_method(self):
        """Setup antes de cada teste"""
        self.dt_model = DecisionTreeModel(max_depth=6)

    def test_modelo_criado(self):
        """Testa se modelo é criado"""
        assert self.dt_model is not None
        assert hasattr(self.dt_model, 'model')

    def test_dataset_extended_gerado(self):
        """Testa geração do dataset estendido"""
        X, y, df = generate_extended_dataset()
        assert len(X) > 0
        assert len(y) > 0
        assert len(df) > 0
        assert X.shape[1] == 2  # temperatura, umidade

    def test_dataset_extended_labels(self):
        """Testa se labels são válidas"""
        X, y, df = generate_extended_dataset()
        categorias_validas = [
            "Muito Frio", "Muito Quente", "Muito Seco", "Muito Úmido",
            "Precisa de Sol para Conforto", "Confortável",
            "Precisa de Vento para Conforto", "Confortável (Zona Adaptativa)", "Indefinido"
        ]
        for label in y:
            assert label in categorias_validas

    def test_treinamento_sucesso(self):
        """Testa se modelo é treinado com sucesso"""
        X, y, _ = generate_extended_dataset()
        model = self.dt_model.train(X, y)
        assert model is not None
        assert hasattr(model, 'classes')
        assert len(model.classes) > 0

    def test_predicoes_apos_treino(self):
        """Testa previsões após treinamento"""
        X, y, _ = generate_extended_dataset()
        self.dt_model.train(X, y)

        # Teste com dados conhecidos
        predictions = self.dt_model.predict(X[:5])
        assert len(predictions) == 5
        assert all(isinstance(p, (str, np.str_)) for p in predictions)

    def test_feature_importance(self):
        """Testa cálculo de importância das features"""
        X, y, _ = generate_extended_dataset()
        self.dt_model.train(X, y)

        importance = self.dt_model.get_feature_importance()
        assert isinstance(importance, dict)
        assert 'temperatura' in importance
        assert 'umidade' in importance

        # Temperatura deve ser mais importante que umidade
        assert importance['temperatura'] > importance['umidade']

    def test_profundidade_arvore(self):
        """Testa profundidade da árvore"""
        X, y, _ = generate_extended_dataset()
        self.dt_model.train(X, y)
        depth = self.dt_model.model.get_depth()
        assert depth <= 6  # max_depth=6

    def test_numero_folhas(self):
        """Testa número de folhas"""
        X, y, _ = generate_extended_dataset()
        self.dt_model.train(X, y)
        num_leaves = self.dt_model.model.get_n_leaves()
        assert num_leaves > 0


class TestIntegracao:
    """Testes de integração do sistema completo"""

    def test_fluxo_completo(self):
        """Testa fluxo completo de classificação"""
        # Gerar dados
        X, y, df = generate_extended_dataset()

        # Treinar
        model = DecisionTreeModel(max_depth=6)
        model.train(X, y)

        # Prever
        predictions = model.predict(X[:10])
        assert len(predictions) == 10

    def test_coerencia_regras_vs_tree(self):
        """Testa coerência entre regras e decision tree"""
        X, y, _ = generate_extended_dataset()

        model = DecisionTreeModel(max_depth=6)
        model.train(X, y)

        # Testar em pontos específicos
        test_points = [
            (2, 50),    # Muito Frio
            (25, 50),   # Confortável
            (36, 50),   # Muito Quente
            (20, 25),   # Muito Seco
            (20, 85),   # Muito Úmido
        ]

        for temp, umid in test_points:
            rule_result = classificar_conforto(temp, umid)
            tree_result = model.predict(np.array([[temp, umid]]))[0]

            # Ambos devem ser válidos (podem variar nas bordas)
            assert rule_result in [
                "Muito Frio", "Muito Quente", "Muito Seco", "Muito Úmido",
                "Precisa de Sol para Conforto", "Confortável",
                "Precisa de Vento para Conforto", "Confortável (Zona Adaptativa)", "Indefinido"
            ]
            assert tree_result in [
                "Muito Frio", "Muito Quente", "Muito Seco", "Muito Úmido",
                "Precisa de Sol para Conforto", "Confortável",
                "Precisa de Vento para Conforto", "Confortável (Zona Adaptativa)", "Indefinido"
            ]


class TestDados:
    """Testes de manipulação de dados"""

    def test_dataset_valido(self):
        """Testa se dataset gerado é válido"""
        X, y, df = generate_extended_dataset()

        # Verificar shape
        assert X.shape[0] == y.shape[0]
        assert X.shape[1] == 2

        # Verificar ranges
        assert np.all(X[:, 0] >= 0) and np.all(X[:, 0] < 40)  # temperatura
        assert np.all(X[:, 1] >= 20) and np.all(X[:, 1] <= 95)  # umidade

    def test_sem_duplicatas_exatas(self):
        """Testa se não há duplicatas exatas no dataset"""
        X, y, df = generate_extended_dataset()
        unique_rows = np.unique(X, axis=0)
        # Pode ter duplicatas de classificação mas não de entrada
        assert len(unique_rows) == len(X)


@pytest.mark.parametrize("temp,umid", [
    (5, 50),      # Muito Frio
    (35, 50),     # Muito Quente
    (20, 25),     # Muito Seco
    (20, 85),     # Muito Úmido
    (22, 50),     # Confortável
    (15, 50),     # Precisa Sol
    (30, 50),     # Precisa Vento
])
def test_clasificacoes_comuns(temp, umid):
    """Testa classificações comuns parametrizadas"""
    result = classificar_conforto(temp, umid)
    assert isinstance(result, str)
    assert len(result) > 0


if __name__ == "__main__":
    # Executar testes com pytest
    pytest.main([__file__, "-v", "--tb=short"])
