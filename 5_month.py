# 15)Подсчет количества слов в файле:
#    Создайте программу, которая подсчитывает количество слов в текстовом файле и выводит это число.
# 16)Запись в файл:   Попросите пользователя ввести некоторый текст и сохраните его в текстовом файле.
# 17)Копирование файла:
#    Напишите программу, которая копирует содержимое одного файла в другой фа

def words(filename):
    with open(filename, 'r') as file:
        text = file.read()
filename = 'example.txt'  
words(filename)



########



def write_to_file(text, filename):
    with open(filename, 'w') as file:
        file.write(text)
    print('{filename}')

text = input("Введите текст: ")
filename = 'output.txt'  
write_to_file(text, filename)


##############################

#
def copy_file(iman_file, zhoroeevv_file):
        with open(iman_file, 'r') as source:
            with open(zhoroeevv_file, 'w') as destination:
                destination.write(source.read())
iman_file = 'source.txt'
zhoroeevv_file = 'copy.txt' 
copy_file(iman_file, zhoroeevv_file)


