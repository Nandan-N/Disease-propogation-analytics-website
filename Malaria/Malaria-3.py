import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('bmh')
df = pd.read_csv('Tuberculosis_final.csv')

x = df['cases']
y = df['Districts']

plt.title('Scatter Plot for Tuberculosis Cases')
plt.xlabel('Cases')
plt.ylabel('Districts')
plt.scatter(x, y)