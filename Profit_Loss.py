# Import Path method from pathlib.
from pathlib import Path

# Import spreadsheet.
import csv

# Instantiate an file path object to current working directory.
filepath2=Path.cwd()/'csv_report_Ignite'/'Profit&Loss.csv'

# Create a new file with `.touch()`.
filepath2.touch()

# read the csv file to append the profit and loss from the csv.
with filepath2.open(mode='r',encoding='utf-8') as file:
    reader=csv.reader(file)
    # skip header 
    next(reader)
    
    # create 2 empty lists to store profit and loss by each cluster
    cluster3=[]
    cluster4=[]
    
    # append profit and loss as a list back to each empty list
    for day,sales,profit,op,profitloss in reader:
        cluster3.append(day)
        cluster4.append(profitloss)

# convert the numbers in each cluster into float
converted3 = [float(num) for num in cluster3]
converted4 = [float(num) for num in cluster4]

# create 3 new clusters
pl_deficit=[]
pl_surplus=[]
pl_surplus_all=[]      

# def function 
def conversion1():
    
    # Docstrings is considered as the comment. Briefly describes the function of this code.
    """
    
    The program will compute the difference in the net profit column if net profit on the current day is lower than the previous day
    
    """
    
    # creating 3 new variables
    num_1=1
    num_2=0
    num_3=0
    none=[]
    global pl_deficit, pl_surplus,pl_surplus_all
    
    # while num_3 is lesser than. len() function returns the number of items in converted 4 variable. 
    while num_3 < len(converted4):
        # += adds the value of the right operand to a variable and assigns the result to the variable.
        num_3+=1
        
        # if function
        if num_3<len(converted4):
            
            # if function. if num_2 in variable converted4 is larger than num_1 in variable converted4.
            if converted4[num_2]>converted4[num_1]:
                
                # append the variable pl_deficit, which appends a new element at the end of a list. 
                pl_deficit.append(f'[Profit Deficit] Day: {converted3[num_3]}, AMOUNT: ${converted4[num_2]-converted4[num_1]}')
                
                # if function. if num_3 is equal to len() of variable converted4 minus 1. 
                if num_3 == len(converted4)-1: 
                    return(pl_deficit)
                
                # else function
                else:
                    num_1+=1
                    num_2+=1
                    
            # else function
            else:
                
                # append the variable pl_surplus, which appends a new element at the end of a list.
                pl_surplus.append(f'{converted3[num_3]}')
                
                # if function. if len() pl_surplus is equal to len () of converted4 minus 1. 
                if len(pl_surplus)==len(converted4)-1:
                    
                    # append the variable  pl_surplus_all, which appends a new element at the end of a list.
                    pl_surplus_all.append(f'[PROFIT SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY')
                    
                    # return function
                    return(pl_surplus_all)

                # else function 
                else:
                   num_1+=1
                   num_2+=1 
        # else function
        else:
            return(None)           

# print variable conversion1            
print(conversion1())
