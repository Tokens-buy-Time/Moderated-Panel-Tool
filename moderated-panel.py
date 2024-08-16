import streamlit as st

# Title of the app
st.title("Moderated Panel Tool")

# Initialize session state for panelists if it doesn't exist
if 'panelist_data' not in st.session_state:
    st.session_state['panelist_data'] = []

# Function to capture panelist details
def add_panelist():
    panelist_name = st.text_input("Panelist Name", key="panelist_name")
    panelist_expertise = st.text_input("Panelist Expertise", key="panelist_expertise")
    panelist_emulated_individual = st.text_input("Emulated Individual", key="panelist_emulated_individual")

    if st.button("Add Panelist"):
        if panelist_name and panelist_expertise and panelist_emulated_individual:
            st.session_state['panelist_data'].append({
                'name': panelist_name,
                'expertise': panelist_expertise,
                'emulated': panelist_emulated_individual
            })
            st.success("Panelist Added!")
        else:
            st.error("Please fill all the fields.")

# Function to display added panelists
def display_panelists():
    st.subheader("Panelists in This Session")
    for i, panelist in enumerate(st.session_state['panelist_data']):
        st.write(f"**Panelist {i + 1}:** {panelist['name']} - Expertise: {panelist['expertise']} - Emulates: {panelist['emulated']}")

# Adding Panelist Section
st.header("Add Panelists")
add_panelist()

# Display Panelists Section
if st.session_state['panelist_data']:
    display_panelists()
