import pandas as pd
import streamlit as st
tab1, tab2 = st.tabs(["Tasks", "Manage"])
with tab1:
    st.title("Work Organization")

    hardtask = st.data_editor
    minimaltask = st.data_editor
    easytask = st.data_editor

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
