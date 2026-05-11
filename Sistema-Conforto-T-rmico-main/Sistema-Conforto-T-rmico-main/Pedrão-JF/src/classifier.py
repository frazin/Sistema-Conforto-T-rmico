from rules import classificar_conforto


class ThermalComfortClassifier:

    def predict(self, temperatura, umidade):
        return classificar_conforto(temperatura, umidade)