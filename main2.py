import streamlit as st
import pandas as pd 
st.title("Work Organizer")
easy = {
    "Task": ["Task", "Task", "Task"],
    "Coins": [0, 0, 0,],
    "Check off": [False, False, False]
}

df = pd.DataFrame(easy)


# Configure columns (optional)
column_config = {
    "Task": st.column_config.TextColumn("Task", help="Enter a Task"),
    "Coins": st.column_config.SelectboxColumn(
        "# of Coins",
        options=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25"],
        help="Select the number of coins"),
    "selected": st.column_config.CheckboxColumn(
            label="Select",
            help="Check to include this row in the filtered results.",
            default=False,
    )
}

# Display editable table
edited_df = st.data_editor(
    df,
    column_config=column_config,
    hide_index=True,
    num_rows="dynamic"  # Allows adding/removing rows
)

# Show the updated DataFrame
st.subheader("Completed tasks")
if "Check off" in edited_df.columns and edited_df["Check Off"].dtype == bool:
    filterlist_df = edited_df[edited_df["Check Off"] == True]
else: filterlist_df = pd.DataFrame()
st.Data_Frame(filterlist_df)
