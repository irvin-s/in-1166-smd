import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

print ("Plot from dataset")

plt.style.use('ggplot')

df = pd.read_csv('../data/crx.data', sep=',')
#df.columns
#df.head()
#df.info()


#Histograma 1
#df.columns
#df.head()
#df.info()
df.groupby('a16')['a16'].count()


#Histograma 2