# Program to handle missing values

n = int(input("Enter number of values: "))

data = []

for i in range(n):
    try:
        value = input(f"Enter value {i+1}: ")
        
        # If user presses enter (empty input), treat as missing
        if value == "":
            raise ValueError
        
        data.append(float(value))
    
    except ValueError:
        print("Invalid or missing value detected. Replacing with 0.")
        data.append(0)

print("\nFinal Data:")
print(data)