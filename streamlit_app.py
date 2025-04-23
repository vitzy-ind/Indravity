import streamlit as st

st.title("vitzy_ind")
st.write("halo")
st.sidebar.title("Settings")
st.sidebar.markdown("This is the sidebar content")
st.sidebar.radio("gender",["laki","cewe"])
st.image("kid.jpg", caption="A kid playing")
st.audio("audio.mp3")
st.video("video.mp4")
