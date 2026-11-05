height = int(input("Masukkan tinggi segitiga: "))
for i in range(height, 0, -1):
    for j in range(i):
        print("* ", end="")
    print()