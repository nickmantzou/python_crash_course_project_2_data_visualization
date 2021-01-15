
import matplotlib.pyplot as plt

# generate x and y values
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.plasma, s=10)  # colormaps!

# set chart title and label axis
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# set size of tick labels
ax.tick_params(axis='both', which='major',labelsize=14)

# set the limits for each axis
ax.axis([0, 1100, 0, 1100000])

plt.show()