
import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [2, 4, 9, 16, 25]

# select the desired style
plt.style.use('seaborn')

# the first line is standard convention when generating plots
# fig represents the entire window of figures or subplots
# ax represents each plot in the figure
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# set size of tick labels
ax.tick_params(axis='both', labelsize=14)

plt.show()