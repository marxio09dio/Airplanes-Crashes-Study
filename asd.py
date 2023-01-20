import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title='EHehehe', layout="wide")


df = pd.read_excel(io='Data/plane_crash_info_cleaned.xlsx', engine='openpyxl', sheet_name='Sheet1',usecols='A:Q', nrows=5064)

st.dataframe(df)

# side bar

st.sidebar.header("Please Filter Here:")
city = st.sidebar.multiselect("Select the Year:", options=df["year"].unique(), default=df["year"].unique())

#customer_type = st.sidebar.multiselect(
#    "Select the Location:",
#    options=df["Location"].unique(),
#    default=df["Location"].unique(),
#)

#gender = st.sidebar.multiselect(
#    "Select the Operator:",
#    options=df["Operator"].unique(),
#    default=df["Operator"].unique()
#)

df_selection = df.query("year == @year") #& Location ==@Location & Operator == @Operator")