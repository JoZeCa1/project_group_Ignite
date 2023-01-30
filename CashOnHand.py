from pathlib import Path
import csv

# create a file to csv file.
fp = Path.cwd()/"csv_report_Ignite"/"CashOnHand.csv"

#HI TESTER
# read the csv file to append day and cash on hand from the csv.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create 2 empty lists to store day and cash for each cluster
    cluster1 = []
    cluster2=[] 
    
    # create a for loop to separate day and cash
    for day,cash in reader:
        #append the day in cluster 1 list
        cluster1.append(day)
        #append the cash in cluster 2 list
        cluster2.append(cash)

#create 3 empty list used for later
cash_deficit=[]
cash_surplus=[]
cash_surplus_all=[]      

#converted the days and cash from string to a float and place converted day in converted 1 and cash into converted 2
converted1 = [float(num) for num in cluster1]
converted2 = [float(num) for num in cluster2]

#create a function called conversion 1
def conversion1():
    #create three random variable used for later parts of the function
    one1=1
    one=0
    days=0
    #extract the 3 empty list using global method 
    global cash_deficit, cash_surplus,cash_surplus_all
    
    #create a while loop
    while days < len(converted2):
        #to ensure that the while loop continues until target is meet.
        days+=1
        
        #create if statement
        if days<len(converted2):
            #create another if statement to check if the sum of the cash in day ... is greater than the new day
            if converted2[one]>converted2[one1]:
                #if there is a cash deficit the programme will detect it and  append it into cash_deficit 
                cash_deficit.append(f'[Cash Deficit] Day: {converted1[days]}, AMOUNT: ${converted2[one]-converted2[one1]}')
                #once all the values have gone through the while loop then return cash deficit
                if days == len(converted2)-1:
                    #return to receive a value
                    return(cash_deficit)
                #else the whole while loop repeats until all the values from each day have gone through
                else:
                    one+=1
                    one1+=1
                
            #if the cash on the present day is lower than the next day
            else :
                #append into cash_surplus 
                cash_surplus.append(f'{converted1[days]}')
                #if the length of cash_surplus is equal the length of converted 2 then there is cash surplus everyday
                if len(cash_surplus)==len(converted2)-1:
                    
                    #since there is cash surplus everyday, append the statement into empty list cash_surplus_all
                    cash_surplus_all.append(f'[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY')
                    #return to receive a value
                    return(cash_surplus_all)

                #if the length of cash_surplus is not equal the length of converted 2 repeat the while loop 
                else:
                   one+=1
                   one1+=1 
                   

#print to activate the function           
print(conversion1())
