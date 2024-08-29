import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from streamlit_extras.no_default_selectbox import selectbox

st.title('Nutrition Calorie Tracker')

# Load data
try:
    df = pd.read_csv("./food.csv", encoding='mac_roman')
except FileNotFoundError:
    st.error("File not found. Please upload the food.csv file.")
    st.stop()
except pd.errors.EmptyDataError:
    st.error("The file is empty.")
    st.stop()
except Exception as e:
    st.error(f"An error occurred: {e}")
    st.stop()

# Input for number of dishes
ye = st.number_input('Enter Number of dishes', min_value=1, max_value=10)

# Initialize lists and variables
list1 = []
list2 = []
calories = 0

# Get user input for each dish
for i in range(ye):
    st.write("--------------------")
    sel = selectbox('Select the food', df['Food'].unique(), no_selection_label=" ", key=f'food_{i}')
    
    sel_serving = st.number_input(f'Select the number of servings for {sel}', min_value=1, max_value=10, value=1, step=1, key=f'serving_{i}')
    
    st.write("Food : ", sel)
    st.write("Serving : ", sel_serving)
    
    if sel in df['Food'].values:
        cal_per_serving = df[df['Food'] == sel]['Calories'].values[0]
        st.write("Calories per serving : ", cal_per_serving)
        
        cal = cal_per_serving * sel_serving
        list1.append(sel)
        list2.append(cal)
        calories += cal
        
        st.write(f"Total calories for {sel_serving} servings of {sel} = {cal} Calories")
    else:
        st.warning(f"{sel} is not in the food database.")
    
st.write("--------------------")
st.write(f"Total Calories: {calories}")

# Create pie chart
if list1 and list2:
    fig = go.Figure(data=[go.Pie(labels=list1, values=list2, textinfo='label+percent', insidetextorientation='radial')])
    fig.update_layout(title="Calorie Breakdown")
    st.plotly_chart(fig)
else:
    st.write("No data to display.")
