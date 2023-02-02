# Import Path method from pathlib 
from pathlib import Path

# import spreadsheet
import csv

# instantiate an file path object to current working directory
filepath2=Path.cwd()/'csv_report_Ignite'/'Profit&Loss.csv'

# create a new file with `.touch()`
filepath2.touch()

# read the csv file to append profit and loss from the cvs
with filepath2.open(mode='r',encoding='utf-8') as file:
    reader=csv.reader(file)

    # skip header
    next(reader)
    
    #Create 2 empty List
    cluster3=[]
    cluster4=[]

    #Append only the Profit_Loss and Day from the Csv
    for day,sales,profit,op,profitloss in reader:
        cluster3.append(day)
        cluster4.append(profitloss)

#Create 2 empty list
converted3 = []
converted4 = [] 
#converted the days and cash from string to a float and placed day in converted 1 and profit/loss into converted 2
for num in cluster3:
    converteda=float(num)
    converted3.append(converteda)
for num in cluster4:
    convertedb=float(num)
    converted4.append(convertedb)

def Profit_loss_function():
    """
    The program will compute the difference in the net profit column if net profit on the current day is lower than the previous day
    Write it into the summary_report.txt to be activated in the main.py
    """
    #Create a file path and create the summary_report.txt
    file_path=Path.cwd()/'summary_report.txt'
    file_path.touch()

    #Create 3 variables
    num_1=1
    num_2=0
    num_3=0

    #Create 3 empty List
    pl_deficit=[]
    pl_surplus=[]
    pl_surplus_all=[] 
    
    #Create a while loop
    while num_3 < len(converted4):
        #Ensure that the while loop continues until target is met
        num_3+=1

        #Create an if statement
        if num_3<len(converted4):
            #Check if the Profit/Loss on the current day is greater/less than the Profit/Loss the following day
            if converted4[num_2]>converted4[num_1]:
                #If there is a Profit deficit the programme will detect it and  append it into the list pl_deficit
                pl_deficit.append(f'[PROFIT DEFICIT] Day: {converted3[num_3]}, AMOUNT: ${converted4[num_2]-converted4[num_1]}')
                #Check if all the values have gone through the while loop
                if num_3 == len(converted4)-1:
                    #Append the results to summary text report
                    with file_path.open(mode='a',encoding='utf-8') as file1:
                        for deficit in pl_deficit:
                            file1.writelines(deficit +'\n')
                    #Return to receive a value
                    return(pl_deficit)
                else:
                    # Add a value of 1 to num_2 and num_1 variable
                    num_1+=1
                    num_2+=1   
            else :
                #Append into pl_surplus
                pl_surplus.append(f'{converted3[num_3]}')
                #If the length of pl_surplus is equal the length of converted 4 then there is profit surplus everyday
                if len(pl_surplus)==len(converted4)-1:
                    #Since there is profit/loss surplus everyday, append the statement into empty list pl_surplus_all
                    pl_surplus_all=(f'[PROFIT SURPLUS] PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY')
                    #Append the results to summary text report
                    with file_path.open(mode='a',encoding='utf-8') as file1:
                        file1.writelines(pl_surplus_all +'\n')
                        #Return to receive a value
                        return(pl_surplus_all)    
                else:
                    # add a value of 1 to num_2 and num_1 variable
                    num_1+=1
                    num_2+=1         
#Activate the Function           
print(Profit_loss_function())
