import streamlit as st


def sidebar():
    with st.sidebar:
        st.markdown(
        "## How to use\n"
        "Select if you want to use your own OpenAI API Key.\n"
        "- If yes, provide your own [OpenAI API key](https://platform.openai.com/account/api-keys) below🔑\n"
        "- If not, the creator's will be used.\n"
        "Start chatting as if the bot was a therapist! Share your feelings!"
    )
        user_choice = st.radio("Do you want to use your own OpenAI API Key?", ("Yes", "No"))
    
        #Yes - Provide the input box and clear current API Key
        if user_choice == "Yes":
            st.session_state.pop("OPENAI_API_KEY", None)
            api_key_input = st.text_input(
                "OpenAI API Key",
                type="password",
                placeholder="Paste your OpenAI API key here (sk-...)",
                help="You can get your API key from https://platform.openai.com/account/api-keys.",
                value=st.session_state.get("OPENAI_API_KEY", "")
            )
            st.session_state["OPENAI_API_KEY"] = api_key_input

        else: 
            # Use own API key
            st.session_state["OPENAI_API_KEY"] = st.secrets['OPEN_API_KEY']
            
        # Disclaimer Expansion
        disclaimer = st.sidebar.expander("⚠️ Disclaimer ⚠️")  
        disclaimer.write("This project is designed for educational purposes only. It is not intended to provide any form of psychological therapy or professional advice") 

        st.markdown("---")
        st.markdown("# About")
        st.markdown(
            "This tool is a work in progress. "
            "You can contribute to the project on [GitHub](https://github.com/PedroHPLopes/eliza_chatbot) " 
            "with your feedback and suggestions💡"
        )
        st.markdown("---")