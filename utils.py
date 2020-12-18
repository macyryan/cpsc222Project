import pandas as pd
import numpy as np
import matplot.pylot as plt

def read_file(file): 
    df = pd.read_csv(file, header=0)
    file.close()
    return df


