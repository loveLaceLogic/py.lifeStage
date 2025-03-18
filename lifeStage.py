age = int(input("Enter your age:  "))

if 0 <= age <= 12:
    lifeStage = "Child"
elif 13 <= age <= 19:
    lifeStage = "Teenager"
elif 20 <= age <= 64:
    lifeStage = "Adult"
else:
    lifeStage = "Senior"
    
print(f"Your life stage based on your age is a/an: {lifeStage}")