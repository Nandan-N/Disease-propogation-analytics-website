import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('bmh')
df = pd.read_csv('Tuberculosis_final.csv')

plt.title("Heat Map for Tuberculosis Death numbers")
plt.xlabel("cases")
plt.ylabel("Year")

heat = df.pivot('Year','Districts','Death numbers')
sns.heatmap(heat)
