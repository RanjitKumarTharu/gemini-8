import streamlit as st
from models import generate_content

st.title('Gemini LLM application')

user_input = st.text_area(
    "Where should we start ?",
    placeholder = "Ask anything"
)

if st.button('Send Prompt'):
    if user_input.strip() =='':
        st.warning("Enter valid prompt .....")
    else:
        with st.spinner('Thinking ......'):
            answer = generate_content(user_input)
            st.success('Content Generated !!!')
            st.write(answer)