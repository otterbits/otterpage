import streamlit as st
import numpy as np


st.set_page_config(layout="wide")
st.markdown("<h1 style='text-align: center; color: green;'>Otterbit world</h1>", unsafe_allow_html=True)
st.write('## coding is very :red[_awesome_] :sunglasses:')

st.divider()
st.link_button("youtube", "https://www.youtube.com/@racoonByteotterBit/")
tab1, tab2, tab3= st.tabs(["INTRO", "PROJECT", "STUDY"])

with tab1:
   st.write("### hello otter!")
   col1, col2 = st.columns(2)
   with col1:
      st.video('https://youtu.be/u52CGaPWk1M?feature=shared', format='video/mp4')

with tab2:
   st.write("### working hard with communication")
   col1, col2 = st.columns(2)
   with col1:
      st.video('https://youtu.be/trS7V4g_8QI?feature=shared', format='video/mp4')
   with col2:
      st.video('https://youtu.be/NlOsPCwWegk?feature=shared', format='video/mp4')

with tab3:
   st.write("### study knowledge")
   col1, col2 = st.columns(2)
   with col1:
      st.video('https://youtu.be/_TeeNkU1fpY?feature=shared', format='video/mp4')
