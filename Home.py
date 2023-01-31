import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title='Airplanes Crash Data', layout="wide")

st.title("Home")

st.header('The accidents inluded are:')
st.caption('Civil and commercial aviation accidents of scheduled and non-scheduled passenger airliners worldwide, which resulted in a fatality (including all U.S. Part 121 and Part 135 fatal accidents)')
st.caption("Cargo, positioning, ferry and test flight fatal accidents.")
st.caption("Military transport accidents with 10 or more fatalities.")
st.caption("Commercial and military helicopter accidents with greater than 10 fatalities.")
st.caption("Civil and military airship accidents involving fatalities.")
st.caption("Aviation accidents involving the death of famous people.")
st.caption("Aviation accidents or incidents of noteworthy interest.")

    

df = pd.read_excel(io='Data/plane_crash_info_cleaned.xlsx', sheet_name='Sheet1',usecols='A:Q', nrows=5064)


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
 

 ## ------Data viz------

fatalities_by_year = df.groupby(by=['Year']).sum()

chart_fatalities_by_year = px.line(fatalities_by_year, x=fatalities_by_year.index, y=fatalities_by_year['Total_Fatalites'], width=1400, height=700, title="<b>Total Deaths by Year</b>")

st.plotly_chart(chart_fatalities_by_year)



### --- operator viz

# group by the "Operator" column and count the occurrences of each unique value
operator_counts = df.groupby("Operator").size().reset_index(name='Accidents')

# sort the operator_counts dataframe by 'counts' column in descending order
operator_counts = operator_counts.sort_values(by='Accidents', ascending=False)

# take only the top 10 values
top_10 = operator_counts.head(10)

chart_operators = px.bar(top_10, x='Operator', y='Accidents', width=1400, height=700, title="<b>Top 10 Airlines with Accidents</b>")

st.plotly_chart(chart_operators)





### --- Ac_type viz
AC_Type_c = df.groupby("AC_Type").size().reset_index(name='AC_Type_c')
AC_Type_c = AC_Type_c.sort_values(by='AC_Type_c', ascending=False)
AC_Type_top = AC_Type_c.head(10)

chart_AC_Type_top = px.bar(AC_Type_top, x='AC_Type', y='AC_Type_c', width=1400, height=700, title="<b>Top 10 AC Type involved in Accidents</b>")

st.plotly_chart(chart_AC_Type_top)






