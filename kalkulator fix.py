# Mendefinisikan fungsi 'kalkulator'
def kalkulator():
    while True:
        # Menampilkan menu pilihan operasi
        print("Pilih operasi:")
        print("1. Penjumlahan (+)")
        print("2. Pengurangan (-)")
        print("3. Perkalian (*)")
        print("4. Pembagian (/)")
        print("5. Modulus (%)")
        print("6. Logika AND (and)")
        print("7. Logika OR (or)")
        print("8. Logika NOT (not)")

        # Meminta pengguna memilih operasi
        pilihan = input("Masukkan nomor operasi (1/2/3/4/5/6/7/8): ")

        # Memeriksa pilihan operasi yang dimasukkan pengguna
        if pilihan in ('1', '2', '3', '4', '5'):
            # Jika pengguna memilih operasi matematika, minta dua angka
            angka1 = float(input("Masukkan angka pertama: "))
            angka2 = float(input("Masukkan angka kedua: "))
            if pilihan == '1':
                # Menampilkan hasil penjumlahan
                print("Hasil penjumlahan:", angka1 + angka2)
            elif pilihan == '2':
                # Menampilkan hasil pengurangan
                print("Hasil pengurangan:", angka1 - angka2)
            elif pilihan == '3':
                # Menampilkan hasil perkalian
                print("Hasil perkalian:", angka1 * angka2)
            elif pilihan == '4':
                if angka2 == 0:
                    # Menampilkan pesan kesalahan jika pembagian oleh nol
                    print("Pembagian oleh nol tidak diizinkan.")
                else:
                    # Menampilkan hasil pembagian
                    print("Hasil pembagian:", angka1 / angka2)
            elif pilihan == '5':
                # Menampilkan hasil modulus
                print("Hasil modulus:", angka1 % angka2)
        elif pilihan in ('6', '7', '8'):
            # Jika pengguna memilih operasi logika, minta dua nilai logika
            nilai1 = input("Masukkan nilai logika pertama (True/False): ").lower()
            nilai2 = input("Masukkan nilai logika kedua (True/False): ").lower()
            if pilihan == '6':
                # Melakukan operasi logika AND dan menampilkan hasilnya
                hasil = nilai1 == 'true' and nilai2 == 'true'
            elif pilihan == '7':
                # Melakukan operasi logika OR dan menampilkan hasilnya
                hasil = nilai1 == 'true' or nilai2 == 'true'
            elif pilihan == '8':
                # Melakukan operasi logika NOT dan menampilkan hasilnya
                hasil = not (nilai1 == 'true')
            print("Hasil:", hasil)
        else:
            # Menampilkan pesan jika pilihan tidak valid
            print("Pilihan tidak valid")

# Memanggil fungsi 'kalkulator' untuk menjalankan program
kalkulator()
