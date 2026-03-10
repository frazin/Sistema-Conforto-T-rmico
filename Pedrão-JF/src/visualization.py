import matplotlib.pyplot as plt


class Visualizer:

    @staticmethod
    def plot_results(df):

        counts = df["classificacao"].value_counts()

        plt.figure(figsize=(8,5))
        counts.plot(kind="bar")

        plt.title("Distribuição de Conforto Térmico")
        plt.xlabel("Categoria")
        plt.ylabel("Quantidade")

        plt.tight_layout()

        plt.savefig("outputs/grafico_conforto.png")
        plt.close()