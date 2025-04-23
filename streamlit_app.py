import streamlit as st

st.title("vitzy_ind")
st.write("halo")
st.sidebar.title("Settings")
st.sidebar.markdown("This is the sidebar content")
st.sidebar.radio("gender",["laki","cewe"])
st.number_input('Pick a number', 0, 10)
st.text_input('Email address')
st.date_input('Traveling date')
st.time_input('School time')
st.text_area('Description')
st.file_uploader('Upload a photo')
st.color_picker('Choose your favorite color')
