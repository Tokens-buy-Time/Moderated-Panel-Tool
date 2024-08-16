import streamlit as st
import python as py
import pandas
inport numpty

# Title of the app
st.title("Moderated Panel Tool")

# Section for Moderator
st.header("Moderator")
moderators_name = st.text_input("Enter name of moderator")

# Section for Panelists
st.header("Panelists")
panelist_name = []
panelist_expertise = []
panelist_emulated_individual = []

for i in range(1, 7):  # Assuming 7 panelists maximum
    panelist_name.append(st.text_input(f"Panelist No. {i} name :"))
    panelist_expertise.append(st.text_input(f"Panelist No. {i} area of expertise :"))
    panelist_emulated_individual.append(st.text_input(f"Panelist No. {i} similar to :"))

# Display Responses
def panel_start
    if st.button(""):
        st.subheader("Panelist Responses:")
        for i, response in enumerate(panelist_responses):
            st.write(f"Panelist {i+1}: {panelist_name}")

# Section for Audience
st.header("Audience")
audience_question = st.text_input("Audience, ask a question:")

if st.button("Submit Audience Question"):
    st.write(f"Audience Question: {audience_question}")
