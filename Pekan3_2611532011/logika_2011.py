a1_2011 = input("Input nilai boolean-1 (True/False): ").strip().lower() == "true"
a2_2011 = input("Input nilai boolean-2 (True/False): ").strip().lower() == "true"

print("\nA1 =", a1_2011)
print("A2 =", a2_2011)

 # Konjungsi: bernilai true jika keduanya True
hasil_2011 = a1_2011 and a2_2011
print("\nKonjungsi (AND)")
print("A1 and A2=", hasil_2011)

# Disjungsi: bernilai true jika salah satu True
hasil_2011 = a1_2011 or a2_2011
print("\nDisjungsi (OR)")
print("A1 or A2=", hasil_2011)

# Negasi A1: membalik nilai A1
hasil_2011 = not a1_2011
print("\nNegasi A1 (NOT)")
print("not A1=", hasil_2011)

# Negasi A2: membalik nilai A2
hasil_2011 = not a2_2011
print("\nNegasi A2 (NOT)")
print("not A2=", hasil_2011)

#XOR: bernilai true jika keduanya berbeda
hasil_2011 = a1_2011 != a2_2011
print("\nDisjungsi Ekslusif (XOR)")
print("A1 XOR A2=", hasil_2011)