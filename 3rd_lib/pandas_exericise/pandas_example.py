import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

local_dict = {'A': 1, 'B': pd.Timestamp(
    '20200422'), 'C': pd.Series(1, index=list(range(4)), dtype='float32')}

my_df = pd.DataFrame(local_dict)

print(my_df)