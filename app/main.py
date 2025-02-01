import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load data
@st.cache_data
def load_data():
    file_path = "data/gym_membership.csv"  # Update path if necessary
    return pd.read_csv(file_path)

df = load_data()

# Streamlit UI
st.title("Gym Membership Data Insights")

# Data Overview
st.subheader("Dataset Overview")
st.write(df.head())
st.write("Summary Statistics:")
st.write(df.describe())

# Age Distribution
st.subheader("Age Distribution")
fig = px.histogram(df, x='Age', nbins=20, title='Age Distribution')
st.plotly_chart(fig)

# Membership Type Distribution
st.subheader("Membership Type Distribution")
fig = px.bar(df['abonoment_type'].value_counts(), title='Membership Type Count')
st.plotly_chart(fig)

# New Insights
st.subheader("Additional Insights")

# Correlation Heatmap
st.write("### Correlation Heatmap")
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig)

# Visits per week vs. Membership Type
st.write("### Visits per Week by Membership Type")
fig = px.box(df, x='abonoment_type', y='visit_per_week', title='Visits per Week by Membership Type')
st.plotly_chart(fig)

# Gender Distribution
st.write("### Gender Distribution")
fig = px.pie(df, names='gender', title='Gender Ratio')
st.plotly_chart(fig)
