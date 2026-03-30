import streamlit as st
import math

st.title("Fun 3D Volume Calculator :rocket:")
st.write("Let's start to find the volume of Geometry.")

# --- KUMPULAN FUNCTION VOLUME ---
def volume_kubus():
    st.subheader('Mencari Volume Kubus')
    sisi = st.number_input("Masukkan panjang sisi kubus (cm): ", min_value=0.0, step=1.0)
    # st.success digunakan agar hasil tampil lebih cantik dengan kotak warna hijau
    st.success(f"Volume kubus adalah: {sisi * sisi * sisi:.2f} cm\u00b3")
    
def volume_balok():
    st.subheader('Mencari Volume Balok')
    panjang = st.number_input("Masukkan panjang balok (cm): ", min_value=0.0, step=1.0)
    lebar = st.number_input("Masukkan lebar balok (cm): ", min_value=0.0, step=1.0)
    tinggi = st.number_input("Masukkan tinggi balok (cm): ", min_value=0.0, step=1.0)
    st.success(f"Volume balok adalah: {panjang * lebar * tinggi:.2f} cm\u00b3")

def volume_tabung():
    st.subheader('Mencari Volume Tabung')
    jari_jari = st.number_input("Masukkan jari-jari alas (cm): ", min_value=0.0, step=1.0)
    tinggi = st.number_input("Masukkan tinggi tabung (cm): ", min_value=0.0, step=1.0)
    hasil = math.pi * (jari_jari**2) * tinggi
    st.success(f"Volume tabung adalah: {hasil:.2f} cm\u00b3")

def volume_bola():
    st.subheader("Mencari Volume Bola")    
    jari_jari = st.number_input("Masukkan jari-jari bola (cm): ", min_value=0.0, step=1.0)
    hasil = 4/3 * math.pi * (jari_jari**3)
    st.success(f"Volume bola adalah: {hasil:.2f} cm\u00b3")

def volume_prisma_segitiga():
    st.subheader("Mencari Volume Prisma Segitiga")
    alas_segitiga = st.number_input("Masukkan alas segitiga (cm): ", min_value=0.0, step=1.0)
    tinggi_segitiga = st.number_input("Masukkan tinggi segitiga (cm): ", min_value=0.0, step=1.0)
    tinggi_prisma = st.number_input("Masukkan tinggi prisma (cm): ", min_value=0.0, step=1.0)
    luas_alas = 0.5 * alas_segitiga * tinggi_segitiga
    hasil = luas_alas * tinggi_prisma
    st.success(f"Volume prisma segitiga adalah: {hasil:.2f} cm\u00b3")

def volume_limas():
    st.subheader("Mencari Volume Limas Segiempat")
    panjang_alas = st.number_input("Masukkan panjang alas (cm): ", min_value=0.0, step=1.0)
    lebar_alas = st.number_input("Masukkan lebar alas (cm): ", min_value=0.0, step=1.0)
    tinggi_limas = st.number_input("Masukkan tinggi limas (cm): ", min_value=0.0, step=1.0)
    luas_alas = panjang_alas * lebar_alas 
    hasil = 1/3 * luas_alas * tinggi_limas
    st.success(f"Volume limas adalah: {hasil:.2f} cm\u00b3")

def volume_kerucut():
    st.subheader("Mencari Volume Kerucut")   
    jari_jari = st.number_input("Masukkan jari-jari alas (cm): ", min_value=0.0, step=1.0)
    tinggi_kerucut = st.number_input("Masukkan tinggi kerucut (cm): ", min_value=0.0, step=1.0)
    hasil = 1/3 * math.pi * (jari_jari**2) * tinggi_kerucut
    st.success(f"Volume kerucut adalah: {hasil:.2f} cm\u00b3")

# --- BAGIAN MENU UTAMA ---
st.divider() # Membuat garis pembatas
st.write("### Pilih Bangun Ruang")

# Menggunakan selectbox sebagai ganti input angka 1-7
pilihan = st.selectbox(
    "Bangun ruang apa yang ingin kamu hitung volumenya?",
    ("Pilih...", "Kubus", "Balok", "Tabung", "Bola", "Prisma Segitiga", "Limas", "Kerucut")
)

# Mengeksekusi function berdasarkan pilihan di selectbox
if pilihan == "Kubus":
    volume_kubus()
elif pilihan == "Balok":
    volume_balok()
elif pilihan == "Tabung":
    volume_tabung()
elif pilihan == "Bola":
    volume_bola()
elif pilihan == "Prisma Segitiga":
    volume_prisma_segitiga()
elif pilihan == "Limas":
    volume_limas()
elif pilihan == "Kerucut":
    volume_kerucut()
