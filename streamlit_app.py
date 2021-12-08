#importing relevant libraries
import streamlit as st


#first page: entering the text 
st.write('# Welche Partei hats gesagt?')
message_text = st.text_input('Füge hier eine Plenarrede hier ein:')

#second page: output of classifier