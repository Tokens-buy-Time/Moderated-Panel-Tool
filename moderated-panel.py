import streamlit as st

# Title of the app
st.title("Moderated Panel Tool")

# Section for Panelists
st.header("Panel Setup")

panelist_name = []
panelist_expertise = []
panelist_emulated_individual = []
moderator_name = None

# Input for each panelist
for i in range(1, 8):  # Assuming 7 panelists maximum
    
    name = st.text_input(f"Panelist {i} Name:")
    expertise = st.text_input(f"Panelist {i} Area of Expertise:")
    emulated_individual = st.text_input(f"Panelist {i} Emulated Expert:")
    
    if st.checkbox(f"Is this panelist the Moderator?", key=f"mod_{i}"):
        moderator_name = name  # Assign this panelist as the moderator
        moderator_expertise = expertise
    else:
        panelist_name.append(name)
        panelist_expertise.append(expertise)
        panelist_emulated_individual.append(emulated_individual)
    
    st.write(" ")

# Button to finalize and generate the prompt
if st.button("Finalize Panel Setup"):
    
    if moderator_name is None:
        st.warning("Please select a moderator.")
    else:
        st.subheader("Copy the following prompt for ChatGPT:")

        # Prepare the prompt text
        prompt = f"""You are the moderator for a virtual expert panel discussion. 
        Your role is to create 20 questions and direct them to the appropriate panelists based on their expertise.
        
        Moderator: {moderator_name}, Expertise: {moderator_expertise}
        
        Panelists:
        """
        for i in range(len(panelist_name)):
            prompt += f"\nPanelist {i+1}: {panelist_name[i]}, Expertise: {panelist_expertise[i]}, Emulated Expert: {panelist_emulated_individual[i]}"
        
        prompt += "\n\nDiscussion Document: [Insert content from Moderators-Brief​⬤
