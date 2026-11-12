# Name: Hilda Amelia Wati
# NIM: 2611532011
# Question 7

name = "hilda amelia wati"
nim = "2611532011"

username = name[:name.find(" ")].lower() + nim[-3:]

print("=" * 30)
print(f"{'STUDENT CARD':^30}")
print("=" * 30)
print(f"{'Name':<10}: {name.title()}")
print(f"{'NIM':<10}: {nim}")
print(f"{'Username':<10}: {username}")
print(f"{'Intake':<10}: 20{nim[:2]}")
print("=" * 30)