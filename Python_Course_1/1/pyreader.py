import csv

output = []

with open('combinatory_output.csv', 'r') as fileReader:

    reader = csv.reader(fileReader, delimiter=',')

    for value in reader:
        print("".join(value))