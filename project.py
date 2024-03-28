import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns 
plt.style.use('ggplot')
pd.set_option('display.max_columns',200)

#reading Data
df = pd.read_csv(r'C:\Users\dani_\OneDrive\Escritorio\DataAnalystYoutube\ProjectRollerCoaster\coaster_db.csv')

#Understanding Data
#size of the table
print(df.shape)

#showing the head of our table
print(df.head())

#showing name of columns
print(df.columns)

#datatypes of columns
print(df.dtypes)

#info about our dataset
print(df.describe())


#Data Prep

#print(df.columns)

df = df[['coaster_name', 
    #'Length', 'Speed', 
    'Location', 'Status', #'Opening date', 'Type',
    'Manufacturer', #'Height restriction', 'Model', 'Height',
       #'Inversions', 'Lift/launch system', 'Cost', 'Trains', 'Park section',
       #'Duration', 'Capacity', 'G-force', 'Designer', 'Max vertical angle',
       #'Drop', 'Soft opening date', 'Fast Lane available', 'Replaced',
       #'Track layout', 'Fastrack available', 'Soft opening date.1',
       #'Closing date', 'Opened', 'Replaced by', 'Website',
       #'Flash Pass Available', 'Must transfer from wheelchair', 'Theme',
       #'Single rider line available', 'Restraint Style',
       #'Flash Pass available', 'Acceleration', 'Restraints', 'Name',
       'year_introduced', 'latitude', 'longitude', 'Type_Main',
       'opening_date_clean', #'speed1', 'speed2', 'speed1_value', 'speed1_unit',
       'speed_mph', #'height_value', 'height_unit', 
       'height_ft',
       'Inversions_clean', 'Gforce_clean']].copy()

print(df.columns)

print(df.shape)
print(df.dtypes)

df['opening_date_clean'] = pd.to_datetime(df['opening_date_clean'])
print(df.dtypes)

#Rename our columns 
df = df.rename(columns={'coaster_name':'Coaster_Name','year_introduced':'Year_Introduced','opening_date_clean':'Opening_Date','latitude':'Latitude','longitude':'Longitude',
                'speed_mph':'Speed_mph','height_ft':'Height_ft','Inversions_clean':'Inversions','Gforce_clean':'Gforce'})

print(df.columns)

#checking null values
print(df.isna().sum())

#checking duplicates
print(df.loc[df.duplicated()])

#checking duplicates in a subset
print(df.loc[df.duplicated(subset="Coaster_Name")].head(5))

#reviewing details
print(df.query('Coaster_Name=="Crystal Beach Cyclone"'))

#
df = df.loc[~df.duplicated(subset=['Coaster_Name','Location','Opening_Date'])].reset_index(drop=True).copy()
print(df)


print(df['Year_Introduced'].value_counts())

plt.figure(figsize=(6, 4))
top_years = df['Year_Introduced'].value_counts().head(10)
top_years.plot.bar()

# Plot bar plot of top 10 Year_Introduced
plt.title('Top 10 Years Coasters Introduced')
plt.xlabel('Year Introduced')
plt.ylabel('Count')
plt.show()

# Plot histogram of Speed_mph with 20 bins
plt.figure(figsize=(6, 4))
plt.hist(df['Speed_mph'], bins=20)
plt.xlabel('Speed (mph)')
plt.ylabel('Frequency')
plt.title('Histogram of Coaster Speeds')
plt.show()

# Plot KDE plot of Speed_mph
plt.figure(figsize=(6, 4))
sns.kdeplot(df['Speed_mph'])
plt.xlabel('Speed (mph)')
plt.ylabel('Density')
plt.title('Kernel Density Estimation (KDE) Plot of Coaster Speeds')
plt.show()


# scatter plot of Speed_mph vs. Height_ft
plt.figure(figsize=(6, 4))
plt.scatter(df['Speed_mph'], df['Height_ft'])
plt.xlabel('Speed (mph)')
plt.ylabel('Height (ft)')
plt.title('Coaster Speeds vs. Heights')
plt.show()


# scatter plot with Seaborn
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Speed_mph', y='Height_ft', hue='Year_Introduced', data=df)
plt.xlabel('Speed (mph)')
plt.ylabel('Height (ft)')
plt.title('Coaster Speeds vs. Heights (Colored by Year Introduced)')
plt.legend(title='Year Introduced')
plt.show()

# Creating pair plot

# Selecting variables of interest
vars_of_interest = ['Year_Introduced', 'Speed_mph', 'Height_ft', 'Inversions', 'Gforce']

sns.pairplot(df, vars=['Year_Introduced', 'Speed_mph', 'Height_ft', 'Inversions', 'Gforce'], hue='Type_Main')
plt.suptitle('Pair Plot of Coaster Variables with Type_Main Hue', y=1.02)
plt.show()






