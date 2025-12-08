# jam_kerja_seminggu = 40
# def gaji_jam():
#     print('Masukkan Posisi Anda')
#     print('1.   Staf/Pegawai Biasa')
#     print('2.   Pengawas/Supervisor')
#     print('3.   Manajer/Kepala Divisi')
#     nilai = int(input("Pilihan"))
#     if nilai == 1:
#         return 50000
#     elif nilai == 2:
#         return 65000
#     elif nilai == 3:
#         return 80000
#     else:
#         print("Masukkan Angka Yang Benar")
#         return None
# gaji_jam = gaji_jam()

# def tunjangan ():
#     print('Masukkan Status Kepegawaian Anda')
#     print('1.   Kontrak')
#     print('2.   Tetap')
#     nilai = int(input("Pilihan"))
#     if nilai == 1: #Kontrak
#         return 0.05
#     elif nilai == 2: #Tetap
#         return 0.1
#     else:
#         print("Masukkan Angka Yang Benar")
#         return None

# tunjangan = tunjangan()

# print('Masukkan Jam Kerja dalam Seminggu:')
# jam_kerja = int(input("Jam Kerja :  "))
# def lembur():
#     if jam_kerja > jam_kerja_seminggu:
#         return 0.015
#         if tunjangan == 0.05 and jam_kerja < 50:
#             return 0.03
#         elif tunjangan == 0.01 and jam_kerja < 45:
#             return 0.05
#     else:
#         return 0
    
# bonus_lembur = lembur()
# asuransi = 35000

# def pajak():
#     if gaji_jam == 65000 and tunjangan == 0.1:
#         return 0.05
#     elif gaji_jam == 80000 and tunjangan == 0.1:
#         return 0.07
#     else:
#         return 0 
    
# nilai_pajak = pajak() 

# gaji_bersih_minggu = gaji_jam * jam_kerja
# calc_tunjangan_dan_lembur = (tunjangan * gaji_bersih_minggu) + (bonus_lembur * gaji_bersih_minggu)
# calc_pajak = asuransi + (nilai_pajak * gaji_bersih_minggu) 
# Gaji_akhir = gaji_bersih_minggu + calc_tunjangan_dan_lembur - calc_pajak
# Gaji_Bulan = Gaji_akhir*4
# print(f"gaji bersih anda dalam seminggi adalah : {Gaji_akhir}")
# print(f"Gaji Bersih anda dalam sebulan adalah : {Gaji_Bulan}")





# import sys

# # --- 1. Fungsi Bantuan untuk Menentukan Upah Dasar ---
# def get_base_rate(level):
#     """Menggunakan dictionary untuk memetakan level ke upah per jam."""
    
#     # Dictionary yang lebih rapi daripada if/elif/else
#     rate_map = {
#         1: 50000,
#         2: 65000,
#         3: 80000
#     }
#     return rate_map.get(level)

# --- 2. Fungsi Utama untuk Menghitung Gaji Bersih ---
def calculate_net_salary(level, status, hours_worked):
    
    # Dapatkan Upah Dasar
    base_rate = get_base_rate(level)
    if base_rate is None:
        print("Level posisi tidak valid.")
        return 0
        
    # --- Konstanta ---
    JAM_NORMAL = 40
    ASURANSI = 35000
    
    # --- 1. Hitung Gaji Pokok (untuk 40 jam) ---
    gaji_pokok_minggu = base_rate * JAM_NORMAL
    
    # --- 2. Hitung Upah Lembur ---
    gaji_lembur_minggu = 0
    jam_lembur = max(0, hours_worked - JAM_NORMAL)
    
    if jam_lembur > 0:
        upah_lembur_per_jam = base_rate * 1.5
        gaji_lembur_minggu = jam_lembur * upah_lembur_per_jam
        
    # --- 3. Tentukan Bonus Standar dan Bonus Kinerja ---
    bonus_percentage = 0.0 # Inisialisasi bonus
    
    if status == 'Kontrak':
        bonus_percentage = 0.05  # Bonus Standar 5%
        if hours_worked > 50:
            bonus_percentage += 0.03  # Tambahan 3% (Total 8%)
            
    elif status == 'Tetap':
        bonus_percentage = 0.10  # Bonus Standar 10%
        if hours_worked > 45:
            bonus_percentage += 0.05  # Tambahan 5% (Total 15%)
            
    gaji_bonus = gaji_pokok_minggu * bonus_percentage
    
    # --- 4. Total Gaji Kotor ---
    gaji_kotor = gaji_pokok_minggu + gaji_lembur_minggu + gaji_bonus

    # --- 5. Hitung Pemotongan (Deductions) ---
    total_potongan = ASURANSI
    pajak_percentage = 0.0 # Inisialisasi Pajak
    
    # Logika Pajak Progresif (hanya untuk Tetap Level 2 & 3)
    if status == 'Tetap':
        if level == 3:
            pajak_percentage = 0.07 # 7% dari Gaji Pokok
        elif level == 2:
            pajak_percentage = 0.05 # 5% dari Gaji Pokok
            
    potongan_pajak = gaji_pokok_minggu * pajak_percentage
    total_potongan += potongan_pajak
    
    # --- 6. Gaji Bersih Akhir ---
    gaji_bersih_minggu = gaji_kotor - total_potongan
    
    # Kembalikan semua hasil penting untuk dicetak
    return {
        'gaji_bersih_minggu': gaji_bersih_minggu,
        'gaji_pokok': gaji_pokok_minggu,
        'gaji_lembur': gaji_lembur_minggu,
        'gaji_bonus': gaji_bonus,
        'potongan_pajak': potongan_pajak,
        'total_potongan': total_potongan
    }

# --- 3. Input Pengguna dan Proses Output ---
def main():
    print("===== Sistem Penggajian PT. Maju Jaya =====")
    
    # Input Level
    print('Masukkan Posisi Anda:')
    print('1. Staf/Pegawai Biasa (Level 1)')
    print('2. Pengawas/Supervisor (Level 2)')
    print('3. Manajer/Kepala Divisi (Level 3)')
    try:
        level = int(input("Pilihan Level (1/2/3): "))
        if level not in [1, 2, 3]:
            print("Pilihan Level tidak valid.")
            return
    except ValueError:
        print("Input Level harus berupa angka.")
        return

    # Input Status
    print('\nMasukkan Status Kepegawaian Anda:')
    print('1. Kontrak')
    print('2. Tetap')
    status_choice = input("Pilihan Status (1/2): ")
    if status_choice == '1':
        status = 'Kontrak'
    elif status_choice == '2':
        status = 'Tetap'
    else:
        print("Pilihan Status tidak valid.")
        return

    # Input Jam Kerja
    try:
        hours_worked = int(input("\nMasukkan Jam Kerja dalam Seminggu: "))
    except ValueError:
        print("Input Jam Kerja harus berupa angka.")
        return

    # Panggil fungsi perhitungan utama
    results = calculate_net_salary(level, status, hours_worked)
    
    if results:
        gaji_bersih_minggu = results['gaji_bersih_minggu']
        gaji_bulan = gaji_bersih_minggu * 4 # Perkiraan 4 minggu per bulan
        
        print("\n================ RINCIAN GAJI MINGGUAN ================")
        print(f"Status Karyawan: {status} (Level {level})")
        print(f"Jam Kerja Total: {hours_worked} Jam")
        print(f"Gaji Pokok (40 jam): Rp. {results['gaji_pokok']:,.0f}")
        print(f"Tunjangan Lembur: Rp. {results['gaji_lembur']:,.0f}")
        print(f"Bonus Kinerja: Rp. {results['gaji_bonus']:,.0f}")
        print("-------------------------------------------------------")
        print(f"Gaji Kotor: Rp. {results['gaji_pokok'] + results['gaji_lembur'] + results['gaji_bonus']:,.0f}")
        print("-------------------------------------------------------")
        print(f"Potongan Asuransi: Rp. 35,000")
        print(f"Potongan Pajak PPh: Rp. {results['potongan_pajak']:,.0f}")
        print(f"Total Potongan: Rp. {results['total_potongan']:,.0f}")
        print("=======================================================")
        print(f"Gaji Bersih (Mingguan): Rp. {gaji_bersih_minggu:,.0f}")
        print(f"Gaji Bersih (Bulanan): Rp. {gaji_bulan:,.0f}")
        
if __name__ == "__main__":
    main()