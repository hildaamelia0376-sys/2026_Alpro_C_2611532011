ulang_2011 = int(input("Masukkan jumlah perulangan: "))

jumlah_2011 = 0
for i in range(1, ulang_2011 + 1):
    print(i, end="")
    jumlah_2011 = jumlah_2011 + i

    if i < ulang_2011:
        print(" + ", end="")
    else:
        print(" = ", jumlah_2011, end="")
print()
print("jumlah =", jumlah_2011)