from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt
from rules import classificar_conforto
import pandas as pd


class DecisionTreeModel:

    def __init__(self, max_depth=5):
        self.model = DecisionTreeClassifier(max_depth=max_depth, random_state=42)
        self.feature_names = ['temperatura', 'umidade']
        self.classes = []

    def train(self, X, y):
        self.model.fit(X, y)
        self.classes = self.model.classes_
        print(f"Modelo Decision Tree treinado com sucesso!")
        print(f"Profundidade da árvore: {self.model.get_depth()}")
        print(f"Número de folhas: {self.model.get_n_leaves()}")
        return self

    def predict(self, X):
        return self.model.predict(X)

    def visualize(self, output_path="outputs/decision_tree.png"):
        plt.figure(figsize=(25, 15))
        plot_tree(
            self.model,
            feature_names=self.feature_names,
            class_names=list(self.classes),
            filled=True,
            rounded=True,
            fontsize=10
        )
        plt.title("Árvore de Decisão - Sistema de Conforto Térmico", fontsize=16, fontweight='bold')
        plt.tight_layout()
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        print(f"Visualização da árvore salva em: {output_path}")
        plt.close()

    def get_feature_importance(self):
        importance = self.model.feature_importances_
        return dict(zip(self.feature_names, importance))


def generate_training_data(csv_path):
    df = pd.read_csv(csv_path)
    df = df.dropna()

    X = df[['temperatura', 'umidade']].values
    y = df.apply(lambda row: classificar_conforto(row['temperatura'], row['umidade']), axis=1).values

    return X, y, df


def generate_extended_dataset():
    data = []
    for temp in range(0, 40, 2):
        for umid in range(20, 95, 5):
            classif = classificar_conforto(temp, umid)
            data.append({'temperatura': temp, 'umidade': umid, 'classificacao': classif})

    df = pd.DataFrame(data)
    return df[['temperatura', 'umidade']].values, df['classificacao'].values, df
