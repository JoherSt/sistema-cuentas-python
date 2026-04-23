import  csv

with open("archivos\\datos.csv ")as archivo :
    #print(csv.reader(archivo))
    reader = csv.reader(archivo)
    for row in reader:
        print(row)