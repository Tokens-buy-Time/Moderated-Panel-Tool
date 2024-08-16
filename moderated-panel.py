import streamlit as st

# Title of the app
st.title("Moderated Panel Tool")

# Initialize session state for storing panelists if it doesn't already exist
if 'panelist_names' not in st.session_state:
    st.session_state['panelist_names'] = []
if 'panelist_expertises' not in st.session_state:
    st.session_state['panelist_expertises'] = []
if 'panelist_emulated_individuals' not in st.session_state:
    st.session_state['panelist_emulated_individuals'] = []

# Function to add panelist details
def add_panelist():
    panelist_name = st.text_input("Panelist Name")
    panelist_expertise = st.text_input("Panelist Expertise")
    panelist_emulated_individual = st.text_input("Emulated Individual")

    if st.button("Add Panelist"):
        if panelist_name and panelist_expertise and panelist_emulated_individual:
            st.session_state['panelist_names'].append(panelist_name)
            st.session_state['panelist_expertises'].append(panelist_expertise)
            st.session_state['panelist_emulated_individuals'].append(panelist_emulated_individual)
            st.success(f"Panelist '{panelist_name}' Added!")
        else:
            st.error("Please fill in all the fields.")

# Function to display added panelists
def display_panelists():
    st.subheader("Panelists in This Session")
    for i in range(len(st.session_state['panelist_names'])):
        st.write(f"**Panelist {i + 1}:** {st.session_state['panelist_names'][i]} - Expertise: {st.session_state['panelist_expertises'][i]} - Emulates: {st.session_state['panelist_emulated_individuals'][i]}")

# Display panelist form
st.header("Add Panelists")
add_panelist()

# Display the list of panelists
display_panelists()
