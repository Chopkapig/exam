import csv

with open("vacancy.csv", encoding="utf8") as file:
    reader = csv.DictReader(file, delimiter=";", quotechar='"')
    data = list(reader)[1:]
name= input()
while(name !="None"):
    name= str(name)
    for el in data:
        if str(el["company"]) == name:
            print(f"В {company} найдена вакансия: {role}. З/п составит: {Salary}")
            break
        else:
            print('К сожалению, ничего не удалось найти')
        name=  input()