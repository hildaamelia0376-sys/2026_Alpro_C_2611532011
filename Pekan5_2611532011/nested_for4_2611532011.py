tinggi_2011 = int(input("Masukkan tinggi pola (bilangan genap, misal 10): "))

if tinggi_2011 % 2 !=0:
    print("Tinggi harus bilangan genap!")
else:
    a_2011 = tinggi_2011
    c_2011 = a_2011
    lebar_2011 = (2 * tinggi_2011) - 2

    for i_2011 in range(1, tinggi_2011 + 1):
        b_2011 = c_2011 + 1

        for j_2011 in range(1, lebar_2011 + 1):

            #Baris atas dan bawah
            if i_2011 == 1 or i_2011 == tinggi_2011:
                if j_2011 == 1 or j_2011 == lebar_2011:
                    print("#", end="")
                else:
                    print("=", end="")

            #Baris isi
            else:
                if j_2011 == 1 or  j_2011 == lebar_2011:
                    print("|", end="")
                else:
                    if j_2011 == c_2011:
                        print("<", end="")
                    elif j_2011 == b_2011:
                        print(">", end="")
                    elif j_2011 == (lebar_2011 - c_2011):
                        print("<", end="")
                    elif j_2011 == (lebar_2011 - c_2011 + 1):
                        print(">", end="")
                    elif j_2011 > b_2011 and j_2011< (lebar_2011 - c_2011):
                        print(".", end="")
                    else:
                        print(" ", end="")
        print()

        # Logika asli Java
        a_2011 -= 2

        if a_2011 <= 0:
            c_2011 = (-a_2011) +2
        else:
            c_2011 = a_2011