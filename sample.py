### data.sample.py
# This is a sample data file for budget.py
# These values should be replaced with your own values

# Starting Savings
savings = 10000

# Saving each month
monthly_savings = 500

# Interest each month
yearly_interest = 0.05

# Forms of Income
income = {
  # Pay (Fortnightly)
  'Wage': 1500 * 2
}

# Outgoing Expenses
expense = {
  # Rent (Weekly)
  'Rent': 300 * 4,

  # Food (Weekly)
  'Food': 150 * 4,

  # Fuel (Weekly)
  'Fuel': 30 * 4,

  # Power Bill (Quarterly avg.)
  'Energy Bill': 250 / 3,

  # Internet Bill (Monthly)
  'Internet Bill': 60,

  # Phone Bill
  'Phone Bill': 40,
}