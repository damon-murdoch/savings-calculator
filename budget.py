# Operating System Library
import os

# Shell Utility Library
import shutil

# Import Module Library
import importlib

# For Monthly: rate = yearly_interest / 12
# For Yearly: rate = yearly_interest
def simple_interest(amount, rate, time):

  # Return the simple interest to the calling process
  return ((amount * rate * time) / 100)

# For Monthly: rate = yearly_interest / 12
# For Yearly: rate = yearly_interest
def compound_interest(amount, rate, time):

  # Return the compound interest to the calling process
  return (amount * ((1 + rate / 100) ** time))

# To calculate budget: 
def calculate_budget(

  # Savings
  savings, 

  # Monthly Savings
  monthly_savings, 

  # Yearly Interest
  yearly_interest, 

  # Incomes Table
  incomes,

  # Expenses Table
  expenses, 
):

  # Income Minus Expenses
  remainder = incomes - expenses - monthly_savings

  print("=== Monthly Statistics ===")
  print()

  # Print the total income to the screen
  print("Income:","$" + str(incomes))

  for income in data.income:

    print ('- ' + income + ': $' + str(data.income[income]) + '/mo')

  print()

  # Print the total expense to the screen
  print("Expense:","$" + str(expenses))

  for expense in data.expense:

    print ('- ' + expense + ': $' + str(data.expense[expense]) + '/mo')

  print()

  # Print the total savings to the screen
  print("Savings:","$" + str(monthly_savings))

  # Print the income minus expenses
  print("Remaining:","$" + str(remainder))

  print()
  print("=== Projected Savings ===")
  print()

  # Loop over the months
  for i in range(1,241):

    # Calculate the savings for the current month
    savings = compound_interest(savings + monthly_savings, yearly_interest/12, 1)

    # Print every month for the next year
    if i in [1,2,3,4,5,6,7,8,9,10,11,12]:
      print("Savings (" + str(round(i)) + " month(s)): " + "$" + str(savings))

    # Print 2, 3, 4, 5, 6, 7, 8, 9, 10 and 20 years
    if i in [24,36,48,60,72,84,96,108,120,240]:
      print("Savings (" + str(round(i/12)) + " years(s)): " + "$" + str(savings))

# Main  Function Loop
if __name__ == '__main__':

  # Source the data is pulled from
  # import data

  # Get the current script path
  path = os.path.dirname(__file__)
  
  try: # Import the data

    # Import Data File
    import data
    
  except: # No data file to import

    # Import Sample File
    import sample as data

  # Local version of savings
  savings = data.savings

  # Local version of savings each month
  monthly_savings = data.monthly_savings

  # Interest each month
  yearly_interest = data.yearly_interest

  # Summarise the income
  incomes = sum(data.income.values())

  # Summarise the expenses
  expenses = sum(data.expense.values())

  # Calculate the Budget
  calculate_budget(

    # Starting Savings
    savings, 

    # Monthly Savings
    monthly_savings, 

    # Yearly Interest
    yearly_interest,

    # Income Table
    incomes,

    # Expenses Table
    expenses
  )