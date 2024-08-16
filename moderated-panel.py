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
if 'stage' not in st.session_state:
    st.session_state['stage'] = 'panel_setup'
if 'briefing_text' not in st.session_state:
    st.session_state['briefing_text'] = ""

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

# Function to handle document upload
def load_briefing_document():
    try:
        with open("Moderators-Brief.txt", "r") as file:
            briefing_text = file.read()
        st.session_state['briefing_text'] = briefing_text
        st.success("Document 'Moderators-Brief.txt' loaded successfully!")
    except FileNotFoundError:
        st.error("File 'Moderators-Brief.txt' not found. Please make sure it's in the correct directory.")

# Function to generate questions for panelists
def generate_questions():
    if 'briefing_text' in st.session_state:
        st.header("Generated Questions")

        # Replace this with GPT-4 API logic to generate questions based on briefing text
        for i, panelist_expertise in enumerate(st.session_state['panelist_expertises']):
            st.write(f"**Questions for {st.session_state['panelist_names'][i]} (Expertise: {panelist_expertise}):**")
            # Simulate generating questions (replace with GPT-4)
            for j in range(1, 6):  # Assuming 5 questions per panelist
                st.write(f"Question {j}: [Generated Question based on briefing for {panelist_expertise}]")

# Panelist setup stage
if st.session_state['stage'] == 'panel_setup':
    st.header("Add Panelists")
    add_panelist()
    display_panelists()

    if st.button("Proceed to Load Briefing Document"):
        st.session_state['stage'] = 'upload_briefing'

# Load briefing document stage
elif st.session_state['stage'] == 'upload_briefing':
    load_briefing_document()

    if 'briefing_text' in st.session_state and st.session_state['briefing_text']:
        if st.button("Generate Questions"):
            st.session_state['stage'] = 'generate_questions'

# Generate questions stage
elif st.session_state['stage'] == 'generate_questions':
    generate_questions()
