import time
from multiprocessing import Pool
def proses_data_simulasi(id_data):
    print(f"Memulai pemrosesan data blok ke-{id_data}...")
    time.sleep(2)
    hasil = id_data * 100
    return f"Blok {id_data} selesai. Hasil: {hasil}"

if __name__ == '__main__':
    print("=== Memulai Alur Kerja Simulasi HPC Paralel ===")
    daftar_blok = [1, 2, 3, 4, 5]
    with Pool(processes=3) as pool:
        hasil_proses = pool.map(proses_data_simulasi, daftar_blok)
        
    print("\n--- Hasil Akhir Pemrosesan ---")
    for res in hasil_proses:
        print(res)
    print("Semua tugas komputasi paralel selesai.")