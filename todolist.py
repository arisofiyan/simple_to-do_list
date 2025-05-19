def tampilkan_todo(todo_list):
    if not todo_list:
        print("Daftar to-do masih kosong.")
    else:
        print("\n--- Daftar To-Do ---")
        for index, tugas in enumerate(todo_list):
            print(f"{index + 1}. {tugas}")

def tambah_todo(todo_list, tugas_baru):
    todo_list.append(tugas_baru)
    print(f"Tugas '{tugas_baru}' berhasil ditambahkan.")

def hapus_todo(todo_list, indeks_hapus):
    try:
        indeks = int(indeks_hapus) - 1
        if 0 <= indeks < len(todo_list):
            tugas_dihapus = todo_list.pop(indeks)
            print(f"Tugas '{tugas_dihapus}' berhasil dihapus.")
        else:
            print("Indeks tidak valid.")
    except ValueError:
        print("Input tidak valid. Masukkan angka indeks.")

todo_list = []

while True:
    print("\n--- Program To-Do List ---")
    print("Pilih tindakan:")
    print("1. Tambah tugas")
    print("2. Lihat daftar tugas")
    print("3. Hapus tugas")
    print("4. Keluar")

    pilihan = input("Masukkan pilihan (1-4): ")

    if pilihan == '1':
        tugas = input("Masukkan tugas baru: ")
        tambah_todo(todo_list, tugas)
    elif pilihan == '2':
        tampilkan_todo(todo_list)
    elif pilihan == '3':
        if todo_list:
            indeks = input("Masukkan nomor tugas yang ingin dihapus: ")
            hapus_todo(todo_list, indeks)
        else:
            print("Daftar to-do masih kosong.")
    elif pilihan == '4':
        print("Terima kasih telah menggunakan program ini!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")