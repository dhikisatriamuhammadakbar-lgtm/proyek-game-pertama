import random
angka = random.randint(1, 100)
print("=== GAME TEBAK ANGKA ===")
tebakan = int(input("Tebak angka 1-100: "))
if tebakan == angka:
    print("Hebat! Tebakanmu benar.")
else:
    print(f"Salah! Angkanya adalah {angka}")