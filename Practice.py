import pandas as pd
import matplotlib.pyplot as plt
import kagglehub
from kagglehub import KaggleDatasetAdapter


def Project():
    try:
        path = kagglehub.dataset_download("caesarmario/our-world-in-data-covid19-dataset")
        print("Path to dataset files:", path)
        print('Okayy')

    except Exception as e:
        print(f"Hey the rror is {e}")


Project()
