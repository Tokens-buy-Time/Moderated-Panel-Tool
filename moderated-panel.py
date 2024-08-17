import streamlit as st
import openai

# Get the API key from Streamlit secrets (make sure you have your API key set)
openai.api_key = 'API-KEY'

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
for i in range(0, 7):  # Assuming 7 panelists plus moderator maximum
    name = st.text_input(f"Panelist {i} Name: ", value=st.session_state["panelist_name"][i])
    expertise = st.text_input(f"Panelist {i} Area of Expertise: ", value=st.session_state["panelist_expertise"][i])
    emulated_individual = st.text_input(f"Panelist {i} Emulated Expert: ", value=st.session_state["panelist_emulated_individual"][i])
    
    if st.checkbox(f"Is this panelist the Moderator?", key=f"mod_{i}"):
        moderator_name = name  # Assign this panelist as the moderator
        moderator_expertise = expertise
    else:
        panelist_name.append(name)
        panelist_expertise.append(expertise)
        panelist_emulated_individual.append(emulated_individual)
    
    st.write(" ")
    if i > 7:
        break

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

        prompt += "\n(ii) discus any given topic, where the topic is to be developed - from a brief, supplied by the Device’s User, as the initial input"
        prompt += "\n(iii) The Moderator will use the user-provided topic to develop a series of 20 questions."
        prompt += " The questions will be presented to the panel members after the user switches to voice mode."
        prompt += "\n(iv) Each question will then be put to an individual panel member, one member at a time, while in voice mode."
        prompt += "\n\nYou are to put 20 questions to the panel, choosing a particular panel member to kick off the conversation for each question as you determine most appropriate."
        prompt += "\n\nThe user is to be requested to switch to verbal conversational AI mode, so that the conversation is audible on the device on which this session is executing."
        prompt += "\n\n(A.1) For each of the Moderator questions and each panel member comment or response, GPT4o various voices are to be made use of for panelist, as defined previously in this prompt."
        prompt += "\n(A.2) Where the Moderator is directing a question to a specific panel member, the Moderator must after identifying themself as the Moderator, ahead of the question being asked, identify the panelist to whom the question is being directed."
        prompt += "\n(A.3) If the Moderator is making a statement or a comment, the statement or comment is to be prefaced as being that of the Moderator."
        prompt += "\n(A.4) Responses by panelists must include in depth detail more than 250 words and at least 3 unique insights."
        prompt += "\n(A.5) Where a panelists is requested to respond to a question put to them by the Moderator, their response is to be prefaced by mention of the name of the panelist who is replying."
        prompt += "\n(A.6) Continue to (A.1) only after reviewing the whole prompt for the first time, meaning, rewind to (A.1) if the full Engineered Prompt has previously been read all the way to (B.5)."
        prompt += "\n(B.2) Request upload of the document which is to serve as the basis for moderated discussion and display a message on the screen to remind the user to so do."
        prompt += "\n(B.3) Thoroughly review the uploaded document and commit all of its content to your memory."
        prompt += "\n(B.4) The topic for discussion shall be the content of the uploaded document with a view to its evaluation and assessment and the topic being based upon what you determine the document to be about."
        prompt += "\n(B.5) Instruct the user that you have completed reading the Engineered Prompt and that they can now switch to Voice mode."
        prompt += "\n\nReposition to (B.1) in the prompt."
        
    # Display the final prompt
        st.text_area("Engineered Prompt:", prompt)
        st.session_state['prompt'] = prompt

# Button to send prompt to OpenAI API
if st.button("Send Prompt to ChatGPT"):
    prompt = st.session_state.get('prompt', '')  # Get the prompt from session state

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # or "gpt-3.5-turbo" if you have restrictions
            messages=[{"role": "system", "content": prompt}],
            max_tokens=1024,
            temperature=0.7,
        )

        generated_text = response['choices'][0]['message']['content']

        st.subheader("Response from ChatGPT:")
        st.write(generated_text)

    except Exception as e:
        st.error(f"Error: {e}")
