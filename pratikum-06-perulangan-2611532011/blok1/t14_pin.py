correct_pin_2011 = "1234"
MAX_ATTEMPTS_2011 = 3
attempt_2011 = 0
pin_2011 = input("Enter your PIN: ")
while pin_2011 != correct_pin_2011 and attempt_2011 < MAX_ATTEMPTS_2011:
    print("Incorrect PIN.")
    attempt_2011 += 1
    pin_2011 = input("Enter your PIN: ")
if pin_2011 == correct_pin_2011:
    print("Access granted.")
else:
    print("Account locked.")