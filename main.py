# Importing all the three files Overheads.py, CashOnHand.py and Profit_Loss.py into the Main.py.
import Overheads, CashOnHand,Profit_Loss

# Import Path method from pathlib.
from pathlib import Path

# def function.
def main():

    """
    Modularizing the Functions from Overheads.py, ProfitLoss.py and CashOnHand.py.
    Print the results from all the 3 different files into the summary_report.txt
    """
    
    # Extracting data from the 3 different files.
    from Profit_Loss import pl_deficit,pl_surplus_all
    from CashOnHand import cash_deficit,cash_surplus_all
    from Overheads import Overheads

    # Instantiate an file path object to current working directory.
    file_path=Path.cwd()/'summary_report.txt'

    # Create a new file with `.touch()`.
    file_path.touch()

    # Writing the results from the three different files into the summary_report.txt and leave spaces in between.
    with file_path.open(mode='w',encoding='utf-8') as file:
        for deficit in cash_deficit:
            file.writelines(deficit +'\n')
        for surplus in cash_surplus_all:
            file.writelines(surplus+'\n')
        for deficit in pl_deficit:
            file.writelines(deficit +'\n')
        for surplus in pl_surplus_all:
            file.writelines(surplus+'\n')
        for highest in Overheads:
            file.writelines(highest+'\n')

# Executing the function.   
print(main())
