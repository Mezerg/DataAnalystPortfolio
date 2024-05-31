import streamlit as st
import pandas as pd


def inject_css_file():
    with open('assets/styles.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def main():
    st.set_page_config(page_title="J.K Portfolio", page_icon="📊", layout="wide")
    inject_css_file()

    st.title('J.K')
    st.write('## Data Analysis Portfolio')
    st.write('Welcome to my portfolio! Here you can find my projects of data analyses. ')
    st.write('I have prepared 3 projects for you to explore. Enjoy!')
    st.write( 'Shop Sales Analysis, Netflix Analysis, Crime in Los Angeles')
    st.write('Skills : Python/Power BI/HTML/CSS')

if __name__ == '__main__':
    main()
   
