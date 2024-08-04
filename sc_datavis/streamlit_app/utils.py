from io import BytesIO

import pandas as pd
import streamlit as st


def file_to_df(file: BytesIO | None) -> pd.DataFrame | None:
    if file is not None:
        file_extension = file.name.split(".")[-1]
        if file_extension == "csv":
            df = pd.read_csv(file)
        elif file_extension == "xlsx":
            df = pd.read_excel(file)
        elif file_extension == "json":
            df = pd.read_json(file)
        else:
            st.error("Invalid file format. Please upload a CSV, Excel, or JSON")
            return None
        return df
    return None


def render_file_uploader():
    uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx", "json"])

    if uploaded_file is not None:
        st.session_state.uploaded_file = uploaded_file
    elif "uploaded_file" not in st.session_state:
        st.error("Please upload a file to visualise")
        st.session_state.uploaded_file = None
