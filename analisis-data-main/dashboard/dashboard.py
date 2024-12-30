import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')

# Load dataset
# bike_sharing = pd.read_csv("bike_sharing.csv")
bike_sharing = pd.read_csv("https://github.com/likesagitri/Project_Dicoding_Data_Analysis/raw/refs/heads/main/analisis-data-main/dashboard/bike_sharing.csv")

with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://avatars.githubusercontent.com/u/125043070?v=4")

    # Menambahkan judul dan subjudul
    st.title('Proyek Akhir: Analisis Data Peminjaman Sepeda :sparkles:')
    st.header('Nama: Like Sagitri')
    st.subheader('Email: likeesagitrihelen@gmail.com')
    st.subheader('Id Dicoding: ')

st.header('Proyek Akhir: Analisis Data Peminjaman Sepeda :sparkles:')
st.subheader('1. Peminjaman Sepeda di hari kerja atau hari libur')
st.write('''
    Berdasarkan grafik di bawah ini dapat dilihat bahwa peminjaman sepeda lebih banyak terjadi di hari kerja daripada hari libur.
''')
workingday_data_hour = bike_sharing.groupby(by='workingday_hourly')['cnt_hourly'].sum()
workingday_labels = ['Hari Libur', 'Hari Kerja']
fig_bar_workingday_hour = plt.figure(figsize=(12, 6))
plt.bar(x=workingday_labels, height=workingday_data_hour)
plt.xlabel('Working Day')
plt.ylabel('Jumlah Peminjam Sepeda')
plt.title('Peminjaman Sepeda di hari kerja atau hari libur')
st.pyplot(fig_bar_workingday_hour)

st.subheader('2. Pengaruh musim terhadap peminjaman sepeda')
st.write('''
    Berdasarkan grafik di bawah ini dapat dilihat bahwa peminjaman sepeda paling banyak terjadi pada musim gugur (Fall).
''')
season_data = bike_sharing.groupby(by='season_daily')['cnt_daily'].mean()
season_labels = ['Spring', 'Summer', 'Fall', 'Winter']
fig_bar_season_daily = plt.figure(figsize=(12, 6))
plt.bar(x=season_labels, height=season_data)
plt.xlabel('Musim')
plt.ylabel('Jumlah Penyewaan Sepeda')
plt.title('Pengaruh Musim Terhadap Peminjaman Sepeda')
st.pyplot(fig_bar_season_daily)

st.caption('Copyright © Dicoding')
