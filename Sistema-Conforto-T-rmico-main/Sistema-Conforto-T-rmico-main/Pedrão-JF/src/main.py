from classifier import ThermalComfortClassifier
from data_handler import DataHandler
from visualization import Visualizer
from decision_tree import DecisionTreeModel, generate_extended_dataset


def main():

    classifier = ThermalComfortClassifier()

    df = DataHandler.load_data("data/sample_input.csv")

    df["classificacao"] = df.apply(
        lambda x: classifier.predict(x["temperatura"], x["umidade"]),
        axis=1
    )

    DataHandler.save_data(df, "outputs/resultados.csv")

    Visualizer.plot_results(df)

    # Novo: Treinamento e visualização da Decision Tree
    print("\n--- Gerando Decision Tree ---")
    X, y, df_extended = generate_extended_dataset()

    dt_model = DecisionTreeModel(max_depth=6)
    dt_model.train(X, y)

    # Visualizar a árvore
    dt_model.visualize("outputs/decision_tree.png")

    # Importância das features
    importances = dt_model.get_feature_importance()
    print(f"Importância das features: {importances}")

    # Salvar dataset estendido
    DataHandler.save_data(df_extended, "outputs/dataset_decision_tree.csv")

    print("Projeto executado com sucesso!")


if __name__ == "__main__":
    main()