import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.title('California Housing Data (1990) by Yongbin Kang')
df = pd.read_csv('housing.csv')


median_house_value_filter = st.slider('Median House Price:', 0, 50001, 20000)  # min, max, default

# create a multi select
location_filter = st.sidebar.multiselect(
     'Choose the location type',
     df.ocean_proximity.unique(),  # options
     df.ocean_proximity.unique(),)  # defaults




genre = st.sidebar.radio(
    "Choose income level",
    ('Low', 'Medium', 'High'))

if genre == 'Low':
    df = df[df.median_income <= 2.5]
elif genre == 'Medium':
    df = df[(df.median_income > 2.5) & (df.median_income < 4.5)]
else:
    df = df[df.median_income >= 4.5]
    


# filter by median_income
df = df[df.median_house_value >= median_house_value_filter]

# filter by location
df = df[df.ocean_proximity.isin(location_filter)]



# show on map
st.map(df)

# show the plot
st.subheader('Histogram of the Median House Value')
fig, ax = plt.subplots(figsize=(20, 5))
df.median_house_value.hist(bins=30)
st.pyplot(fig)