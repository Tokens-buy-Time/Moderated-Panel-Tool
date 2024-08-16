import streamlit as st
from PyPDF2 import PdfReader

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
def upload_briefing_document():
    st.header("Upload Briefing Document")
    uploaded_file = st.file_uploader("Choose a file", type=["pdf", "txt"])

    if uploaded_file is not None:
        if uploaded_file.type == "application/pdf":
            reader = PdfReader(uploaded_file)
            briefing_text = ""
            for page in reader.pages:
                briefing_text += page.extract_text()
        else:
            briefing_text = uploaded_file.read().decode('utf-8')

        st.session_state['briefing_text'] = briefing_text
        st.success("Document uploaded successfully!")

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

    if st.button("Proceed to Upload Briefing Document"):
        st.session_state['stage'] = 'upload_briefing'

# Upload briefing document stage
elif st.session_state['stage'] == 'upload_briefing':
    upload_briefing_document()

    if 'briefing_text' in st.session_state:
        if st.button("Generate Questions"):
            st.session_state['stage'] = 'generate_questions'

# Generate questions stage
elif st.session_state['stage'] == 'generate_questions':
    generate_questions()
