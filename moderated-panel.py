import streamlit as st

# Title of the app
st.title("Moderated Panel Tool")

# Initialize empty lists to store panelist details
panelist_names = []
panelist_expertises = []
panelist_emulated_individuals = []

# Function to add panelist details
def add_panelist():
    panelist_name = st.text_input("Panelist Name")
    panelist_expertise = st.text_input("Panelist Expertise")
    panelist_emulated_individual = st.text_input("Emulated Individual")

    if st.button("Add Panelist"):
        if panelist_name and panelist_expertise and panelist_emulated_individual:
            panelist_names.append(panelist_name)
            panelist_expertises.append(panelist_expertise)
            panelist_emulated_individuals.append(panelist_emulated_individual)
            st.success(f"Panelist '{panelist_name}' Added!")
        else:
            st.error("Please fill in all the fields.")

# Function to display added panelists
def display_panelists():
    st.subheader("Panelists in This Session")
    for i in range(len(panelist_names)):
        st.write(f"**Panelist {i + 1}:** {panelist_names[i]} - Expertise: {panelist_expertises[i]} - Emulates: {panelist_emulated_individuals[i]}")

# Display panelist form
st.header("Add Panelists")
add_panelist()

# Display the list of panelists
display_panelists()
