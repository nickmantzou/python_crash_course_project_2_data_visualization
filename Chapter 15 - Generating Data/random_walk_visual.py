
import matplotlib.pyplot as plt

from random_walk import RandomWalk

# make a random walk
rw = RandomWalk(50_000)
rw.fill_walk()

# plot the points in the walk
plt.style.use('classic')
fig, ax = plt.subplots(figsize=(15, 9))
point_number = range(rw.num_points)   # numbering of the points used for colormaping
ax.scatter(rw.x_values, rw.y_values, c=point_number, cmap=plt.cm.Blues, edgecolors='none', s=1)

# emphasizing the first and last points
ax.scatter(0, 0, c='green', edgecolors='none', s=100)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

# remove the axis
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
plt.show()