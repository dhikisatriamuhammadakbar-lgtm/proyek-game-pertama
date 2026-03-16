import random

def main():
    # Menghasilkan angka acak antara 1 sampai 100
    angka_rahasia = random.randint(1, 100)
    tebakan = 0
    jumlah_percobaan = 0

    print("=== Game Tebak Angka ===")
    print("Saya sudah memilih angka antara 1 sampai 100.")
    print("Coba tebak ya!")

    # Loop hingga pemain menebak dengan benar
    while tebakan != angka_rahasia:
        try:
            tebakan = int(input("\nMasukkan tebakanmu: "))
            jumlah_percobaan += 1

            if tebakan < angka_rahasia:
                print("Terlalu RENDAH! Coba lagi.")
            elif tebakan > angka_rahasia:
                print("Terlalu TINGGI! Coba lagi.")
            else:
                print(f"SELAMAT! Kamu berhasil menebak angka {angka_rahasia}")
                print(f"dalam {jumlah_percobaan} kali percobaan.")
        except ValueError:
            print("Masukkan angka yang valid ya!")

if __name__ == "__main__":
    main()
