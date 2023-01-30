# import Path 
from pathlib import Path
# import spreadsheet
import csv

# create a file to csv file
filepath2=Path.cwd()/'csv_report_Ignite'/'Profit&Loss1.csv'

# read the csv file to append profit and loss from the cvs
with filepath2.open(mode='r',encoding='utf-8') as file:
    reader=csv.reader(file)
    # skip header
    next(reader)
    
    # create 2 empty lists to store profit and loss by each cluster
    cluster1=[]
    cluster2=[]

    for day,sales,profit,op,profitloss in reader:
        cluster1.append(day)
        cluster2.append(profitloss)

    # print(cluster2)
    # print(cluster1)

converted3 = [float(num) for num in cluster1]
converted4 = [float(num) for num in cluster2]



pl_deficit=[]
pl_surplus=[]
pl_surplus_all=[]      

# print(len(converted2))
def conversion1():
    one1=1
    one=0
    days=0
    global pl_deficit, pl_surplus,pl_surplus_all
    

    while days < len(converted4):
        days+=1
        # print(days)
        if days<len(converted4):
            # print(days)
            if converted4[one]>converted4[one1]:

                pl_deficit.append(f'[Profit Deficit] Day: {converted3[days]}, AMOUNT: ${converted4[one]-converted4[one1]}')
                
                if days == len(converted4)-1:
                    return(pl_deficit)
                else:
                    one+=1
                    one1+=1
                

            else :

                pl_surplus.append(f'{converted3[days]}')

                if len(pl_surplus)==len(converted4)-1:
                    # print(len(cash_surplus))
                    # print(len(converted2))
                    pl_surplus_all.append(f'[PROFIT SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY')

                    return(pl_surplus_all)

                    
                else:
                   one+=1
                   one1+=1 
                   

            
print(conversion1())
