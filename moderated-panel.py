import streamlit as st

# Title of the app
st.title("Moderated Panel Tool")

# Section for Moderator
st.header("Moderator")
moderator_question = st.text_input("Enter your question for the panel:")

# Section for Panelists
st.header("Panelists")
panelist_responses = []
for i in range(1, 4):  # Assuming 3 panelists for simplicity
    panelist_responses.append(st.text_input(f"Panelist {i} response:"))

# Display Responses
if st.button("Submit Responses"):
    st.subheader("Panelist Responses:")
    for i, response in enumerate(panelist_responses):
        st.write(f"Panelist {i+1}: {response}")

# Section for Audience
st.header("Audience")
audience_question = st.text_input("Audience, ask a question:")

if st.button("Submit Audience Question"):
    st.write(f"Audience Question: {audience_question}")
