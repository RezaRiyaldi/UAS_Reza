from model.daftar_nilai import *
def garis():
    print(71*"=")

def header():
    garis()
    print("| {0:^2} | {1:^7} | {2:^18} | {3:^5} | {4:^5} | {5:^5} | {6:^7} |".format("No", "NIM", "Nama", "Tugas", "UTS", "UAS", "Akhir"))
    garis()

def tidakAdaData(): 
    header()          
    print("|{0:^69}|".format("TIDAK ADA DATA!!! Silahkan Tambah Data Terlebih Dahulu"))
    garis()

def cetak_daftar_nilai():
    print("==== Lihat Data ====")
    print("\n Daftar Nilai Mahasiswa ")
    if data.items():
        header()
        no = 0
        for x in data.items():
            no += 1 
            print(f"| {no:>2} | {x[1][0]:>7} | {x[0]:<18} | {x[1][1]:>5} | {x[1][2]:>5} | {x[1][3]:>5} | {x[1][4]:>6.2f} |")
        garis()
    else:
        tidakAdaData()

def cetak_hasil_pencarian():
    print("==== Cari Data ====")
    if len(data) <= 0:
        tidakAdaData()
    
    else:
        nama = input("Masukkan Nama        : ")
        if nama in data.keys():
            print("\n Daftar Nilai Mahasiswa ")
            header()
            print("| {0:^2} | {2:>7} | {1:<18} | {3:>5} | {4:>5} | {5:>5} | {6:>7.2f}  |"
                .format("#", nama, data[nama][0], data[nama][1],data[nama][2], data[nama][3], data[nama][4]))
            garis()
        else:
            print(f"Data {nama} tidak ditemukan!")