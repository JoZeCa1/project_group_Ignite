# Import Path method from pathlib.
from pathlib import Path
# Import all the csv.
import csv

# instantiate an file path object to current working directory.
fp = Path.cwd()/"csv_report_Ignite"/"CashOnHand.csv"

# Create a new file with `.touch()`.
fp.touch()

# Open file_path_overheads with .open() to return a file object.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:

    # Instantiate a reader object.
    reader = csv.reader(file)

    # Use `next()` to skip the header.
    next(reader)

    # Create 2 empty lists.
    cluster1 =[]
    cluster2=[] 
    
    # Create a for loop to separate day and cash.
    for day,cash in reader:
        
        # Append to have only day in cluster 1 list.
        cluster1.append(day)

        # Append to have only cash in cluster 2 list.
        cluster2.append(cash)

# Create 3 empty list to store the data for cash deficit and cash surplus.
cash_deficit=[]
cash_surplus=[]
cash_surplus_all=[]      

# Converted the days and cash from string to a float and place converted day in converted 1 and cash into converted 2.
converted1 = [float(num) for num in cluster1]
converted2 = [float(num) for num in cluster2]

# def function. Create a function called conversion 1.
def conversion1():
    """
    
    This program will compute the difference in Cash-on-Hand if the current day is lower than the previous day.
    
    """
    # Create three random variable used for later parts of the function.
    num_1=1
    num_2=0
    num_3=0
    none=[]

    # Extract the 3 global scope empty list using global method into a local scope .
    global cash_deficit, cash_surplus,cash_surplus_all
    
    # Create a while loop.
    while num_3 < len(converted2):

        # To ensure that the while loop continues until target is met
        num_3+=1
        
        # Create if statement.
        if num_3<len(converted2):

            # Check if the cash on hand on the current day is greater than the cash on hand the following day.
            if converted2[num_2]>converted2[num_1]: 

                # If there is a cash deficit the programme will detect it and  append it into the list cash_deficit. 
                cash_deficit.append(f'[Cash Deficit] Day: {converted1[num_3]}, AMOUNT: ${converted2[num_2]-converted2[num_1]}')

                # Once all the values have gone through the while loop then return cash deficit.
                if num_3 == len(converted2)-1:

                    # Return to receive a value.
                    return(cash_deficit)

                # Else the whole while loop repeats until all the values from each day have gone through.
                else:

                    # Add a value of 1 to num_2 variable.
                    num_2+=1

                    # Add a value of 1 to num_1 variable.
                    num_1+=1
                
            # The cash on the current day is lower than the following day.
            else:

                # Append into cash_surplus .
                cash_surplus.append(f'{converted1[num_3]}')

                # If the length of cash_surplus is equal the length of converted 2 then there is cash surplus everyday.
                if len(cash_surplus)==len(converted2)-1:
                    
                    # Since there is cash surplus everyday, append the statement into empty list cash_surplus_all.
                    cash_surplus_all.append(f'[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY')

                    # Return to receive a value.
                    return(cash_surplus_all)

                # If the length of cash_surplus does not hit the requirements above on line 96.
                else:

                    # Add a value of 1 to num_2 variable.
                    num_2+=1

                    # Add a value of 1 to num_1 variable.
                    num_1+=1 
        else:

            # If it does not meet the requirements above.
            return(none)   

# Print to activate the function           
print(conversion1())

