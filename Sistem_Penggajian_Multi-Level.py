def base_rate():
    print('Masukkan Posisi Anda')
    print('1.   Staf/Pegawai Biasa')
    print('2.   Pengawas/Supervisor')
    print('3.   Manajer/Kepala Divisi')
    nilai = int(input("Pilihan"))
    if nilai == 1:
        return 50000
    elif nilai == 2:
        return 65000
    elif nilai == 3:
        return 80000
    else:
                print("Masukkan Angka Yang Benar")
        return None

Gaji = base_rate()
