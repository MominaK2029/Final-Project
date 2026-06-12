import streamlit as st
import pandas as pd
tab1, tab2 = st.tabs(["Tasks", "Manage"])
with tab1:
    st.title("Work Organization")
    if 'df' not in st.session_state:
        
        st.session_state.df = pd.DataFrame({"Tasks": ["Type a task", "Type a task"], "Reward": [4, 4]})
        
# 2. Assign the editor to a variable or handle edits using a callback
    edited_df = st.data_editor(st.session_state.df, hide_index=True, num_rows="dynamic")

# 3. Use the updated variable for the rest of your app
    st.write("'Fall seven times, stand up eight.' — Japanese Proverb")
