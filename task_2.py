import csv
import pickle

class lab4:
    def __init__(self):
        self.stlist = [[None for x in range(4)] for y in range(9)]

    def students(self):
        with open('C:/Users/Анастасия/ВШИТиАС/МАГИЯ/Обучение/1 курс/Программная инженерия/Работа в ФС/students.csv', encoding='UTF-8') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=';', quotechar='|')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print('header was read')
                    line_count += 1
                else:
                    for i in range(4):
                        self.stlist[line_count-1][i] = row[i]
                    print('Значения записаны в строку')
                    line_count += 1
            print(self.stlist)

    def sortbyname(self):
        self.stlist.sort(key=lambda student: student[1])
        print('sorted by name:\n', self.stlist)

    def morethan22(self):
        age22 = []
        for student in self.stlist:
            if int(student[2])>22:
                age22.append(student)
        print('age>22:\n', age22)

    def writetocsv(self, filename='testwriting'): #task 2.3
        name = filename + '.csv'
        with open (name, 'w') as f:
            thewriter = csv.writer(f, delimiter=';', lineterminator = '\n')
            thewriter.writerow(['#', 'Name', 'Age', 'Group'])
            thewriter.writerows(self.stlist)
        f.close()

    def savetopickle(self):
        with open('test.pickle', 'wb') as p:
            pickle.dump(self.stlist, p)
            print('saved in pickle file')
        p.close()

    def readfrompickle(self):
        with open('test.pickle', 'rb') as r:
            stlist = pickle.load(r)
            print('read from pickle file')
            print(stlist)
        r.close()

obj1 = lab4()
obj1.students()

#task 2.1: sort by name
obj1.sortbyname()

#task 2.2 age>22
obj1.sortbyname()

#task 2.3 write to csv
obj1.writetocsv()
print('wrote to the "testwriting.csv" file')

#task 2.4 add information aboun one more student and write to csv "students_changed.csv"
#для этого потребовалось немного изменить ф-цию записи, чтобы передавать в нее имя файла (без расширения, чтобы избежать ошибок)
obj1.stlist.append(['46', 'Пушкин Александр Сергеевич', '221', 'БО-202222'])
obj1.writetocsv('students_changed')
print('one student was added, changes were saved in the "students_changed" file')

#task 2.5
obj1.savetopickle()
obj1.readfrompickle()

    

