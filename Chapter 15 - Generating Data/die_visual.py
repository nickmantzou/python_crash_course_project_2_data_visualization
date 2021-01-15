
from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# create a D6
die = Die()

# make some rolls and store them in a list
results = []
for roll_num in range(10000):
    result = die.roll()
    results.append(result)

# Analyze the results
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# visualize the results
x_values = list(range(1, die.num_sides+1))   # need to turn range into a list for plotly to accept
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of the Result'}
my_layout = Layout(title='Results of rolling one D6 10,000 times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout})

