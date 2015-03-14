import statistics as stats
import matplotlib.pyplot as plt
data = []
shortdata = []
with open('data.txt', 'r') as f:
    for line in f:
        data.append(line.split())

# This reads the file and assign a list
# for each line. The entries of the lists are each number
# in the file that are separated by a white space.
# it creates a list of lists. The lists are the rows of data.txt.

# Now I want to compare the 4th entry of lists 1-2, then lists 3-4, 5-6 , etc.
# And append into the list shortdata the lists whose 4th entry
# is the greater in each pair of lists'''

for y, z in zip(data[::2], data[1::2]):
    shortdata.append(max(y, z, key=lambda s: float(s[3])))
print(shortdata)

machines_number = [float(sd[0]) for sd in shortdata]
# Note that sd stands for shortdata
cores_number = [float(sd[1]) for sd in shortdata]

average_Mnps_permachine = [float(sd[2]) for sd in shortdata]

total_Mnps = [float(sd[3]) for sd in shortdata]

games_per_minute = [float(sd[4]) for sd in shortdata]

print('Average machines number:', stats.mean(machines_number),
      'and the std dev is', stats.stdev(machines_number))
print('Average cores number:', stats.mean(cores_number),
      'and the std dev is', stats.stdev(cores_number))
print('Average Mnps per machine:', stats.mean(average_Mnps_permachine),
      'and the std dev is', stats.stdev(average_Mnps_permachine))
print('Average total Mnps:', stats.mean(total_Mnps),
      'and the std dev is', stats.stdev(total_Mnps))
print('Average games per minute:', stats.mean(games_per_minute),
      'and the std dev is', stats.stdev(games_per_minute))

# Plotting part:
plt.plot(machines_number, 'r', total_Mnps, 'k', linewidth=3)
#  avrgMnpsf, 'b', totalmnpsf, 'y', gamespminf, 'g')
plt.ylabel('n° of machines')
plt.xlabel('days')
plt.show()
