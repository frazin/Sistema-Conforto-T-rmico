from classifier import ThermalComfortClassifier
from data_handler import DataHandler
from visualization import Visualizer


def main():

    classifier = ThermalComfortClassifier()

    df = DataHandler.load_data("data/sample_input.csv")

    df["classificacao"] = df.apply(
        lambda x: classifier.predict(x["temperatura"], x["umidade"]),
        axis=1
    )

    DataHandler.save_data(df, "outputs/resultados.csv")

    Visualizer.plot_results(df)

    print("Projeto executado com sucesso!")


if __name__ == "__main__":
    main()