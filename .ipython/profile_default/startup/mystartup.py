# essentials
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

# less essential
import variants.snv as snv

# test DataFrame to manipulate
df = pd.DataFrame(np.arange(9).reshape((3,3)), columns=("A","B","C"), index=("a","b","c"))
df2 = sns.load_dataset("iris")
print("startup script: {}".format(__file__))
