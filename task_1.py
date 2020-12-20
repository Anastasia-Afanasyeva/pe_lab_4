import os, os.path

def get_files_count(dir):
    dirListing = os.listdir(dir)
    return len(dirListing)

count = get_files_count('C:/Users/Анастасия/ВШИТиАС/МАГИЯ/Обучение/1 курс/Программная инженерия/Работа в ФС/test')
print("Файлов в директории: " + str(count))

