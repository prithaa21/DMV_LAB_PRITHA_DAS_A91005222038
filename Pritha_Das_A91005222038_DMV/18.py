#Program to draw a scatter plot(assume the dataset in such a way that the graph should contain
# outlier(s) and cluster(s) and either of positive or negetive correlation)
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(r"D:\SEM 8\DMV\LAB\Pritha_Das_A91005222038_DMV\dataset\books_dataset.csv")
x=np.random.rand(50)
y=-x+np.random.normal(0,0.1,50)
x=np.append(x, 0.2)
y=np.append(y,2)
plt.scatter(x,y, color='pink')
plt.xlabel('X VALUES')
plt.ylabel('Y VALUES')
plt.title("Negative correlation with outlier")
plt.show()