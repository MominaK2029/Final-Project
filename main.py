import streamlit as st
import pandas as pd
st.title("Work Organization")

hardtask = st.data_editor({})
minimaltask = st.data_editor({})
easytask = st.data_editor({})

hardtask = pd.DataFrame({
    'Hard Task':["Clean the house"]
})
minimaltask = pd.DataFrame({
    'Minimal Task':["Broom the house"]
})
easytask = pd.DataFrame({
    'Easy Task':["Lock the door"]
})

search_query1 = st.text_input("Search Type", placeholder="Type here... ex: Hard")

if search_query1.strip().lower() == "Easy":
    st.write(f"Results for '{search_query1}':")
    st.dataframe(easytask, hide_index=True)
else:
    st.write("Showing all records:")
    st.dataframe(easytask, hide_index=True)