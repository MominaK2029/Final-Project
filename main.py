import pandas as pd
import streamlit as st
tab1, tab2, tab3 = st.tabs(["Tasks", "Shop", "Manage"])
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

    if search_query1.strip().lower() == "Easy":
        st.write(f"Results for '{search_query1}':")
        st.dataframe(easytask, hide_index=True)
        filtered_easy = easytask[
            easytask['Easy Task'].str.contains(search_query1, case=False) 
            ]
        st.write(f"Results for '{search_query1}':")
        st.dataframe(filtered_easy, hide_index=True)
    elif search_query1.strip().lower() == "Minimal":
        st.write(f"Results for '{search_query1}':")
        st.dataframe(hardtask, hide_index=True)
    elif search_query1.strip().lower() == "Hard":
        st.write(f"Results for '{search_query1}':")
        st.dataframe(hardtask, hide_index=True)
    else:
        st.write("Showing all records:")
        st.dataframe(easytask, hide_index=True)
        st.dataframe(minimaltask, hide_index=True)
        st.dataframe(hardtask, hide_index=True)
with tab3:
    task = st.menu_button("Section..", options=["Easy", "Minimal", "Hard"])
    if task.strip().lower() == "Easy":
        search = st.text_input("Type in your task")
    elif task.strip().lower() == "Minimal":
        search = st.text_input("Type in your task")
    else:
        task.strip().lower() == "Minimal"
        search = st.text_input("Type in your task") 
