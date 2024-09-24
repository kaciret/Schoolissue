import csv

def import_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data

student_data = import_csv('Students.csv')
print(student_data) 