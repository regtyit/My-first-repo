# titles = ('User_ID', 'Name', 'Sername', 'Age', 'City')
# data = [(1, 'Vasilisa', 'Kovaleva', 27, 'Tbilisi')]

# with open('NewDataBase.csv', 'w') as file: # mode= 'write'

#     file.write(','.join(titles)+'\n')

#     for line in data:
#         line=[str(i) for i in line]
#         file.write(','.join(line)+'\n')

with open('NewDataBase.csv', 'r') as file:

    titles = tuple(file.readline().split(','))
    data = []

    for line in file:
        if line != '\n':
            line = line.split(',')
            data.append((int(line[0]), line[1], line[2], int(line[3]), line[4]))

# new_line = tuple(input('введите данные: ').split())
# if new_line not in data:
#     data.append(new_line)

print(titles, data)

fixed_data = int(input('Введите строку для исправления: ')) - 1

data[fixed_data] = tuple(input('Введите данные: ').split(','))

with open('NewDataBase.csv', 'w') as file: # mode= 'write'

    file.write(','.join(titles)+'\n')

    for line in data:
        line=[str(i) for i in line]
        file.write(','.join(line)+'\n')

print(titles, data)