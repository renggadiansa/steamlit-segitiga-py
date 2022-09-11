import streamlit as st

st.write("""
# Aplikasi Luas Segitiga
ini adalah aplikasi untuk menghitung luas dari Segitiga"""
)

alas = st.number_input("Silahkan Masukkan Nilai Alas", 0)
tinggi = st.number_input("Silahkan Masukkan Nilai Tinggi", 0)
hitung = st.button("Silahakan Klik Untuk Mengetauhi Luasnya")

if hitung:
    luas = 0.5 * alas * tinggi
    st.success(f"Luas Segitiganya Adalah... {luas}")
    st.balloons()
