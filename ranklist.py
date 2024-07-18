import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

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

st.write("### :orange[Contribution Edition]")
st.code("Results last updated at ")

with st.sidebar:
    with st.expander("Contacts"):
        st.write("##### :blue[Phone:]")
        st.code("044-22516020",language = None)
        st.write("##### :blue[Mail:]")
        st.code("officeitmit@gmail.com",language = None)

    with st.expander("Event Details"):
        st.write("##### :blue[Access Drive Details]")
        st.link_button("Go to gallery", "https://streamlit.io/gallery")

with st.expander(":blue[Rank List]"):

    df = pd.read_csv("Result_for_TOS.csv")
    st.write("##### [Point Based Evaluation]")
    st.dataframe(df, use_container_width=True, hide_index=True)

    st.write("###### :blue[Other Evaluations]")

    st.write("##### [Binary Evaluation]")

    st.dataframe(df, use_container_width=True, hide_index=True)

    st.write("##### [Fool-Proof Evaluation]")

    st.dataframe(df, use_container_width=True, hide_index=True)