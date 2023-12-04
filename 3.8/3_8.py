import random

TrValues = []
ostatok = []
komp1 = []
komp2 = []
komp3 = []
komp4 = []
komp5 = []
komp6 = []
komp7 = []

File = open('77.csv')
AllValues = File.read().split('\n')
count = len(AllValues)

print("1) Разделить набор на тренировочную и тестовую выборку в соотношение 70:30 соответственно")

random.shuffle(AllValues ) #случайно перемешиваем элементы списка

count = len(AllValues )
count70 = round((count * 70)/100,)
print("Элементов в списке:", count)
print("Количество элементов в 70% :", count70)
print("--------------------------------------------")
print("70% элементов:\n",*AllValues[:count70], sep = "\n")
print("--------------------------------------------")
print("30% элементов:\n",*AllValues[count70:],sep = "\n")

print("--------------------------------------------")
print("2) Разделить набор на тренировочную и тестовую выборку в соотношение 80:20 соответственно")
print("Элементов в списке:", count)
random.shuffle(AllValues)
count80 = round((count * 80)/100,)
print("Количество элементов в 80% :", count80)
print("--------------------------------------------")
print("80% элементов:\n",*AllValues[:count80], sep = "\n")
print("--------------------------------------------")
print("20% элементов:\n",*AllValues[count80:],sep = "\n")

random.shuffle(AllValues)
LenghtVal = len(AllValues)
Delenie = LenghtVal * 12/100
for i in AllValues:
    if Delenie > 0:
        TrValues.append(i)
        Delenie -= 1
    else:
        ostatok.append(i)
LenghtValOst = len(ostatok)
DelenieKomp = LenghtValOst / 7

for i in ostatok:
    if LenghtValOst > DelenieKomp * 6:
        komp1.append(i)
    elif LenghtValOst > DelenieKomp * 5:
        komp2.append(i)
    elif LenghtValOst > DelenieKomp * 4:
        komp3.append(i)
    elif LenghtValOst > DelenieKomp * 3:
        komp4.append(i)
    elif LenghtValOst > DelenieKomp * 2:
        komp5.append(i)
    elif LenghtValOst > DelenieKomp:
        komp6.append(i)
    else:
        komp7.append(i)
    LenghtValOst -= 1

File = open('TestVal', 'w')
print(""" 
Тестовая:
""")
for i in TrValues:
    print(i, )
    File.write(i + '\n')
File.close()

File = open('Trvalues1', 'w')
print("""
Тренировочная 1:
""")
for i in komp2 + komp3 + komp4 + komp5 + komp6 + komp7:
    print(i)
    File.write(i + '\n')
File.close()

File = open('Valid1', 'w')
print(""" 
Валидационная 1:
""")
for i in komp1:
    print(i)
    File.write(i + '\n')
File.close()

File = open('Trvalues2', 'w')
print("""
Тренировочная 2:
""" )

for i in komp1 + komp3 + komp4 + komp5 + komp6 + komp7:
    print(i)
    File.write(i + '\n')
File.close()

File = open('Valid2', 'w')
print(""" 
Валидационная 2:
""")
for i in komp2:
    print(i)
    File.write(i + '\n')
File.close()

File = open('Trvalues3', 'w')
print(' Тренировочная 3:')
for i in komp1 + komp2 + komp4 + komp5 + komp6 + komp7:
    print(i)
    File.write(i + '\n')
File.close()

File = open('Valid3', 'w')
print(""" 
Валидационная 3:
""")
for i in komp3:
    print(i)
    File.write(i + '\n')
File.close()

File = open('Trvalues4', 'w')
print(' Тренировочная 4:')
for i in komp1 + komp2 + komp3 + komp5 + komp6 + komp7:
    print(i)
    File.write(i + '\n')
File.close()

File = open('Valid4', 'w')
print(""" 
Валидационная 4:
""")
for i in komp4:
    print(i)
    File.write(i + '\n')
File.close()

File = open('Trvalues5', 'w')
print(' Тренировочная 5:')
for i in komp1 + komp2 + komp3 + komp4 + komp6 + komp7:
    print(i)
    File.write(i + '\n')
File.close()

File = open('Valid5', 'w')
print(""" 
Валидационная 5:
""")
for i in komp5:
    print(i)
    File.write(i + '\n')
File.close()

File = open('Trvalues6', 'w')
print(' Тренировочная 6:')
for i in komp1 + komp2 + komp3 + komp4 + komp5 + komp7:
    print(i)
    File.write(i + '\n')
File.close()

File = open('Valid6', 'w')
print(""" 
Валидационная 6:
""")
for i in komp6:
    print(i)
    File.write(i + '\n')
File.close()

File = open('Trvalues7', 'w')
print(' Тренировочная 7:')
for i in komp1 + komp2 + komp3 + komp4 + komp5 + komp6:
    print(i)
    File.write(i + '\n')
File.close()

File = open('Valid7', 'w')
print(""" 
Валидационная 7:
""")
for i in komp7:
    print(i)
    File.write(i + '\n')
File.close()



File.close()

