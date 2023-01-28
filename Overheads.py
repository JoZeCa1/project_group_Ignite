from pathlib import Path
import csv

file_path_overheads=Path.cwd()/'csv_report_Ignite'/'Overheads1.csv'
# file_path_overheads.touch()
# print(file_path_overheads.exists())

with file_path_overheads.open(mode='r',encoding='utf-8') as file:
    reader=csv.reader(file)
    next(reader)

    
    Cluster5=[]
    Cluster6=[]
    for num in reader:
        Cluster5.append(num)
   
#
# Converted5=[[x[0],float(x[1])] for x in Cluster5]
Converted5=[]
for x in Cluster5:
    Convertedx=[x[0],float(x[1])]
    Converted5.append(Convertedx)


testerbot2=[]
testerbot=[]

def overhead():
    global testerbot2
    global testerbot
    day=0
    dayed=1
    testerbot.append(Converted5[0])
    
    while day<len(Converted5):
        day+=1 
        
        if day<len(Converted5):
            
            
            if Converted5[day][dayed]>testerbot[0][1]:
                
                testerbot.pop(0)
                testerbot.append(Converted5[day])
                
                if day==len(Converted5)-1:
                    testerbot2.append(f'[Highest Expense] {testerbot}')
                    return(testerbot2)
                
            else:
                if day==len(Converted5)-1:
                    testerbot2.append(f'[Highest Expense] {testerbot[0][0]} {testerbot[0][1]}%')
                    return(testerbot2)
                
            
print(overhead())

                













