print("=== PROGRAM INPUT NILAI MAHASISWA ===")

#Membuat dictionary kosong untuk menampung data
data_mahasiswa = {}

#Meminta input dari pengguna
nama = input("Masukkan Nama Mahasiswa : ")
tugas = float(input("Masukkan Nilai Tugas    : "))
uts = float(input("Masukkan Nilai UTS      : "))
uas = float(input("Masukkan Nilai UAS      : "))

#Memasukkan data ke dalam dictionary menggunakan Key
data_mahasiswa['nama'] = nama
data_mahasiswa['tugas'] = tugas
data_mahasiswa['uts'] = uts
data_mahasiswa['uas'] = uas

#Menampilkan hasil dictionary yang sudah terisi
print("--- HASIL DATA MAHASISWA ---")
print(data_mahasiswa)

#Menampilkan data dengan lebih rapi menggunakan perulangan for
print("--- RINCIAN NILAI ---")
for key, value in data_mahasiswa.items():
    print(f"{key.capitalize()} : {value}")