# Import Path method from pathlib.
from pathlib import Path

# Import spreadsheet.
import csv

# Instantiate an file path object to current working directory.
filepath2=Path.cwd()/'csv_report_Ignite'/'Profit&Loss.csv'

# Create a new file with `.touch()`.
filepath2.touch()

# read the csv file to append profit and loss from the csv.
with filepath2.open(mode='r',encoding='utf-8') as file:
    reader=csv.reader(file)
    # skip header 
    next(reader)
    
    # create 2 empty lists to store profit and loss by each cluster
    cluster3=[]
    cluster4=[]

    for day,sales,profit,op,profitloss in reader:
        cluster3.append(day)
        cluster4.append(profitloss)

    

converted3 = [float(num) for num in cluster3]
converted4 = [float(num) for num in cluster4]



pl_deficit=[]
pl_surplus=[]
pl_surplus_all=[]      


def conversion1():
    """
    Pls add DocStrings TY

    """
    num_1=1
    num_2=0
    num_3=0
    none=[]
    global pl_deficit, pl_surplus,pl_surplus_all
    

    while num_3 < len(converted4):
        num_3+=1
        
        if num_3<len(converted4):
            
            if converted4[num_2]>converted4[num_1]:

                pl_deficit.append(f'[Profit Deficit] Day: {converted3[num_3]}, AMOUNT: ${converted4[num_2]-converted4[num_1]}')
                
                if num_3 == len(converted4)-1:
                    return(pl_deficit)
                else:
                    num_1+=1
                    num_2+=1
                

            else :

                pl_surplus.append(f'{converted3[num_3]}')

                if len(pl_surplus)==len(converted4)-1:
                    
                    pl_surplus_all.append(f'[PROFIT SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY')

                    return(pl_surplus_all)

                    
                else:
                   num_1+=1
                   num_2+=1 
        else:
            return(None)           

            
print(conversion1())
