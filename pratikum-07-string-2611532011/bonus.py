# Name: Hilda Amelia Wati
# NIM: 2611532011
# Bonus

text = input("Masukkan kalimat: ")

clean = text.replace(" ", "").lower()

if clean == clean[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")