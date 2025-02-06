import io
import pandas as pd
from PIL import Image


def get_training_data():
    df = pd.read_parquet("hf://datasets/Kayamori/31C/data/train-00000-of-00001.parquet")
    image_data = (df["image"].iloc[0])["bytes"]
    image_stream = io.BytesIO(image_data)
    image = Image.open(image_stream)
    image.show()