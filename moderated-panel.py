import streamlit as st
import pandas
import numpy

# Title of the app
st.title("Moderated Panel Tool")


# Section for Panelists
def panel("panelist_name", "panelist_expertise", panelist_emulated_individual")

st.header("Panelists")
panelist_name = []
panelist_expertise = []
panelist_emulated_individual = []

for i in range(1, 8):  # Assuming 7 panelists maximum

    = st.number_input(label="Panelists No.", value=st.session_state["panelist_name"][i])
    
    st.session_state["panelist_name"][i] = st.number_input(label="Panelists No.", value=st.session_state["panelist_name"][i])
    st.session_state["panelist_expertise"][i] = st.number_input(label="Panelists No.", value=st.session_state["panelist_expertise"][i])
    st.session_state["panelist_emulated_individual"][i] = st.number_input(label="Panelists No.", value=st.session_state["panelist_emulated_individual"][i])

    

    # Display Panelists
def panel_start():
    
    if st.button("List panelist"):
        
        st.subheader(" This session's panelist will be :-")
        
        for i, panel in enumerate(panelist_name):
            st.write(f"Panelist No. {i+1}: {panelist_name}")
    
    
    panelist_name.append(st.text_input(f"Panelist No. {i} name :"))
    panelist_expertise.append(st.text_input(f"Panelist No. {i} area of expertise :"))
    panelist_emulated_individual.append(st.text_input(f"Panelist No. {i} similar to :"))
    
    st.session_state["panelist_name"][i] = panelist_name[i]
    st.session_state["panelist_expertise"][i] = panelist_expertise[i]
    st.session_state["panelist_emulated_individual"][i] = panelist_emulated_individual[i]
    
    write(" ")



