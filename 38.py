import csv


def write(filename, data):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print(f'{filename} has been created successfully.')


data1 = [
    ['Name', 'Major', 'Grade'],
    ['John', 'Computer', '16.5'],
    ['Alice', 'Math', '18'],
    ['Bob', 'Electronic', '14.35'],
    ['Yaylor', 'Computer', '19.5'],
]

write("students.csv",data1)
