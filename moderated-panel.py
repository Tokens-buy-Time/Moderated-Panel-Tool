import streamlit as st
import openai

# Get the API key from Streamlit secrets
openai_api_key = st.secrets["General"]["OPENAI_API_KEY"]

# Title of the app
st.title("Moderated Panel Tool")

# Section for Panelists
st.header("Panel Setup")

# Add input fields and finalize the panel setup as before...

# Button to send prompt to OpenAI API
if st.button("Send Prompt to ChatGPT"):
    prompt = st.session_state['prompt']  # Assuming you've saved the prompt in session state

    try:
        response = openai.Completion.create(
            engine="gpt-4",  # or "gpt-3.5-turbo" if you have restrictions
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.7,
        )

        generated_text = response.choices[0].text.strip()

        st.subheader("Response from ChatGPT:")
        st.write(generated_text)

    except Exception as e:
        st.error(f"Error: {e}")



# Section for Panelists
st.header("Panel Setup")

panelist_name = []
panelist_expertise = []
panelist_emulated_individual = []
moderator_name = None

# Input for each panelist
for i in range(1, 8):  # Assuming 7 panelists plus moderator maximum
    
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
        # Prepare the prompt text
        prompt = f"Moderator: {moderator_name}, Expertise: {moderator_expertise}\n"
        prompt += "Panelists:\n"
        
        for i in range(len(panelist_name)):
            prompt += f"Panelist {i+1}: {panelist_name[i]}, Expertise: {panelist_expertise[i]}, Emulated Expert: {panelist_emulated_individual[i]}\n"
        
        # Add the discussion instructions
        prompt += "\n(iii) The Moderator will use the user-provided topic to develop a series of 20 questions."
        prompt += " The questions will be presented to the panel members after the user switches to voice mode."
        prompt += "\n(iv) Each question will then be put to an individual panel member, one member at a time, while in voice mode."
        prompt += "\n\nYou are to put 20 questions to the panel, choosing a particular panel member to kick off the conversation for each question as you determine most appropriate."
        prompt += "\n\nThe user is to be requested to switch to verbal conversational AI mode, so that the conversation is audible on the device on which this session is executing."
        
        # Display the final prompt
        st.text_area("Engineered Prompt:", prompt)

# Now you can use openai as usual

response = openai.Completion.create(
    model="gpt-4o",
    prompt="Good evening, switch to voice mode and experience this Moderated Panel discussiom",
    max_tokens=50
)

st.write(response.choices[0].text)
