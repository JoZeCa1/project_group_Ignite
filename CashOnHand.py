# Import Path method from pathlib
from pathlib import Path
# Import all the csv
import csv

# instantiate an file path object to current working directory
fp = Path.cwd()/"csv_report_Ignite"/"CashOnHand.csv"

# create a new file with `.touch()`
fp.touch()

# open file_path_overheads with .open() to return a file object
with fp.open(mode="r", encoding="UTF-8", newline="") as file:

    # instantiate a reader object
    reader = csv.reader(file)

    # use `next()` to skip the header.
    next(reader)

    # Create 2 empty lists
    cluster1 =[]
    cluster2=[] 
    
    # Create a for loop to separate day and cash
    for day,cash in reader:     
        # Append to have only day in cluster 1 list, and append cash into cluster2
        cluster1.append(day)
        cluster2.append(cash)

#Create 2 empty list
converted1=[]
converted2=[]
#converted the days and cash from string to a float and place converted day in converted 1 and cash into converted 2
for num in cluster1:
    convertedx=float(num)
    converted1.append(convertedx)
for num in cluster2:
    convertedy=float(num)
    converted2.append(convertedy)

def coh_function():
    """
    This program will compute the difference in Cash-on-Hand if the current day is lower than the previous day.
    Write it into the summary_report.txt to be activated in the main.py
    """
    #Create a file path and create the summary_report.txt
    file_path=Path.cwd()/'summary_report.txt'
    file_path.touch()

    #Create three random variable used for later parts of the function
    num_1=1
    num_2=0
    num_3=0

    #Create 3 empty list
    cash_deficit=[]
    cash_surplus=[]
    cash_surplus_all=[]   
    
    #Create a while loop
    while num_3 < len(converted2):

        #Ensure that the while loop continues until target is meet.
        num_3+=1

        #Create if statement
        if num_3<len(converted2):

            #Check if the cash on hand on the current day is greater/lesser than the cash on hand the following day
            if converted2[num_2]>converted2[num_1]: 
                #If there is a cash deficit the programme will detect it and  append it into the list cash_deficit 
                cash_deficit.append(f'[CASH DEFICIT] DAY: {converted1[num_3]}, AMOUNT: ${converted2[num_2]-converted2[num_1]}')
                #Once all the values have gone through the while loop then return cash deficit
                if num_3 == len(converted2)-1:
                    #Append the results from cash deficit into the summary text report
                    with file_path.open(mode='a',encoding='utf-8') as file2:
                        for deficit in cash_deficit:
                            file2.writelines(deficit +'\n')
                    #Return to receive a value
                    return(cash_deficit)
                #If it does not meet the requirements in line 75    
                else:
                    #Add a value of 1 to num_2 and num_1variable
                    num_2+=1
                    num_1+=1      
            #If it does not meet the requirements in line 71    
            else:
                #Append into cash_surplus 
                cash_surplus.append(f'{converted1[num_3]}')
                #If the length of cash_surplus is equal the length of converted 2 then there is cash surplus everyday
                if len(cash_surplus)==len(converted2)-1:
                    #Since there is cash surplus everyday, append the statement into empty list cash_surplus_all
                    cash_surplus_all=(f'[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY')
                    #Append the results into the summary text report
                    with file_path.open(mode='a',encoding='utf-8') as file2:
                        file2.writelines(cash_surplus_all +'\n')
                    #Return to receive a value
                    return(cash_surplus_all)
                #If it does not meet the requirements in line 90
                else:
                    # Add a value of 1 to num_2 and num_1 variable
                    num_2+=1
                    num_1+=1 
#Activate the function           
print(coh_function())
