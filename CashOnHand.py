from pathlib import Path
import csv

# create a file to csv file.
# fp = Path.cwd()/"CashOnHand.csv"
fp=Path.cwd()/'project_group_Ignite'/'csv_report_Ignite'/'CashOnHand.csv'

# read the csv file to append profit and quantity from the csv.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create 2 empty lists to store day and cash by each cluster
    cluster1 = []
    cluster2=[] 
    
    
    for day,cash in reader:
        cluster1.append(day)
        cluster2.append(cash)
    
    
        


converted1 = [float(num) for num in cluster1]
converted2 = [float(num) for num in cluster2]
# print(len(converted2))
one1=1
one=0
days=0
cash_deficit=[]
cash_surplus=[]
cash_surplus_all=[]

while days < len(converted2):
    days+=1
    
    if days<len(converted2):
        if converted2[one]>converted2[one1]:
            cash_deficit.append(f'[Cash Deficit] Day: {converted1[days]}, AMOUNT: ${converted2[one]-converted2[one1]}')
        
            one+=1
            one1+=1
    
        else:
            cash_surplus.append(f'{converted1[days]}')
            one+=1
            one1+=1
            if len(cash_surplus)==len(converted2)-1:
                cash_surplus_all.append(f'[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY')

    
