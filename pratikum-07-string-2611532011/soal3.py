# Name: Hilda Amelia Wati
# NIM: 2611532011
# Question 3

text = "Informatika"
print(text[10])
print(text.upper())
print(text[0:11])

text = "Hilda Amelia Wati"
count = 0
for char in text.lower():
    if char in "aiueo":
        count += 1
print("Vowels:", count)