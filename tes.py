import streamlit as st

st.title("Contoh Program Streamlit")
with st.form(key="my form"):
    nama = st.text_input("Nama Lengkap")
    jenis_kelamin = st.radio("Jenis_Kelamin", ("Laki-Laki", "Perempuan"))
    submit = st.form_submit_button(label="kirim")