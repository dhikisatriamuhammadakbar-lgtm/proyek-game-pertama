import random
angka = random.randint(1, 10)
print("=== GAME TEBAK ANGKA ===")
tebakan = int(input("Tebak angka 1-10: "))
if tebakan == angka:
    print("Hebat! Tebakanmu benar.")
else:
    print(f"Salah! Angkanya adalah {angka}")
