import subprocess
import time
import re

core_temp = []
i = 0
while i < 120:
    sht = subprocess.check_output("sensors")
    time.sleep(1)
    core_temp.append(sht)
    i = i+1

last_data = []
for i in core_temp:
    last_data = re.findall("\\+(?!87|105|84|100)(\d+)", str(core_temp))

# f1 = open('./data_cores_temp.txt', 'w+')
# f1.write(str(core_temp))
core_1_temp = last_data[::2]
core_2_temp = last_data[1::2]

f1 = open('./data_core1_temp.txt', 'w+')
f1.write(str(core_1_temp))
f2 = open('./data_core2_temp.txt', 'w+')
f2.write(str(core_2_temp))
f1.close()
f2.close()
