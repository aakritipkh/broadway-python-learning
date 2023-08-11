score = float(input("Enter the score"))
if score > 1.0 or score < 0.0:
    print("Score not valid")
elif score >= 0.9:
    print("You got grade A")
elif score >= 0.8:
    print("You got grade B")
elif score >= 0.7:
    print("You got grade C")
elif score >= 0.6:
    print("You got grade D")
else:
    print("You got grade F")


