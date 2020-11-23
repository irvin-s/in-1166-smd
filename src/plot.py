import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

print ("Plot from dataset")

plt.style.use("bmh")

df = pd.read_csv('../data/crx.data', sep=",")
df.columns
df.head()
df.info()