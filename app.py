import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title='Airplanes Crash Data', layout="wide")


df = pd.read_excel(io='plane_crash_info_cleaned.xlsx', sheet_name='Sheet1',usecols='A:Q', nrows=5064)

#st.dataframe(df)

# side bar

# ------Filters------
st.sidebar.header("Please Filter Here:")
years = df['year'].unique()
#year = st.sidebar.multiselect("Select the Year:", options=df["year"].unique(), default=df["year"].unique())
year = st.sidebar.select_slider("Select the Year Range", options=years, value=[1908, 2023])


#df_selection = df.query("year == @year")
df_selection = df.query("year >= @year[0] and year <= @year[1]")

#st.dataframe(df_selection)


#------Page total KPIs------
st.title(":red[All Accidents] from 1908 to 2023")
st.markdown('##')

total_accidentes = len(df)
total_aboard_fatalities = int(df['Aboard_Fatalities'].sum())
total_ground_fatalities = int(df['Ground_Fatalities'].sum())
total_fatalities = int(df['Total_Fatalites'].sum())

left_columnn, middle_column, md_column, right_column = st.columns(4)
with left_columnn:
    st.metric(label='Number of Accidents', value=total_accidentes)
    #st.subheader('Total Accidents')
    #st.subheader(f"{total_accidentes:,}")
with middle_column:
    st.metric(label='Aboard Fatalities', value=total_aboard_fatalities)
    #st.subheader('Aboard Fatalities')
    #st.subheader(total_aboard_fatalities)
with md_column:
    st.metric(label='Ground Fatalities', value=total_ground_fatalities)
    #st.subheader('Ground Fatalities')
    #st.subheader(total_ground_fatalities)
with right_column:
    st.metric(label='Total Fatalites', value=total_fatalities)
    #st.subheader('Total Fatalites')
    #st.subheader(total_fatalities)


st.markdown('---')



# ------total selected years------
st.title("Total for :red[Selected Year(s)]")
st.markdown('##')

#---total accidents---
total_accidentes = len(df_selection)
percente_acc = len(df_selection) / len(df) * 100
percent_acc_formatted = "{:.2f}%".format(round(percente_acc, 2))

#---Total aboard fatalities---
total_aboard_fatalities = int(df_selection['Aboard_Fatalities'].sum())

#---Total ground fatalities---
total_ground_fatalities = int(df_selection['Ground_Fatalities'].sum())

#---Total fatalities---
total_fatalities = int(df_selection['Total_Fatalites'].sum())


left_columnn, middle_column, md_column, right_column = st.columns(4)
with left_columnn:
    st.metric(label='Number of Accidents', value=total_accidentes, delta=percent_acc_formatted, delta_color='off')
    #st.subheader('Total Accidents')
    #st.subheader(total_accidentes)
with middle_column:
    st.metric(label='Aboard Fatalities', value=total_aboard_fatalities)
    #st.subheader('Aboard Fatalities')
    #st.subheader(total_aboard_fatalities)
    #st.subheader(percent_fata_formatted)
with md_column:
    st.metric(label='Ground Fatalities', value=total_ground_fatalities)
    #st.subheader('Ground Fatalities')
    #st.subheader(total_ground_fatalities)
with right_column:
    st.metric(label='Total Fatalites', value=total_fatalities)
    #st.subheader('Total Fatalites')
    #st.subheader(total_fatalities)

st.markdown('---')

 

 ## ------Data viz------

left_columnn, middle_column, md_column, right_column = st.columns(4)

fatalities_by_year = df.groupby(by=['year']).sum()


chart_fatalities_by_year = px.line(fatalities_by_year, x=fatalities_by_year.index, y=fatalities_by_year['Total_Fatalites'], width=800, height=700, title="<b>Total Deaths by Year</b>")

with left_columnn:
    st.plotly_chart(chart_fatalities_by_year)


# group by the "Operator" column and count the occurrences of each unique value
operator_counts = df_selection.groupby("Operator").size().reset_index(name='Accidents')

# sort the operator_counts dataframe by 'counts' column in descending order
operator_counts = operator_counts.sort_values(by='Accidents', ascending=False)

# take only the top 10 values
top_10 = operator_counts.head(10)

chart_operators = px.bar(top_10, x='Operator', y='Accidents', width=800, height=700, title="<b>Top 10 Airlines with Accidents</b>")

with middle_column:
    st.plotly_chart(chart_operators)