import pandas as pd

# Baca file Excel
df_excel = pd.read_excel('disperkim-od_16985_jumlah_produksi_sampah_berdasarkan_kabupatenkota_v3_data.xlsx', sheet_name='data')

# 1. buatlah sebuah DataFrame dari data jumlah produksi sampah berdasarkan Kabupaten/Kota di Jawa Barat. 
dataframe = df_excel[['nama_kabupaten_kota', 'jumlah_produksi_sampah', 'tahun']].copy()
dataframe.rename(columns={
    'nama_kabupaten_kota': 'Kabupaten/Kota',
    'jumlah_produksi_sampah': 'Jumlah Produksi Sampah (ton)',
    'tahun': 'Tahun'
}, inplace=True)

print("==========================================================================================")
print("DataFrame Awal:")
print(dataframe)
print("==========================================================================================\n")


# Input dari pengguna untuk tahun tertentu
tahun = int(input("Masukkan tahun untuk menghitung total produksi sampah: "))

# Hitung total produksi sampah untuk tahun tertentu
total_sampah = 0
for _, row in dataframe.iterrows():
    if row['Tahun'] == tahun:
        total_sampah += row['Jumlah Produksi Sampah (ton)']

# Tampilkan hasil
print("==========================================================================================")
print(f"Total produksi sampah di seluruh Kabupaten/Kota di Jawa Barat untuk tahun {tahun}: {total_sampah:.2f} ton")
print("==========================================================================================")

# 3. Jumlahkan data per tahun 
jumlah_per_tahun = {}
for i, row in dataframe.iterrows():
    tahun = row['Tahun']
    sampah = row['Jumlah Produksi Sampah (ton)']
    if tahun in jumlah_per_tahun:
        jumlah_per_tahun[tahun] += sampah
    else:
        jumlah_per_tahun[tahun] = sampah

jumlah_per_tahun_df = pd.DataFrame(list(jumlah_per_tahun.items()), columns=['Tahun', 'Total Produksi Sampah (ton)'])
print("==========================================================================================")
print("\nJumlah produksi sampah per tahun:")
print(jumlah_per_tahun_df)
print("==========================================================================================\n")

# 4. Jumlahkan data per Kota/Kabupaten per tahun 
jumlah_per_kota_tahun = {}
for i, row in dataframe.iterrows():
    kota = row['Kabupaten/Kota']
    tahun = row['Tahun']
    sampah = row['Jumlah Produksi Sampah (ton)']
    key = (kota, tahun)
    if key in jumlah_per_kota_tahun:
        jumlah_per_kota_tahun[key] += sampah
    else:
        jumlah_per_kota_tahun[key] = sampah

jumlah_per_kota_tahun_df = pd.DataFrame(
    [(k[0], k[1], v) for k, v in jumlah_per_kota_tahun.items()],
    columns=['Kabupaten/Kota', 'Tahun', 'Total Produksi Sampah (ton)']
)
print("==========================================================================================")
print("\nJumlah produksi sampah per Kota/Kabupaten per tahun:")
print(jumlah_per_kota_tahun_df)
print("==========================================================================================\n")


# 5. Ekspor hasil ke CSV dan Excel
#jumlah_per_tahun_df.to_csv('jumlah_per_tahun.csv', index=False)
#jumlah_per_kota_tahun_df.to_csv('jumlah_per_kota_tahun.csv', index=False)
#jumlah_per_tahun_df.to_excel('jumlah_per_tahun.xlsx', index=False)
#jumlah_per_kota_tahun_df.to_excel('jumlah_per_kota_tahun.xlsx', index=False)

print("\nFile CSV dan Excel telah diekspor.")
print("==========================================================================================\n")