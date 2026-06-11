import pandas as pd
import streamlit as st
tab1, tab2 = st.tabs(["Tasks", "Manage"])
with tab1:
    st.title("Work Organization")

    hardtask = st.data_editor
    minimaltask = st.data_editor
    easytask = st.data_editor

    hardtask = pd.DataFrame({
        'Hard Task':["Clean the house"],
        'Coins':["14"]
    })
    minimaltask = pd.DataFrame({
        'Minimal Task':["Broom the house"],
        'Coins':["8"] 
    })
    easytask = pd.DataFrame({
        'Easy Task':["Lock the door"],
        'Coins':["4"]
    })

    search_query1 = st.text_input("Search Type of Task", placeholder="Type here... ex: Minimal")

    if search_query1.strip().lower() == "easy":
        st.write(f"Results for '{search_query1}':")
        st.dataframe(easytask, hide_index=True)
    elif search_query1.strip().lower() == "minimal":
        st.write(f"Results for '{search_query1}':")
        st.dataframe(minimaltask, hide_index=True)
    elif search_query1.strip().lower() == "hard":
        st.write(f"Results for '{search_query1}':")
        st.dataframe(hardtask, hide_index=True)

    else:
        st.write("Showing all records:")
        st.dataframe(easytask, hide_index=True)
        st.dataframe(minimaltask, hide_index=True)
        st.dataframe(hardtask, hide_index=True)
with tab2:
    task = st.selectbox("Section..", options=["Easy", "Minimal", "Hard"])
    if task == "Easy":
        search = st.text_input("Type in your task")
    elif task == "Minimal":
        search = st.text_input("Type in your task")
    else:
        task == "Hard"
        search = st.text_input("Type in your task") 
