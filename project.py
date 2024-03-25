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



