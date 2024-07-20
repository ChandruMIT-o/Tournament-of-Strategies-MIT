import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

import os

def display_code_files(folder_path):
    if not os.path.isdir(folder_path):
        st.error("The specified folder does not exist.")
        return
    
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                code_content = file.read()
            name = str(file_name).split(".")
            st.code(f"Strategy: {name[0]}", language = None)
            
            st.code(code_content, language='python')

css = """
<style>
[data-testid = "stAppViewContainer"]{
background-color: #000000;
opacity: 1;
background: linear-gradient(135deg, #19191955 25%, transparent 25%) -16px 0/ 32px 32px, linear-gradient(225deg, #191919 25%, transparent 25%) -16px 0/ 32px 32px, linear-gradient(315deg, #19191955 25%, transparent 25%) 0px 0/ 32px 32px, linear-gradient(45deg, #191919 25%, #000000 25%) 0px 0/ 32px 32px;
}

[data-testid = "stSidebar"]{
background-color: #000000;
opacity: 1;
background-image:  repeating-radial-gradient( circle at 0 0, transparent 0, #000000 16px ), repeating-linear-gradient( #19191955, #191919 );
}
</style>
"""

st.markdown(css, unsafe_allow_html=True)

st.image("Assets/poster2.jpg")
st.write("##### Check the ranklist here for each Editions of the game.")

st.write("### :orange[Cooperation Edition]")
st.code("""Final Results have been Published!""")

with st.sidebar:
    with st.expander("Contacts"):
        st.write("##### :blue[Phone:]")
        st.code("+91 7667634519",language = None)
        st.write("##### :blue[Mail:]")
        st.code("officeitmit@gmail.com",language = None)

    with st.expander("Event Details"):
        st.write("##### :blue[Access Drive Details]")
        st.link_button("Go to Drive", "https://drive.google.com/drive/folders/1eWMRrbatMhwQvE4Wat4LUtdt0O6Op5a0?usp=sharing")

with st.expander(":blue[Rank List]"):

    df = pd.read_csv("finalised.csv")
    st.write("##### [Point Based Evaluation]")
    st.dataframe(df, use_container_width=True, hide_index=True, height=800)

    st.write("###### :blue[Other Evaluations]")

    st.write("##### [Binary Evaluation]")

    # st.dataframe(df, use_container_width=True, hide_index=True)

    st.write("##### [Fool-Proof Evaluation]")

    # st.dataframe(df, use_container_width=True, hide_index=True)

with st.expander("All Strategies [Code]"):
    display_code_files("strategies")