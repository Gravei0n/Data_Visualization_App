import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO

# Function to display information about different charts
def chart_info():
    st.sidebar.header("Chart Information")
    st.sidebar.write("### Pie Chart")
    st.sidebar.write("Use for categorical data to show proportions.")
    
    st.sidebar.write("### Bar Chart")
    st.sidebar.write("Use for categorical data to show comparisons.")
    
    st.sidebar.write("### Line Chart")
    st.sidebar.write("Use for time series data to show trends over time.")
    
    st.sidebar.write("### Scatter Plot")
    st.sidebar.write("Use for numerical data to show relationships between variables.")
    
    st.sidebar.write("### Histogram")
    st.sidebar.write("Use for numerical data to show distributions.")

# Function to generate visualizations
def generate_visualizations(df):
    st.write("## Generated Visualizations")

    if st.checkbox("Show DataFrame"):
        st.write(df)

    # Pie Chart
    if 'category' in df.columns:
        st.write("### Pie Chart")
        pie_data = df['category'].value_counts()
        fig, ax = plt.subplots()
        ax.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%')
        st.pyplot(fig)

    # Bar Chart
    if 'category' in df.columns:
        st.write("### Bar Chart")
        bar_data = df['category'].value_counts()
        fig, ax = plt.subplots()
        sns.barplot(x=bar_data.index, y=bar_data.values, ax=ax)
        st.pyplot(fig)

    # Line Chart
    if 'date' in df.columns and 'value' in df.columns:
        st.write("### Line Chart")
        fig, ax = plt.subplots()
        sns.lineplot(x='date', y='value', data=df, ax=ax)
        st.pyplot(fig)

    # Scatter Plot
    numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns
    if len(numerical_columns) >= 2:
        st.write("### Scatter Plot")
        fig, ax = plt.subplots()
        sns.scatterplot(x=numerical_columns[0], y=numerical_columns[1], data=df, ax=ax)
        st.pyplot(fig)

    # Histogram
    if len(numerical_columns) >= 1:
        st.write("### Histogram")
        fig, ax = plt.subplots()
        sns.histplot(df[numerical_columns[0]], bins=10, kde=True, ax=ax)
        st.pyplot(fig)

# Streamlit App
st.title("Data Visualization App")
st.write("Upload your data to generate relevant visualizations.")

# Sidebar for chart information
chart_info()

# File uploader
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # Read the uploaded file
    df = pd.read_csv(uploaded_file)
    generate_visualizations(df)


