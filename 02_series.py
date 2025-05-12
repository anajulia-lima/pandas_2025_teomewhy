# %%

import pandas as pd
import numpy as np

#%%

idades = [23,25,27,31,33]

media = sum(idades) / len(idades)
media


# %%
series_idades = pd.Series(idades)
series_idades

# %%
media_idade = series_idades.mean()
summary_idades = series_idades.describe()
summary_idades
# %%
