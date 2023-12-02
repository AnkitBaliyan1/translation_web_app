import streamlit as st
from openai._client import OpenAI

API_KEY = st.secrets['OPENAI_API']
client = OpenAI(api_key=API_KEY)


def generate_message(system_input, user_input):
    message = [{
        'role':'system',
        'content':system_input},
        {'role':'user',
         'content':user_input
    }]
    return message


def generate_response(system_input, user_input, model='gpt-3.5-turbo', temperature = 0.2):

    messages = generate_message(system_input, user_input)

    response = client.chat.completions.create(model=model,
                                 messages = messages,
                                 temperature = temperature)
    
    return response.choices[0].message.content
    
def main():

    system_input = "You are a language expert who can translate any language into English.\
        Whatever the user input you will get, you just need to translate into basic English sentense without using complex words."

    user_input = st.text_input("Enter your question..")


    if st.button("Translate"):
        final_answer = generate_response(system_input=system_input,
                    user_input=user_input)

        st.write(final_answer)



