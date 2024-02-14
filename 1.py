import csv

with open("vacancy.csv", encoding="utf8") as file:
    reader = csv.reader(file, delimiter=";", quotechar='"')
    answer= list(reader)[1:]
    size={}
    tupe={}

    for salary, work_Type, company_Size, role, company in answer:
        count =1
        if "52000" in salary:
            print(f"{count}. {company}-{role}-{salary}")
        count+=1
        if "51200" in salary:
            print(f"{count}. {company}-{role}-{salary}")
            count+=1
        if "50400" in salary:
            print(f"{count+1}. {company}-{role}-{salary}")
            count+= 1
            break
with open("vacancy_new.csv","w", encoding="utf",newline="") as file:
    w = csv.writer(file, delimiter=";")
    w.writerow(['company','role','solary'])
    w.writerows(answer)