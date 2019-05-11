import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
np.random.seed(42)

Dict = {}
Dict['Type'] = ['Type 1']*175 + ['Type 2']*525
Dict['Area'] = ["Middle East"]*50 + ['East Asia']*125 + ["Middle East"]*300 + ['East Asia']*225
Dict['age_at_onset'] = (list(np.random.normal(15,5,175))+list(np.random.normal(40,7,525)))
Dict['Weight'] = (list(np.random.normal(20,3,300)+40)+list(np.random.normal(40,3,400)+30))
df = pd.DataFrame(Dict)
df = df.sample(700).reset_index(drop=True)
df.age_at_onset = [-x if x < 0 else x for x in df.age_at_onset]
df.age_at_onset = [x+10 if x < 5 else x for x in df.age_at_onset]
