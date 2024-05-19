import pandas as pd
import streamlit as st

with open('assets/netflixstyle.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# st.title('Crime Statistics in Los Angeles Power BI')

st.image('assets/crimeimage.png', width=900)