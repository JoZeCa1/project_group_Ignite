# Import Path method from pathlib.
from pathlib import Path
import csv

# Instantiate an file path object to current working directory.
file_path_overheads=Path.cwd()/'csv_report_Ignite'/'Overheads.csv'

# Create a new file with `.touch()`.
file_path_overheads.touch()

# Open file_path_overheads with .open() to return a file object.
with file_path_overheads.open(mode='r',encoding='utf-8') as file:

    # Instantiate a reader object.
    reader=csv.reader(file)

    # Use `next()` to skip the header.
    next(reader)

    # Create an empty list called Cluster5.
    Cluster5=[]

    # Using a for loop extract data from reader and append into Cluster5.
    for num in reader:
        Cluster5.append(num)
   
# Create empty list called Converted5.
Converted5=[]

# Convert the percentage values from Cluster5 into a float form String and append into Converted5.
for x in Cluster5:
    Convertedx=[x[0],float(x[1])]
    Converted5.append(Convertedx)

# Create two empty lists.
Overheads=[]
Overheads2=[]

def overhead():

    """
    
    This function helps the team find the highest overhead category

    """
    # Extract the 2 global scope empty list using global method into a local scope.
    global Overheads
    global Overheads2

    # Create 2 variables that will be used later in the function.
    num_1=0
    num_2=1

    # Append the first value form Converted5 into Overheads2 which will be used for comparision purposes later in the function.
    Overheads2.append(Converted5[0])
    
    # Create a while loop.
    while num_1<len(Converted5):

        # Add a value of 1 to num_1 variable.
        num_1+=1 
        
        # Create an if statement.
        if num_1<len(Converted5):
            
            # Check if the value in Converted5 is greater than value of Values in the overheads2.
            if Converted5[num_1][num_2]>Overheads2[0][1]:
                
                # If the requirements above are met, remove the items in the Overheads2.
                Overheads2.pop(0)

                # Append the Greater Value into Overheads2.
                Overheads2.append(Converted5[num_1])
                
                # Once all the values in Converted5 has gone through the function.
                if num_1==len(Converted5)-1:

                    # Append the Highest Overhead into the lsit Overhead.
                    Overheads.append(f'[Highest Expense] {Overheads2}')

                    # Return to receive results.
                    return(Overheads)
                
            # Else statement is not required as code should run only if the statement above is true.
            # If it does not meet the requirements above.    
            else:

                # Once all the values in Converted5 has gone through the function.
                if num_1==len(Converted5)-1:

                    # Append the Highest Overhead into the lsit Overhead.
                    Overheads.append(f'[Highest Expense] {Overheads2[0][0]} {Overheads2[0][1]}%')

                    # Return to receive results.
                    return(Overheads)

        # Else statement is not required as code should run only if the statement above is true.
        else:
            return(Overheads)        
            
print(overhead())
