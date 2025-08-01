import time
import os
import shutil
import re

directory_path = 'D:/Datos/Orders/New/'
destination_path = 'D:/Datos/Orders/Processed/'

while True:
    files = [f for f in os.listdir(directory_path) if re.match(r'.*.txt', f)] 
    for file in files:
        filepath = directory_path + file
        ##BEGIN: USE CASE SPECIFIC##
        orderlines = []
        with open(filepath,'r') as f:
            for i, line in enumerate(f):
                for match in re.finditer(r'ES\d{9}', line):
                    print('Found on line %s: %s' % (i+1, match.group()) )
                    orderlines.append('{},{}\n'.format(match.group(),line.strip()))

        with open('D:/Datos/Orders/collected_orders.csv','a') as f:
            for line in orderlines:
                f.write(line)
        ##END: USE CASE SPECIFIC##

        destination_file = destination_path + file
        shutil.move(filepath, destination_file)

    time.sleep(10)