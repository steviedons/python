from die import Die
import pygal

# Creat a 6 sided die
die_1 = Die(12)
die_2 = Die(10)

# Make some rolls and store the results in a list
#results = []

#for roll_number in range(100):
#    result = die.roll()
#    results.append(result)

results = [die_1.roll() + die_2.roll() for n in range(100000)]
max_results = die_1.num_sides + die_2.num_sides
frequencies = [results.count(n) for n in range(2, max_results+1)]

#print(results)
print(frequencies)

# Visualize the results

hist = pygal.Bar()


hist.title = "Results of rolling two different size die 10000 times"
hist.x_labels = [str(x) for x in range(2, die_1.num_sides + die_2.num_sides + 1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D' + str(die_1.num_sides) + ' + ' + 'D' + str(die_2.num_sides), frequencies)
hist.render_to_file('die_visual.svg')