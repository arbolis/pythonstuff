import subprocess
import time
import re

core_temp = []
i = 0
while i < 2:
    sht = subprocess.check_output("sensors")
    time.sleep(.1)
    core_temp.append(sht)
    i = i+1

last_data = []
for i in core_temp:
    last_data = re.findall("\\+(?!87|105)(\d+)", str(core_temp))
print(last_data)
# f1 = open('./data_cores_temp.txt', 'w+')
# f1.write(str(core_temp))
