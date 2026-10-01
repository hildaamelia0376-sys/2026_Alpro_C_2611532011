batas_2011 = int(input("Masukkan nilai batas: "))
for line_2011 in range(1, batas_2011 + 1):
    for j in range(1, (-1 * line_2011 + batas_2011) + 1):
        print(".", end="")
    print(line_2011)