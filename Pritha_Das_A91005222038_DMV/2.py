import matplotlib.pyplot as mpl
#data provided
data = [12, 15, 18, 20, 40, 36, 10, 22, 24, 25, 28, 30, 32, 35, 45, 33]

#plotting the histogram
mpl.hist(data, bins = 5, edgecolor = 'black')

#adding the title and labels
mpl.title("HISTOGRAM (with already given inputs)")
mpl.xlabel("VALUES (x-axis)")
mpl.ylabel("FREQUENCY (y-axis)")

#displaying the histogram
mpl.show()