# === PROGRAM JAM PASIR KRISTAL PALINDROMIK (PEKAN 5) ===

n_2011 = int(input("Masukkan ukuran skala jam pasir (N): "))

print("=== PROGRAM JAM PASIR KRISTAL PALINDROMIK (PEKAN 5) ===")

# Bingkai atas
print("#", end="")
for i_2011 in range(4 * n_2011 + 5):
    print("=", end="")
print("#")

# Fase 1: Jam pasir bagian atas
for baris_2011 in range(n_2011, 0, -1):

    print("|", end="")

    # Spasi padding kiri
    print(" ", end="")

    # Spasi penyeimbang kiri
    for spasi_2011 in range(2 * (n_2011 - baris_2011)):
        print(" ", end="")

    # Angka menurun
    for angka_2011 in range(baris_2011, 0, -1):
        print(angka_2011, end=" ")

    # Poros kristal
    print("<*>", end="")

    # Angka menaik
    for angka_2011 in range(1, baris_2011 + 1):
        print(" ", end="")
        print(angka_2011, end="")

    # Spasi penyeimbang kanan
    for spasi_2011 in range(2 * (n_2011 - baris_2011)):
        print(" ", end="")

    print(" |")

# Fase 2: Titik pusat
print("|", end="")

for spasi_2011 in range(2 * n_2011 + 1):
    print(" ", end="")

print("<*>", end="")

for spasi_2011 in range(2 * n_2011 + 1):
    print(" ", end="")

print("|")

# Fase 3: Jam pasir bagian bawah
for baris_2011 in range(1, n_2011 + 1):

    print("|", end="")

    # Spasi padding kiri
    print(" ", end="")

    # Spasi penyeimbang kiri
    for spasi_2011 in range(2 * (n_2011 - baris_2011)):
        print(" ", end="")

    # Angka menurun
    for angka_2011 in range(baris_2011, 0, -1):
        print(angka_2011, end=" ")

    # Poros kristal
    print("<*>", end="")

    # Angka menaik
    for angka_2011 in range(1, baris_2011 + 1):
        print(" ", end="")
        print(angka_2011, end="")

    # Spasi penyeimbang kanan
    for spasi_2011 in range(2 * (n_2011 - baris_2011)):
        print(" ", end="")

    print(" |")

# Bingkai bawah
print("#", end="")
for i_2011 in range(4 * n_2011 + 5):
    print("=", end="")
print("#")