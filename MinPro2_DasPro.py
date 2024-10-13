from prettytable import PrettyTable # import prettytable untuk nampilin table

antrian_pasien = {} # buat dictionary untuk nyimpan data antrian pasien
# fungsi buat nambah pasien ke antrian dan masukkan data pasien baru ke dalam dictionary
def tambah_pasien(nomor, nama, keluhan):
    antrian_pasien[nomor] = {'Nama': nama, 'Keluhan': keluhan}
    print(f"Pasien {nama} dengan nomor antri {nomor} berhasil ditambahkan.")
# fungsi untuk lihat daftar antrian pasien
def lihat_antrian():
    # ngecek apakah ada pasien dalam antrian
    if antrian_pasien:
        # membuat tabel dengan PrettyTable
        table = PrettyTable()
        table.field_names = ["Nomor Antri", "Nama Pasien", "Keluhan"]
        # nambah data dari dictionary ke dalam tabel
        for nomor, info in antrian_pasien.items():
            table.add_row([nomor, info['Nama'], info['Keluhan']]) # menggunakan prettytable di antrian tabel
        # nampilin tabel
        print(table)
    else:
        print("Pasien tidak ada dalam antrian.") 
# fungsi untuk update data pasien
def update_pasien(nomor, nama_baru=None, keluhan_baru=None):
    # ngecek apakah pasien dengan nomor input ada dalam antrian
    if nomor in antrian_pasien:
        # Jika ada nama baru, ya update nama
        if nama_baru:
            antrian_pasien[nomor]['Nama'] = nama_baru
        # Jika ada keluhan baru, ya update keluhan la
        if keluhan_baru:
            antrian_pasien[nomor]['Keluhan'] = keluhan_baru
        print(f"Data pasien nomor antri {nomor} berhasil diperbarui.")
    else:
        print(f"Pasien dengan nomor antri {nomor} tidak ditemukan.") # jika menggunakan update dan tidak ada nomor yang dicari
# fungsi untuk menghapus pasien dari antrian
def hapus_pasien(nomor):
    # ngecek apakah pasien dengan nomor tersebut ada dalam antrian
    if nomor in antrian_pasien:
        # menghapus pasien dari dictionary
        del antrian_pasien[nomor]
        print(f"Pasien dengan nomor antri {nomor} berhasil dihapus.")
    else:
        print(f"Pasien dengan nomor antri {nomor} tidak ditemukan.") # di cek dulu coba di antrian ada datanya atau ndak

# fungsi untuk nampilin menu utama dengan PrettyTable
def menu(job):
    while True:
        menu_table = PrettyTable()
        menu_table.field_names = ["Sistem Antrian Rumah Sakit"]
        menu_table.add_row([f"Anda login sebagai {job.upper()}"])
        print(menu_table)
        # buat tabel untuk menu
        menu_table = PrettyTable()
        menu_table.field_names = ["No", "Menu"]
        # nambahin menu-menu ke tabel berdasarkan job yang dipilih
        menu_table.add_row([1, "Tambah Pasien"])
        menu_table.add_row([2, "Lihat Antrian"])
        
        if job == "admin":  # cuma admin yang bisa melakukan update dan hapus data
            menu_table.add_row([3, "Update Data Antrian Pasien"])
            menu_table.add_row([4, "Hapus Data Antrian Pasien"])
        menu_table.add_row([5, "Keluar"])
        # nampilin tabel menu yang pretty
        print(menu_table)

        pilihan = input("Pilih menu: ") # untuk input yang ada di menu

        # nambahin pasien baru
        if pilihan == '1':
            nomor = input("Masukkan nomor antrian: ")
            nama = input("Masukkan nama pasien: ")
            keluhan = input("Masukkan keluhan/penyakit pasien: ")
            tambah_pasien(nomor, nama, keluhan)
        # lihat-lihat daftar antrian pasien
        elif pilihan == '2':
            lihat_antrian()
        # update data pasien (hanya admin yang boleh/berbicara)
        elif pilihan == '3' and job == "admin":
            nomor = input("Masukkan nomor antri pasien yang ingin diupdate: ")
            nama_baru = input("Masukkan nama baru (kosongkan jika tidak ada yang ingin mengubah): ")
            keluhan_baru = input("Masukkan keluhan/penyakit baru (kosongkan jika tidak ada yang ingin mengubah): ")
            update_pasien(nomor, nama_baru or None, keluhan_baru or None)
        # menghapus pasien dari antrian (hanya admin saja)
        elif pilihan == '4' and job == "admin":
            nomor = input("Masukkan nomor antri pasien yang ingin dihapus: ")
            hapus_pasien(nomor)
        # keluar dari program
        elif pilihan == '5':
            print("Terima kasih! Program dihentikan.")
            break
        # pilihan tidak valid atau tidak ada
        else:
            print("Pilihan tidak ada, silakan coba lagi.")

# fungsi untuk milih job saat program dimulai
def pilih_job_login():
    while True:
        # bikin profil buat program saya
        table = PrettyTable()
        table.field_names = ["Nama", "NIM", "Program"]
        table.add_row(["Mochammad Rezky Ramadhan", "2409116029", "Sistem Antrian Rumah Sakit"])
        print(table)
        # milih job
        table = PrettyTable()
        table.field_names = ["No", "Pilihlah Job anda:"]
        table.add_row(["1", "Pasien"])
        table.add_row(["2", "Admin"])
        print(table)
        job = input("Masukkan pilihan (1 atau 2): ")
        # proses input job 
        if job == '1':
            return "pasien"
        elif job == '2':
            return "admin"
        else:
            print("Pilihan tidak ada untuk job tersebut, coba lagi.")

# jalanin program
job_terpilih = pilih_job_login()  # milih job di awal
menu(job_terpilih)  # jalanin menu sesuai job
