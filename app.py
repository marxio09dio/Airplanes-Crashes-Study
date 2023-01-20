import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title='Airplanes Crash Data', layout="wide")


df = pd.read_excel(io='Data/plane_crash_info_cleaned.xlsx', engine='openpyxl', sheet_name='Sheet1',usecols='A:Q', nrows=5064)

st.dataframe(df)

# side bar

# Filters
st.sidebar.header("Please Filter Here:")
year = st.sidebar.multiselect("Select the Year:", options=df["year"].unique(), default=df["year"].unique())


df_selection = df.query("year == @year")

st.dataframe(df_selection)


#Page
st.title("Accidentes Dashboard")
st.markdown('##')

#Needs review
total_accidentes = len(df)
total_fatalities = int(df['Total_Fatalites'].sum())

left_columnn, middle_column, right_column = st.columns(3)
with left_columnn:
        st.subheader('Total Accidentes')
        st.subheader(total_accidentes)
with middle_column:
    st.subheader('Total Fatalites')
    st.subheader(total_fatalities)





 