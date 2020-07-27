import csv

csvname="/Users/SUHAS/PycharmProjects/untitled/data/emp.csv"

with open(csvname) as File:
    reader = csv.reader(File)


    for row in reader:
        print(row)