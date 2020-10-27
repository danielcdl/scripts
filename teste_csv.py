import csv

perms_list = ['01 02 03 04 05 06 07 08 09 10','11 12 13 14 15 16 17 18 19 20']

with open("C:\\Users\\CHRONOS\\Desktop\\Arquivo2.csv", 'w', newline='') as arquivo:
    writer = csv.writer(arquivo, delimiter=' ')
    writer.writerows(perms_list)
