# -*- coding: utf-8 -*-
"""
Generates JS code to import unique portals data into IITC Uniques plugin
"""

import csv
clist = ""
vlist = ""  

with open("..\dump\game_log.tsv", newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t', quotechar='|')
    next(reader) #skip header
    for row in reader:
        if (row[3] == 'captured portal'):
            try:
                lat = float(row[1]) * 1000000
                lon = float(row[2]) * 1000000    
            except ValueError:
                continue       
            clist = clist + f'[{lon:.0f},{lat:.0f}],'
        if (row[3].startswith('hacked') and row[3].endswith('portal')):
            try:
                lat = float(row[1]) * 1000000
                lon = float(row[2]) * 1000000    
            except ValueError:
                continue       
            vlist = vlist + f'[{lon:.0f},{lat:.0f}],'

with open("data.txt", "w") as f:
    f.write("clist = [" + clist[:-1] + "]\n")
    f.write("vlist = [" + vlist[:-1] + "]")