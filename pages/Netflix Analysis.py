import pandas as pd
import streamlit as st

with open('assets/netflixstyle.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.title('Netflix Analysis in Power BI')

st.image('assets/netfliximage.png', width=900)