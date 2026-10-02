ulang_2011 = int(input("Masukkan jumlah perulangan: "))

jumlah_2011 = 0
for i_2011 in range(1, ulang_2011 + 1):
    print(i_2011, end="")
    jumlah_2011 = jumlah_2011 + i_2011

    if i_2011 < ulang_2011:
        print(" + ", end="")
    else:
        print(" = ", jumlah_2011, end="")
print()
print("jumlah =", jumlah_2011)