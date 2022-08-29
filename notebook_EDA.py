import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout='wide')
st.markdown("""<div style="display:flex;justify-content:center;"><h1>CUSTOMER SEGMENTATION</h1></div>""", unsafe_allow_html=True)
st.markdown('''<p style="text-align:center">IN FRENCH ONLY AT THE MOMENT</p>''', unsafe_allow_html=True)

HtmlFile = open("notebookanalyse.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
components.html(source_code, height=1000, scrolling=True)