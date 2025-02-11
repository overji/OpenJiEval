import pandas as pd

def get_training_data():
    df = pd.read_parquet("hf://datasets/Kayamori/31C/data/train-00000-of-00001.parquet")
    for index, row in df.iterrows():
        df.loc[index, "image"] = row["image"]["path"]
    return df