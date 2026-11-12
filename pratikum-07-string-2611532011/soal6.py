# Name: Hilda Amelia Wati
# NIM: 2611532011
# Question 6

#Pemanasan
first_name = " muhammad"
last_name = "rafi "

full_name = first_name.strip() + " " + last_name.strip()

print(full_name)
print(full_name.title())

#masalah
full_name = "  Siti Aisyah  "
nim = "2610511023"

clean = full_name.strip()
space = clean.find(" ")

if space == -1:
    first_name = clean
else:
    first_name = clean[:space]

username = first_name.lower() + nim[-3:]

print(username)