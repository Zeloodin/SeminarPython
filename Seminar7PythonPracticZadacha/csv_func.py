import csv

def save_csvfile(csv_data_array,name = "phonebook.csv",delimiter=' ', quotechar=';'):
    with open(name, mode='w') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=delimiter, quotechar=quotechar, quoting=csv.QUOTE_MINIMAL)
        employee_writer.writerows(csv_data_array)




import csv
def read_csvfile(name = "phonebook.csv",sep =";",delimiter=';', quotechar='|'):
    with open(name, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=delimiter, quotechar=quotechar)
        for row in spamreader:
            print(sep.join(row))

def get_csvfile(name = "phonebook.csv",sep =";",delimiter=';', quotechar='|'):
    array_data = []
    with open(name, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=delimiter, quotechar=quotechar)
        for row in spamreader:
            array_data.append(row)
    return array_data


if __name__ == '__main__':
   csv_file = get_csvfile()
   print(csv_file)
   save_csvfile(csv_file)