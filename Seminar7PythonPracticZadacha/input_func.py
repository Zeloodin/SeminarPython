import csv
def read_csvfile(name = "phonebook.csv",sep =";",delimiter=';', quotechar='|'):
    with open(name, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=delimiter, quotechar=quotechar)
        for row in spamreader:
            print(sep.join(row))

if __name__ == '__main__':
    read_csvfile()