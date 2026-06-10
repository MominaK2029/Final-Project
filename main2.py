import streamlit as st
import pandas as pd 
st.title("Tester")
easy = {
    "Name": ["Task", "Task", "Task"],
    "Coins": [0, 0, 0,],
}

df = pd.DataFrame(easy)

st.title("Editable Table with Streamlit Data Editor")

# Configure columns (optional)
column_config = {
    "Task": st.column_config.TextColumn("Task", help="Enter a Task"),
    "Coins": st.column_config.SelectboxColumn(
        "-",
        options=["1", "2", "3", "4"],
        help="Select the person's role"
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
    edited_df.to_csv("updated_data.csv", index=False)
    st.success("Data saved to updated_data.csv")