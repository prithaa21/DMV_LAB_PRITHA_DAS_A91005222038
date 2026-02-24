import matplotlib.pyplot as mpl
#taking input from the user
n = int(input("Enter the total number of values: "))
data = []
#setting the data
for i in range(n):
    value = float(input(f"Enter the value of {i+1}: "))
    data.append(value)
#setting the value of bins
bins = int(input("Enter the number of bins: "))
#plotting the histogram
mpl.hist(data, bins = bins, edgecolor = 'black')
#adding the title and labels
mpl.title("HISTOGRAM (with user inputs)")
mpl.xlabel("VALUES (x-axis)")
mpl.ylabel("FREQUENCY (y-axis)")
#displaying the histogram
mpl.show()