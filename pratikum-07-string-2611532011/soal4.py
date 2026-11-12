# Name: Hilda Amelia Wati
# NIM: 2611532011
# Question 4

phone = "082611532011"
masked = phone[:4] + "*" * (len(phone) - 7) + phone[-3 :]
print(masked)