import numpy as np
import matplotlib.pyplot as plt


with open('genome.txt', 'r') as file:
    content = file.read()
genome_sequence = content


t = np.linspace(0, 4 * np.pi, len(genome_sequence))
x = np.cos(t)
y = np.sin(t)
z = np.linspace(0, 5, len(genome_sequence))

coordinates = np.column_stack((x, y, z))
colors = np.random.choice(['red', 'green', 'blue', 'orange','yellow'], len(genome_sequence))

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(x, y, z, c=colors)
plt.show()