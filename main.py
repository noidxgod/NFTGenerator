import os
import itertools
from PIL import Image
import zipfile
import random

def rep(a):
    simbol = "\ "
    simbol = simbol.replace(" ",'')
    simbol2 = '"'
    a = a.replace(simbol,'/')
    a = a.replace(simbol2,'')
    a = a.replace(' ','')
    return(a)
print("Путь к основной папке:")
pathh = "C:/2"#str(input())
pathh = rep(pathh)

test = os.walk(pathh)
path, dirs, files = next(test)
folders = []
amountfiles = []
filepaths = []
for i in range(len(dirs)):
    folders.append(str(dirs[i]))
    filepaths.append([])
print()
for i in range(0, len(folders)):
    test = os.walk(pathh + "/" + str(folders[i]))
    path, dirs, files = next(test)
    for j in range(0,len(files)):
        filepaths[i].append(pathh + "/"+ str(folders[i])+ "/" + files[j])
    amountfiles.append(len(files))
for i in range(0,len(folders)):
    print(str(folders[i]) + " - " + str(amountfiles[i]))

maxamountnft = 1
for i in range(0,len(amountfiles)):
    maxamountnft = maxamountnft * amountfiles[i]
print("Итоговое количество: ", maxamountnft)
print()
print("Вставьте путь к телу:")
pathhofmain = str(input())
pathhofmain = rep(pathhofmain)
peres = (list(itertools.product(*filepaths)))
print("Введите общее название итоговых файлов:")
nameofresult = str(input())
print("Вставьте путь, куда сохранить итоговые результаты:")
pathhofresult = str(input())
pathhofresult = rep(pathhofresult)
print("Максимальное количество?(Y/N)")
ans = str(input())
rando = []
if ans == "Y" or ans == 'y':
    for i in range(0, maxamountnft):
        print('\r', 'Процесс', str(i * 100 // maxamountnft), '%', end='')
        pathhofmainimage = pathhofmain
        for j in range(0, len(amountfiles)):
            if j != 0:
                img = Image.open(pathhofmainimage)
                watermark = Image.open(peres[i][j])
                img.paste(watermark, (0, 0), watermark)
                img.save(pathhofresult + '/' + nameofresult + str(i + 1) + ".png")
            else:
                img = Image.open(peres[i][j])
                watermark = Image.open(pathhofmainimage)
                img.paste(watermark, (0, 0), watermark)
                img.save(pathhofresult + '/' + nameofresult + str(i + 1) + ".png")
            pathhofmainimage = pathhofresult + '/' + nameofresult + str(i + 1) + ".png"
    print('\r', str(100), '%', end='')
else:
    print("Введите требуемое количество:")
    fixamountnft = int(input())
    i = 0
    while len(rando) != fixamountnft:
        buf = []
        for j in range(0, len(amountfiles)):
            number = random.randrange(len(filepaths[j]))
            buf.append(filepaths[j][number])
        if buf not in rando:
            rando.append(buf)
        else:
            i = i - 1
        i = i + 1
    for i in range(0, fixamountnft):
        print('\r', 'Процесс', str(i * 100 // fixamountnft), '%', end='')
        pathhofmainimage = pathhofmain
        for j in range(0,len(amountfiles)):
            if j != 0:
                img = Image.open(pathhofmainimage)

                watermark = Image.open(rando[i][j])
                img.paste(watermark, (0, 0), watermark)
                img.save(pathhofresult + '/' + nameofresult + str(i + 1) + ".png")
            else:
                img = Image.open(rando[i][j])
                watermark = Image.open(pathhofmainimage)
                img.paste(watermark, (0, 0), watermark)
                img.save(pathhofresult + '/' + nameofresult + str(i + 1) + ".png")
            pathhofmainimage = pathhofresult + '/' + nameofresult + str(i + 1) + ".png"
print()
print(" Завершено!!!")
print("Добавить итоговые файлы в архив?(Y/N)")
ans = str(input())
if ans == "Y" or ans == 'y':
    print("Введите название архива:")
    files = os.listdir(pathhofresult)
    nameofzip = str(input())
    newzip = zipfile.ZipFile(pathhofresult + '/' + nameofzip + ".zip",'w') #создаем архив
    for f in files:
        arcname = files[i]
        newzip.write(pathhofresult + "/" + f,arcname = f)
    print("Готово!")
print("Завершено!")