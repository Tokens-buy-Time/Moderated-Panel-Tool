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
prompt = f"""
You are the moderator for a virtual expert panel discussion. 
Your role is to create 20 questions and direct them to the appropriate panelists based on their expertise.

Moderator: {moderator_name}, Expertise: {moderator_expertise}

Panelists:
"""
for i in range(len(panelist_name)):
    prompt += f"\nPanelist {i+1}: {panelist_name[i]}, Expertise: {panelist_expertise[i]}, Emulated Expert: {panelist_emulated_individual[i]}"
    if i > 7:
        break


# Add the instruction for switching to voice mode, ensuring straight quotes are used

prompt += "\n\n(iii) The Moderator will use the user-provided topic to develop a series of 20 questions."
prompt += " The questions will be presented to the panel members after the user switches to voice mode."
prompt += "\n(iv) Each question will then be put to an individual panel member, one member at a time, while in voice mode."
prompt += "\n\nYou are to put 20 questions to the panel, choosing a particular panel member to kick off the conversation for each question as you determine most appropriate."
prompt += "\n\nThe user is to be requested to switch to verbal conversational AI mode, so that the conversation is audible on the device on which this session is executing."


st.text_area("Engineered Prompt:", prompt)
[
    You are to put 20 questions to the panel, choosing a particular panel member to kick-off the conversation for each question, as you determine most appropriate.

    The user is to be requested to switch to verbal conversational AI mode, referred to as voice mode, so that the conversation is audible on the device on which this session is executing.

    They must be requested to switch to voice mode only after you have reviewed this prompt in its entirety and are ready to begin the panel moderated discusion.

    You must indicate that they can make the switch by letting them know via a message displayed on the screen.

    The panel shall conduct its discussion in the manner that is typical of modern seminars and conferences.

    Conversation shall continue with a view to :-

    (i) having the panel discuss, using Conversational AI, where the participants are as previously defined,

    (ii) discus any given topic, where the topic is to be developed - from a brief, supplied by the Device User, as the initial input and is to be used to supplement the complete engineered prompt - which defines the overall assignment - as raw training data contained within the uploaded document and committed to memory.

    (iii) the Moderator using the user provided topic, to develop the aforementioned series of 20 questions, to be presented to the panel members after the used switches to voice mode,
    (iv) each question then to be put to an individual panel member; one member at a time, while in voice mode.

    (B.1) The different voices are as follows :-

    (1) panelist_name[1]
    (2) panelist_name[2]
    (3) panelist_name[3]
    (4) panelist_name[4]
    (5) panelist_name[5]
    (6) panelist_name[6]
    (7) panelist_name[7]

    (A.1) For each of the Moderator questions and each panel member comment or response, voices are to be used for each response, as defined previously in this prompt.

    (A.2) Where the Moderator is directing a question to a specific panel member, the Moderator must - after identifying itself as the Moderator - ahead of the question being asked - plus also identify the panel member to whom the question is being directed.

    (A.3) If the Moderator is making a statement or a comment, the statement or comment is to be prefaced as being that of the Moderator.

    (A.4) Responses from panel members must include in depth detail (> 250 words) and multiple insights (> 3).

    (A.5) Where a panel member is requested to respond to a question put to them by the Moderator, the response is to be prefaced by mention of the name of the panel member who is to replying.

    (A.6) Continue to (A.1) only after reviewing the whole prompt for the first time; meaning, return to (A.1) if the full Engineered Prompt has previously been read all the way to (B.5).

    # Pre conversation actions :

    (B.2) Request upload of the document which is to serve as the basis for moderated discussion; Display a message on the screen to remind the user to so do.

    (B.3) Thoroughly review the uploaded document and commit all of its content to your memory.

    (B.4) The topic for discussion shall be the content of the uploaded document; with a view to its evaluation and assessment; the topic being based upon what you determine the document to be about.

    (B.5) Instruct the user that you have completed reading the Engineered Prompt and that they can now switch to voice mode.

    Return to (B.1)
 ]

        
        st.text_area("Engineered Prompt:", prompt)
