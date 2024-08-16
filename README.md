# Moderated Panel Tool

This tool allows a moderator to pose questions to a panel, collect their responses, and allow the audience to ask questions as well.

## How to Run

1. Clone this repository.
2. Install the dependencies using `pip install -r requirements.txt`.
3. Run the app with `streamlit run moderated-panel.py`.

## Features

- Moderator can pose a question.
- Panelists can respond.
- Audience can ask questions.

# Methodology :
This App uses OpenAI's ChatGPT mobile App to simulate an expert panel discussion that is facilitated by a moderator.

# Initialization :
A briefing document "PDF" is first loaded when requested by the App, followed by the moderator generating 20 questions, to be pit to the panel, based upon the topic suggested within the brief.

# Operation :
The discussion is AI generated and takes place in 'Voice mode' on the user's device.

# Feature :
The user may participate in the discussion after it ends, by asking individual panelists questions.

