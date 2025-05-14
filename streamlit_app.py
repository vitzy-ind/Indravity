import streamlit as st

st.title("Indra")
st.write("menjalani hari hari biasa dengan bersekolah")
st.sidebar.title("Settings")
st.sidebar.markdown("new add")
st.sidebar.markdown("gender")
st.sidebar.radio("gender",["male","female"])
