import streamlit as st
import openai

# Get the API key from Streamlit secrets
# openai.api_key = st.secrets["OPENAI_API_KEY"] # Uncomment this when secrets are available

# Title of the app
st.title("Moderated Panel Tool")

# Section for Panelists
st.header("Panel Setup")

panelist_name = []
panelist_expertise = []
panelist_emulated_individual = []
moderator_name = None

if "panelist_name" not in st.session_state:
    st.session_state["panelist_name"] = [
        "Michael",
        "Clayton",
        "Steve",
        "Alex",
        "Bridger",
        "Ernestine",
        "Andy"
    ]

if "panelist_expertise" not in st.session_state:
    st.session_state["panelist_expertise"] = [
        "Business Development",
        "Innovation",
        "Lean Start Up",
        "Business Model Design",
        "Private Equity Funds",
        "Venture Capital",
        "Systems Engineering"
    ]
    
if "panelist_emulated_individual" not in st.session_state:
    st.session_state["panelist_emulated_individual"] = [
        "Michael J Skok",
        "Clayton Christensen",
        "Steve Blank",
        "Alexander Osterwalder",
        "Bridger Pennington",
        "Ernestine Fu",
        "Andy Jassy"
    ]

# Input for each panelist
for i in range(7):  # Assuming 7 panelists plus moderator maximum
    name = st.text_input(f"Panelist {i+1} Name: ", value=st.session_state["panelist_name"][i])
    expertise = st.text_input(f"Panelist {i+1} Area of Expertise: ", value=st.session_state["panelist_expertise"][i])
    emulated_individual = st.text_input(f"Panelist {i+1} Emulated Expert: ", value=st.session_state["panelist_emulated_individual"][i])
    
    if st.checkbox(f"Is this panelist the Moderator ?", key=f"mod_{i}"):
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
        
        # Store the final prompt in session state
        st.session_state["prompt"] = prompt
        st.text_area("Engineered Prompt:", prompt)

# Button to send prompt to OpenAI API
if st.button("Send Prompt to ChatGPT"):
    if "prompt" in st.session_state:
        prompt = st.session_state["prompt"]

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",  # or "gpt-3.5-turbo"
                messages=[{"role": "system", "content": prompt}],
                max_tokens=1024,
                n=1,
                temperature=0.7,
            )

            generated_text = response.choices[0].message["content"].strip()

            st.subheader("Response from ChatGPT:")
            st.write(generated_text)

        except Exception as e:
            st.error(f"Error: {e}")
