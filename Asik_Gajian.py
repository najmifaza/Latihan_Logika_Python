Nama_P = input("Masukkan Nama Panjang: ")
Jabatan_P = input("Masukkan Jabatan \n'1 untuk dewan harian, 2 untuk pegawai biasa' : ")
jenis_P = input("1 Untuk Pegawai Biasa, 2 untuk Pegawai Tetap: ")
Jam_Kerja = int(input("Masukkan Jam Kerja: "))
    
if Jabatan_P == '2':
    Gaji_Jam = 50000
elif Jabatan_P == '1':
    Gaji_Jam = 60000

Gaji_pokok = Gaji_Jam * Jam_Kerja

if jenis_P == '2':
    Bonus = 0.14 * Gaji_pokok
elif jenis_P == '1':
        Bonus = 0.07 * Gaji_pokok

Total_Gaji = Gaji_pokok + Bonus
Potongan_asuransi = 25000
Gaji_bersih = Total_Gaji - Potongan_asuransi

print("Gaji_bersih dari", Nama_P, "adalah Rp.", Gaji_bersih)


