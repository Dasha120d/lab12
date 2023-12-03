import re

file = open("77.csv")
values = file.readlines()#список строк
file.close()

with open("myfile.txt", "w") as my_file:#создаем файл
    for i in values:
        if  re.match('\"\d\d-\d\d-\d\d\d\d \d\d:\d\d\t\d\d\t\d', i):
            my_file.write(i)
        else:
            i = re.sub(r"(\d\d-\d\d)(:)", r"\1", i)
            my_file.write(i)