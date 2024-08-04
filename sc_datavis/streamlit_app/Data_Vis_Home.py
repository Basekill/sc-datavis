import io

import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import streamlit as st

from sc_datavis.streamlit_app.utils import file_to_df, render_file_uploader

st.set_page_config(page_title="EDA Dashboard", layout="wide")
st.title("Exploratory Data Analysis Dashboard")

render_file_uploader()
df = file_to_df(st.session_state.uploaded_file)

if df is not None:
    with st.expander("Data Information"):
        buf = io.StringIO()
        df.info(buf=buf)
        st.markdown(buf.getvalue())

    with st.expander("Summary Statistics"):
        st.write(df.describe())

    with st.expander("Missing Values"):
        st.write(df.isnull().sum())

    with st.expander("First Few Rows"):
        st.write(df.head())

    with st.expander("Correlation Heatmap"):
        fig, ax = plt.subplots(figsize=(12, 10))
        sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)

    # Distribution plots for numerical columns
    with st.expander("Distribution Plots"):
        numerical_cols = df.select_dtypes(include=["int64", "float64"]).columns
        for col in numerical_cols:
            fig = px.histogram(
                df, x=col, marginal="box", nbins=30, title=f"Distribution of {col}"
            )
            st.plotly_chart(fig)

    # Box plots for numerical columns
    with st.expander("Box Plots"):
        for col in numerical_cols:
            fig = px.box(df, y=col, title=f"Box Plot of {col}")
            st.plotly_chart(fig)

    # Bar plots for categorical columns
    with st.expander("Bar Plots"):
        categorical_cols = df.select_dtypes(include=["object"]).columns
        for col in categorical_cols:
            value_counts = df[col].value_counts().reset_index()
            value_counts.columns = [col, "count"]
            fig = px.bar(value_counts, x=col, y="count", title=f"Bar Plot of {col}")
            st.plotly_chart(fig)

    # Scatter plot matrix
    with st.expander("Scatter Plot Matrix"):
        fig = px.scatter_matrix(
            df, dimensions=numerical_cols, title="Scatter Plot Matrix"
        )
        st.plotly_chart(fig)
