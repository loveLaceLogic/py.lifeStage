try:
    age = int(input("Enter your age:  "))
    
    if age < 0:
        print("Age cannot be negative. Please enter a valid age.")
    elif age <= 12:
        lifeStage = "Child"
    elif age <= 19:
        lifeStage = "Teenager"
    elif age <= 64:
        lifeStage = "Adult"
    else:
        lifeStage = "Senior"

    if age >= 0:
        print(f"Your life stage based on your age is: {lifeStage}")

except ValueError:
    print("Invalid input! Please enter a valid number.")
