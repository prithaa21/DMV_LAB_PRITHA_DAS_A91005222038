import matplotlib.pyplot as mpl
#taking user input
n = int(input("Enter the number of data points: "))

x = []
y = []
#taking the value for x and y
for i in range (n):
    x_val = float(input(f"Enter the value {i+1} for x in x-axis: "))
    y_val = float(input(f"Enter the value {i+1} for y in y-axis: "))
    
    x.append(x_val)
    y.append(y_val)
#plotting the line graph/chart
mpl.plot(x, y, marker ='o')
#adding the title and labels
mpl.title("LINE CHART (with user inputs)")
mpl.xlabel("X-AXIS")
mpl.ylabel("Y-AXIS")
#displaying the line graph/chart
mpl.show()
    