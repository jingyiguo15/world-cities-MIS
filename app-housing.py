
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("housing.csv")

# Title
st.title("California Housing Data (1990) by Your Name")

# House value slider
min_value = st.slider(
    "Minimal Median House Value",
    min_value=0,
    max_value=500001,
    value=200000
)

# Subheader
st.subheader("See more filters in the sidebar:")

# Sidebar: location type
location_types = st.sidebar.multiselect(
    "Choose the location type",
    options=sorted(df["ocean_proximity"].dropna().unique()),
    default=sorted(df["ocean_proximity"].dropna().unique())
)

# Sidebar: income level
income_level = st.sidebar.radio(
    "Choose income level",
    ["Low", "Medium", "High"]
)

# Filter the data
filtered_df = df[
    (df["median_house_value"] >= min_value)
    & (df["ocean_proximity"].isin(location_types))
]

# Filter by income level
if income_level == "Low":
    filtered_df = filtered_df[
        filtered_df["median_income"] <= 2.5
    ]
elif income_level == "Medium":
    filtered_df = filtered_df[
        (filtered_df["median_income"] > 2.5)
        & (filtered_df["median_income"] < 4.5)
    ]
else:
    filtered_df = filtered_df[
        filtered_df["median_income"] >= 4.5
    ]

# Display the filtered map
st.map(filtered_df[["latitude", "longitude"]])

# Display the histogram
st.subheader("Distribution of Median House Values")

fig, ax = plt.subplots()
ax.hist(filtered_df["median_house_value"], bins=30)
ax.set_xlabel("Median House Value (USD)")
ax.set_ylabel("Number of Districts")
ax.set_title("Median House Value Histogram")

st.pyplot(fig)
plt.close(fig)