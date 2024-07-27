import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import folium
from streamlit_folium import folium_static
import plotly.graph_objects as go
from wordcloud import WordCloud

# Function to display information about different charts
def chart_info():
    st.sidebar.header("Chart Information")
    st.sidebar.write("### Bar Chart")
    st.sidebar.write("Used to compare different categories of data.")
    
    st.sidebar.write("### Line Chart")
    st.sidebar.write("Ideal for showing trends over time.")
    
    st.sidebar.write("### Pie Chart")
    st.sidebar.write("Useful for showing proportions and percentages.")
    
    st.sidebar.write("### Histogram")
    st.sidebar.write("Used to show the distribution of a dataset.")
    
    st.sidebar.write("### Scatter Plot")
    st.sidebar.write("Shows the relationship between two variables.")
    
    st.sidebar.write("### Bubble Chart")
    st.sidebar.write("A variation of a scatter plot where the size of the bubbles represents an additional dimension of the data.")
    
    st.sidebar.write("### Area Chart")
    st.sidebar.write("Similar to a line chart, but the area below the line is filled in.")
    
    st.sidebar.write("### Heatmap")
    st.sidebar.write("Displays data in a matrix format with colors representing the values.")
    
    st.sidebar.write("### Tree Map")
    st.sidebar.write("Used to display hierarchical data as a set of nested rectangles.")
    
    st.sidebar.write("### Box Plot")
    st.sidebar.write("Shows the distribution of data based on a five-number summary (minimum, first quartile, median, third quartile, and maximum).")
    
    st.sidebar.write("### Violin Plot")
    st.sidebar.write("Combines aspects of box plots and kernel density plots to show data distributions.")
    
    st.sidebar.write("### Donut Chart")
    st.sidebar.write("A variation of the pie chart with a hole in the center.")
    
    st.sidebar.write("### Waterfall Chart")
    st.sidebar.write("Used to show cumulative effects of sequentially introduced positive or negative values.")
    
    st.sidebar.write("### Gantt Chart")
    st.sidebar.write("Used for project management to show the schedule of tasks or activities.")
    
    st.sidebar.write("### Map Visualization")
    st.sidebar.write("Geographic data displayed on maps (e.g., choropleth maps).")
    
    st.sidebar.write("### Sankey Diagram")
    st.sidebar.write("Used to visualize flows and their quantities in a system.")
    
    st.sidebar.write("### Radar Chart")
    st.sidebar.write("Displays multivariate data in the form of a two-dimensional chart.")
    
    st.sidebar.write("### Sunburst Chart")
    st.sidebar.write("A radial equivalent of a tree map.")
    
    st.sidebar.write("### Bullet Chart")
    st.sidebar.write("Used for comparing a metric against a target.")
    
    st.sidebar.write("### Bubble Map")
    st.sidebar.write("Combines bubble charts and map visualizations to show the geographical distribution of data points.")
    
    st.sidebar.write("### Network Diagram")
    st.sidebar.write("Displays relationships between different entities in a network.")
    
    st.sidebar.write("### Chord Diagram")
    st.sidebar.write("Visualizes the inter-relationships between data in a matrix format.")
    
    st.sidebar.write("### Timeline")
    st.sidebar.write("Shows a sequence of events in chronological order.")
    
    st.sidebar.write("### Word Cloud")
    st.sidebar.write("Visual representation of text data where the size of each word indicates its frequency or importance.")

# Function to generate visualizations
def generate_visualizations(df):
    st.write("## Generated Visualizations")

    if st.checkbox("Show DataFrame"):
        st.write(df)

    chart_type = st.selectbox("Select Chart Type", ["Bar Chart", "Line Chart", "Pie Chart", "Histogram", "Scatter Plot",
                                                    "Bubble Chart", "Area Chart", "Heatmap", "Tree Map", "Box Plot", 
                                                    "Violin Plot", "Donut Chart", "Waterfall Chart", "Gantt Chart", 
                                                    "Map Visualization", "Sankey Diagram", "Radar Chart", "Sunburst Chart", 
                                                    "Bullet Chart", "Bubble Map", "Network Diagram", "Chord Diagram", 
                                                    "Timeline", "Word Cloud"])

    columns = df.columns.tolist()

    if chart_type == "Bar Chart":
        x_col = st.selectbox("Select X Column", columns)
        y_col = st.selectbox("Select Y Column", columns)
        fig = px.bar(df, x=x_col, y=y_col)
        st.plotly_chart(fig)

    elif chart_type == "Line Chart":
        x_col = st.selectbox("Select X Column", columns)
        y_col = st.selectbox("Select Y Column", columns)
        fig = px.line(df, x=x_col, y=y_col)
        st.plotly_chart(fig)

    elif chart_type == "Pie Chart":
        names_col = st.selectbox("Select Names Column", columns)
        values_col = st.selectbox("Select Values Column", columns)
        fig = px.pie(df, names=names_col, values=values_col)
        st.plotly_chart(fig)

    elif chart_type == "Histogram":
        x_col = st.selectbox("Select X Column", columns)
        fig = px.histogram(df, x=x_col)
        st.plotly_chart(fig)

    elif chart_type == "Scatter Plot":
        x_col = st.selectbox("Select X Column", columns)
        y_col = st.selectbox("Select Y Column", columns)
        fig = px.scatter(df, x=x_col, y=y_col)
        st.plotly_chart(fig)

    elif chart_type == "Bubble Chart":
        x_col = st.selectbox("Select X Column", columns)
        y_col = st.selectbox("Select Y Column", columns)
        size_col = st.selectbox("Select Size Column", columns)
        fig = px.scatter(df, x=x_col, y=y_col, size=size_col)
        st.plotly_chart(fig)

    elif chart_type == "Area Chart":
        x_col = st.selectbox("Select X Column", columns)
        y_col = st.selectbox("Select Y Column", columns)
        fig = px.area(df, x=x_col, y=y_col)
        st.plotly_chart(fig)

    elif chart_type == "Heatmap":
        st.write("Heatmap requires two categorical columns and one numerical column.")
        x_col = st.selectbox("Select X Column", columns)
        y_col = st.selectbox("Select Y Column", columns)
        z_col = st.selectbox("Select Z Column", columns)
        fig = px.density_heatmap(df, x=x_col, y=y_col, z=z_col)
        st.plotly_chart(fig)

    elif chart_type == "Tree Map":
        path_col = st.selectbox("Select Path Column", columns)
        values_col = st.selectbox("Select Values Column", columns)
        fig = px.treemap(df, path=[path_col], values=values_col)
        st.plotly_chart(fig)

    elif chart_type == "Box Plot":
        y_col = st.selectbox("Select Y Column", columns)
        x_col = st.selectbox("Select X Column", columns)
        fig = px.box(df, y=y_col, x=x_col)
        st.plotly_chart(fig)

    elif chart_type == "Violin Plot":
        y_col = st.selectbox("Select Y Column", columns)
        x_col = st.selectbox("Select X Column", columns)
        fig = px.violin(df, y=y_col, x=x_col)
        st.plotly_chart(fig)

    elif chart_type == "Donut Chart":
        names_col = st.selectbox("Select Names Column", columns)
        values_col = st.selectbox("Select Values Column", columns)
        fig = px.pie(df, names=names_col, values=values_col, hole=0.3)
        st.plotly_chart(fig)

    elif chart_type == "Waterfall Chart":
        x_col = st.selectbox("Select X Column", columns)
        y_col = st.selectbox("Select Y Column", columns)
        fig = go.Figure(go.Waterfall(
            x = df[x_col],
            y = df[y_col]
        ))
        st.plotly_chart(fig)

    elif chart_type == "Gantt Chart":
        st.write("Gantt Chart requires columns for task names, start and end dates.")
        task_col = st.selectbox("Select Task Column", columns)
        start_col = st.selectbox("Select Start Date Column", columns)
        end_col = st.selectbox("Select End Date Column", columns)
        fig = px.timeline(df, x_start=start_col, x_end=end_col, y=task_col)
        st.plotly_chart(fig)

    elif chart_type == "Map Visualization":
        st.write("Map Visualization requires columns for latitude and longitude.")
        lat_col = st.selectbox("Select Latitude Column", columns)
        lon_col = st.selectbox("Select Longitude Column", columns)
        map_df = df[[lat_col, lon_col]].dropna()
        map_center = [map_df[lat_col].mean(), map_df[lon_col].mean()]
        m = folium.Map(location=map_center, zoom_start=2)
        for idx, row in map_df.iterrows():
            folium.Marker([row[lat_col], row[lon_col]]).add_to(m)
        folium_static(m)

    elif chart_type == "Sankey Diagram":
        st.write("Sankey Diagram requires columns for source, target, and value.")
        source_col = st.selectbox("Select Source Column", columns)
        target_col = st.selectbox("Select Target Column", columns)
        value_col = st.selectbox("Select Value Column", columns)
        fig = go.Figure(go.Sankey(
            node=dict(
                pad=15,
                thickness=20,
                line=dict(color="black", width=0.5),
                label=df[source_col].append(df[target_col]).unique()
            ),
            link=dict(
                source=df[source_col].map({k: i for i, k in enumerate(df[source_col].append(df[target_col]).unique())}),
                target=df[target_col].map({k: i for i, k in enumerate(df[source_col].append(df[target_col]).unique())}),
                value=df[value_col]
            )
        ))
        st.plotly_chart(fig)

    elif chart_type == "Radar Chart":
        st.write("Radar Chart requires multiple numerical columns.")
        num_cols = st.multiselect("Select Numerical Columns", columns)
        fig = go.Figure()
        for col in num_cols:
            fig.add_trace(go.Scatterpolar(r=df[col], theta=num_cols, fill='toself', name=col))
        st.plotly_chart(fig)

    elif chart_type == "Sunburst Chart":
        st.write("Sunburst Chart requires hierarchical path columns and a value column.")
        path_cols = st.multiselect("Select Path Columns", columns)
        values_col = st.selectbox("Select Values Column", columns)
        fig = px.sunburst(df, path=path_cols, values=values_col)
        st.plotly_chart(fig)

    elif chart_type == "Bullet Chart":
        st.write("Bullet Chart requires columns for measure and target.")
        measure_col = st.selectbox("Select Measure Column", columns)
        target_col = st.selectbox("Select Target Column", columns)
        fig = go.Figure(go.Indicator(
            mode="number+gauge+delta", value=df[measure_col].mean(),
            delta={'reference': df[target_col].mean()},
            gauge={'shape': "bullet"}))
        st.plotly_chart(fig)

    elif chart_type == "Bubble Map":
        st.write("Bubble Map requires columns for latitude, longitude, and size.")
        lat_col = st.selectbox("Select Latitude Column", columns)
        lon_col = st.selectbox("Select Longitude Column", columns)
        size_col = st.selectbox("Select Size Column", columns)
        fig = px.scatter_geo(df, lat=lat_col, lon=lon_col, size=size_col)
        st.plotly_chart(fig)

    elif chart_type == "Network Diagram":
        st.write("Network Diagram requires columns for source, target, and weight.")
        source_col = st.selectbox("Select Source Column", columns)
        target_col = st.selectbox("Select Target Column", columns)
        weight_col = st.selectbox("Select Weight Column", columns)
        fig = go.Figure(go.Sankey(
            node=dict(
                pad=15,
                thickness=20,
                line=dict(color="black", width=0.5),
                label=df[source_col].append(df[target_col]).unique()
            ),
            link=dict(
                source=df[source_col].map({k: i for i, k in enumerate(df[source_col].append(df[target_col]).unique())}),
                target=df[target_col].map({k: i for i, k in enumerate(df[source_col].append(df[target_col]).unique())}),
                value=df[weight_col]
            )
        ))
        st.plotly_chart(fig)

    elif chart_type == "Chord Diagram":
        st.write("Chord Diagram requires columns for source, target, and value.")
        source_col = st.selectbox("Select Source Column", columns)
        target_col = st.selectbox("Select Target Column", columns)
        value_col = st.selectbox("Select Value Column", columns)
        fig = go.Figure(go.Chord(
            df[source_col], df[target_col], df[value_col]
        ))
        st.plotly_chart(fig)

    elif chart_type == "Timeline":
        st.write("Timeline requires columns for events and dates.")
        event_col = st.selectbox("Select Event Column", columns)
        date_col = st.selectbox("Select Date Column", columns)
        fig = px.timeline(df, x_start=date_col, x_end=date_col, y=event_col)
        st.plotly_chart(fig)

    elif chart_type == "Word Cloud":
        st.write("Word Cloud requires a column for text data.")
        text_col = st.selectbox("Select Text Column", columns)
        text = " ".join(df[text_col].dropna().astype(str))
        wordcloud = WordCloud().generate(text)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        st.pyplot()

# Streamlit App
st.title("Advanced Data Visualization App")
st.write("Upload your data to generate relevant visualizations.")

# Sidebar for chart information
chart_info()

# File uploader
uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx"])
if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith(".xlsx"):
            df = pd.read_excel(uploaded_file)
        
        generate_visualizations(df)
    
    except Exception as e:
        st.error(f"Error: {e}")
