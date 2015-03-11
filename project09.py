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

# The following is a pretty compact loop that took me 5 lines previously
# My understanding is that sd[i] selects the i'th element in each lists
# inside the list shortdata due to the "for... in"
machinesnbf = [float(sd[0]) for sd in shortdata]
# Note that sd stands for shortdata
# machinesnbf stands for machines number final

# yet another compact loops to follow
coresnbf = [float(sd[1]) for sd in shortdata]
# coresnbf stands for number of cores final, as in final version to be treated

avrgMnpsf = [float(sd[2]) for sd in shortdata]
# Stands for average million node per seconds final

totalmnpsf = [float(sd[3]) for sd in shortdata]
# Stands for total million nodes per second final

gamespminf = [float(sd[4]) for sd in shortdata]
# Stands for games per minute final

# Now the calculations on the correct lists: #Using the statistics module here

print('Average machines number:', stats.mean(machinesnbf),
      'and the std dev is', stats.stdev(machinesnbf))
print('Average cores number:', stats.mean(coresnbf),
      'and the std dev is', stats.stdev(coresnbf))
print('Average Mnps per machine:', stats.mean(avrgMnpsf),
      'and the std dev is', stats.stdev(avrgMnpsf))
print('Average total Mnps:', stats.mean(totalmnpsf),
      'and the std dev is', stats.stdev(totalmnpsf))
print('Average games per minute:', stats.mean(gamespminf),
      'and the std dev is', stats.stdev(gamespminf))

# Plotting part:
plt.plot(machinesnbf, 'r', totalmnpsf, 'k', linewidth=3)
#  avrgMnpsf, 'b', totalmnpsf, 'y', gamespminf, 'g')
plt.ylabel('n° of machines')
plt.xlabel('days')
plt.show()
