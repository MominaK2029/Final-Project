import streamlit as st
import pandas as pd 
st.title("Work Organizer")
easy = {
    "Name": ["Task", "Task", "Task"],
    "Coins": [0, 0, 0,],
}

df = pd.DataFrame(easy)


# Configure columns (optional)
column_config = {
    "Task": st.column_config.TextColumn("Task", help="Enter a Task"),
    "Coins": st.column_config.SelectboxColumn(
        "-",
        options=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25"],
        help="Select the number of coins"
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
st.subheader("Updated Data")
st.write(edited_df)

# Example: Save changes to CSV
if st.button("Save Changes"):
    edited_df.to_csv("updated_data.csv", index=True)
    st.success("Data saved to updated_data.csv")
