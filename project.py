import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns 
plt.style.use('ggplot')
pd.set_option('display.max_columns',200)

#reading Data
df = pd.read_csv(r'C:\Users\dani_\OneDrive\Escritorio\DataAnalystYoutube\ProjectRollerCoaster\coaster_db.csv')

#understanding Data
print(df.shape)

#showing the head of our table
print(df.head())

#showing name of columns
print(df.columns)

#datatypes of columns
print(df.dtypes)

#info about our dataset
print(df.describe())




