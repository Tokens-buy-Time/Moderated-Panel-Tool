import streamlit as st
import python as py
import pandas
import numpy

# Title of the app
st.title("Moderated Panel Tool")


# Section for Panelists
st.header("Panelists")
panelist_name = []
panelist_expertise = []
panelist_emulated_individual = []

for i in range(1, 7):  # Assuming 7 panelists maximum
    panelist_name.append(st.text_input(f"Panelist No. {i} name :"))
    panelist_expertise.append(st.text_input(f"Panelist No. {i} area of expertise :"))
    panelist_emulated_individual.append(st.text_input(f"Panelist No. {i} similar to :"))

# Display Panelists
def panel_start():
    if st.button("List panelist"):
        st.subheader(" This session's panelist will be :-")
        for i, panel in enumerate(panelist_name):
            st.write(f"Panelist No. {i+1}: {panelist_name}")

