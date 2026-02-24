import matplotlib.pyplot as mpl

#provided data
x = [1, 2, 3, 4, 5]
y = [10, 15, 20, 25, 30]

#plotting the line chart
mpl.plot(x, y, marker ='o')

#adding title and labels to the chart
mpl.title("LINE CHART (with already given inputs)")
mpl.xlabel("X-AXIS")
mpl.ylabel("Y-AXIS")

#dislaying the line chart
mpl.show()
    