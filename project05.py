import statistics as stats
data = []
shortdata = []
with open('data.txt', 'r') as f:
    for line in f:
        data.append(line.split())
        ''' This reads the file and assign a list
 for each line. The entries of the lists are each number
 in the file that are separated by a white space.
 print(data)  Just a check here. This works fine,
 it creates a list of lists. The lists are the rows of data.txt.

Now I want to compare the 4th entry of lists 1-2, then lists 3-4, 5-6 , etc.
 And write into a .txt file the lists whose 4th entry
 is the greater in each pair of lists'''
i = 0
while i <= len(data)-1:  # This makes sure that I don't get
                        # out of bounds of file, etc. Pretty awesome.
    if float(data[i][3]) >= float(data[i+1][3]):
        shortdata.append(data[i])
        i += 2                                # To ensure not to compare
    # row 2 with row 3, row 4 with row 5, etc.
    else:
        shortdata.append(data[i+1])
        i += 2

'''Now that shortdata is the list I want,
it's time to import numpy and stuff like that to perform calculations on it.
 print(float(shortdata[0][2]))  I need to use this float() call in order to
 perform calculations on the values of the list '''

j = 0
machinesnb = []
while j <= len(shortdata)-1:
    machinesnb.append(shortdata[j][0])
    j = j+1

# now machinesnb is the correct list ready to tackle.

j = 0
coresnb = []
while j <= len(shortdata)-1:
    coresnb.append(shortdata[j][1])
    j = j+1

j = 0
avrgMnps = []
while j <= len(shortdata)-1:
    avrgMnps.append(shortdata[j][2])
    j = j+1

j = 0
totalmnps = []
while j <= len(shortdata)-1:
    totalmnps.append(shortdata[j][3])
    j = j+1

j = 0
gamespmin = []
while j <= len(shortdata)-1:
    gamespmin.append(shortdata[j][4])
    j = j+1

# Now I've got to convert these lists of strings to lists of floats

machinesnbf = list(map(float, machinesnb))
coresnbf = list(map(float, coresnb))
avrgMnpsf = list(map(float, avrgMnps))
totalmnpsf = list(map(float, totalmnps))
gamespminf = list(map(float, gamespmin))

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

