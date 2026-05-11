import pandas as pd


class DataHandler:

    @staticmethod
    def load_data(path):
        return pd.read_csv(path)

    @staticmethod
    def save_data(df, path):
        df.to_csv(path, index=False)