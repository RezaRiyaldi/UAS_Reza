from view.input_nilai import *
from view.view_nilai import *
data = {}

def tambah_data():
    print("==== Tambah Data ====")
    global data
    nama = input_nama()
    nim = input_nim()
    nilaiTugas = input_nilaiTugas()
    nilaiUts = input_nilaiUas()
    nilaiUas = input_nilaiUas()
    nilaiAkhir = (0.30 * nilaiTugas) + (0.35 * nilaiUts) + (0.35 * nilaiUas)
    data[nama] = nim, nilaiTugas, nilaiUts, nilaiUas, nilaiAkhir
    print(f"Berhasil menambahkan data '{nama}' dengan NIM : {nim}!")
    return data

def ubah_data():
    print("==== Ubah Data ====")
    if len(data) <= 0:  
        tidakAdaData()
    else: 
        nama = input("Masukkan Nama: ")
        if nama in data.keys():
            nim           = input_nim()
            nilaiTugas    = input_nilaiTugas()
            nilaiUts      = input_nilaiUts()
            nilaiUas      = input_nilaiUas()
            nilaiAkhir    = (0.30 * nilaiTugas) + (0.35 * nilaiUts) + (0.35 * nilaiUas)
            data[nama]  = nim, nilaiTugas, nilaiUts, nilaiUas, nilaiAkhir
            print("\nData Berhasil Di Update!")
        else:
            print("Data tidak ditemukan !!!")

def hapus_data():
    print("==== Hapus Data ====")
    if len(data) <= 0:  
        tidakAdaData()
    else: 
        nama = input("Masukkan Nama:  ")
        if nama in data.keys():
            del data[nama]
            print("Data",nama,"Telah dihapus!")
        else:
            print("Data Mahasiswa Tidak Ada Coba Harap Periksa Kembali".format(nama))