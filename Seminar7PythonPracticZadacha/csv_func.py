import csv

def save_csvfile(csv_data_array,name = "phonebook.csv",delimiter=';', quotechar='|', newline=''):
    with open(name, mode='w', newline=newline) as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=delimiter, quotechar=quotechar, quoting=csv.QUOTE_MINIMAL)
        for row in csv_data_array:
            employee_writer.writerow(row)

def read_csvfile(name = "phonebook.csv",sep =";",delimiter=';', quotechar='|',newline=""):
    with open(name, newline=newline) as csvfile:
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
   save_csvfile(csv_file)